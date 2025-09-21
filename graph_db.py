import streamlit as st
from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
        except Exception as e:
            st.error(f"Failed to create Neo4j driver: {e}")
            self.driver = None

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def add_chunk_with_entities(self, chunk_text, entities):
        if self.driver is None: return
        with self.driver.session() as session:
            session.execute_write(self._create_chunk_and_link_entities, chunk_text, entities)

    @staticmethod
    def _create_chunk_and_link_entities(tx, chunk_text, entities):
        # Create the Chunk node
        query = "MERGE (c:Chunk {text: $chunk_text}) RETURN c"
        tx.run(query, chunk_text=chunk_text)

        # For each entity, create the entity node and link it to the chunk
        for entity in entities:
            query = """
            MERGE (e:Entity {name: $entity_name})
            WITH e
            MATCH (c:Chunk {text: $chunk_text})
            MERGE (c)-[:MENTIONS]->(e)
            """
            tx.run(query, entity_name=entity, chunk_text=chunk_text)

    def get_context_for_terms(self, search_terms):
        if self.driver is None or not search_terms: return []
        with self.driver.session() as session:
            result = session.execute_read(self._find_chunks_by_cooccurrence, search_terms)
            return [record["context"] for record in result]

    @staticmethod
    def _find_chunks_by_cooccurrence(tx, terms):
        # This updated query is more flexible and ranks results by relevance.
        # It finds chunks connected to entities that match the search terms.
        query = """
        UNWIND $terms AS term
        MATCH (c:Chunk)-[:MENTIONS]->(e:Entity)
        WHERE toLower(e.name) CONTAINS toLower(term) OR toLower(term) CONTAINS toLower(e.name)
        WITH c, COLLECT(DISTINCT e.name) AS matched_entities, COUNT(DISTINCT e) AS score
        ORDER BY score DESC, size(c.text) ASC
        RETURN DISTINCT c.text AS context
        LIMIT 5
        """
        result = tx.run(query, terms=terms)
        return list(result)