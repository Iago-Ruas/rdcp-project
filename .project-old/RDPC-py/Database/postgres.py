import asyncpg


class Database:
    _pool = None  # Armazena o pool de conexões

    @classmethod
    async def init_pool(cls):
        """Inicializa o pool de conexões."""
        cls._pool = await asyncpg.create_pool(
            database="meu_banco",
            user="meu_usuario",
            password="minha_senha",
            host="localhost",
            port="5432",
            min_size=1,
            max_size=10,
        )

    @classmethod
    async def fetch(cls, query, *args):
        """Executa um SELECT e retorna os resultados."""
        async with cls._pool.acquire() as conn:
            return await conn.fetch(query, *args)

    @classmethod
    async def execute(cls, query, *args):
        """Executa comandos INSERT, UPDATE e DELETE."""
        async with cls._pool.acquire() as conn:
            return await conn.execute(query, *args)

    @classmethod
    async def create_tables(cls):
        """Cria as tabelas no banco de dados."""
        create_tables_sql = """
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

        CREATE TABLE IF NOT EXISTS Users (
            id UUID PRIMARY KEY DEFAULT,
            is_reviewer BOOLEAN NOT NULL,
            is_editor BOOLEAN NOT NULL,
            first_name VARCHAR(255) NOT NULL,
            full_surname VARCHAR(255) NOT NULL,
            full_surname_abbr VARCHAR(50) NOT NULL,
            social_name VARCHAR(255),
            cellphone VARCHAR(20),
            nationality VARCHAR(100)
        );

        CREATE TABLE IF NOT EXISTS Affiliations (
            id UUID PRIMARY KEY DEFAULT,
            user_id UUID NOT NULL,
            institution VARCHAR(255) NOT NULL,
            department VARCHAR(255),
            city VARCHAR(100),
            state VARCHAR(100),
            federal_unit VARCHAR(100),
            country VARCHAR(100),
            CONSTRAINT affiliations_user_fk FOREIGN KEY (user_id) 
                REFERENCES Users(id) 
                ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS Article (
            id UUID PRIMARY KEY DEFAULT,
            is_reviewed BOOLEAN NOT NULL,
            author_id UUID NOT NULL,
            reviewer_id UUID,
            article_language VARCHAR(50) NOT NULL,
            english_title VARCHAR(500),
            portuguese_title VARCHAR(500),
            spanish_title VARCHAR(500),
            conflict_existence BOOLEAN NOT NULL,
            third_party_data BOOLEAN NOT NULL,
            third_party_info TEXT,
            article_type VARCHAR(50) CHECK (article_type IN ('monografia', 'tese', 'artigo_publicado')),
            structured_summary TEXT,
            short_summary TEXT,
            article_area VARCHAR(255),
            references TEXT,
            exist_media BOOLEAN NOT NULL,
            media TEXT,
            article_pdf_file BYTEA,
            featured_image BYTEA,
            CONSTRAINT article_author_fk FOREIGN KEY (author_id) REFERENCES Users(id) ON DELETE CASCADE,
            CONSTRAINT article_reviewer_fk FOREIGN KEY (reviewer_id) REFERENCES Users(id) ON DELETE SET NULL
        );

        CREATE TABLE IF NOT EXISTS Bibliographic_References (
            id UUID PRIMARY KEY DEFAULT,
            article_id UUID NOT NULL,
            book_name VARCHAR(500) NOT NULL,
            book_author VARCHAR(255) NOT NULL,
            CONSTRAINT biblio_article_fk FOREIGN KEY (article_id) REFERENCES Article(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS Media (
            id UUID PRIMARY KEY DEFAULT,
            article_id UUID NOT NULL,
            image_name VARCHAR(255) NOT NULL,
            image BYTEA NOT NULL,
            CONSTRAINT media_article_fk FOREIGN KEY (article_id) REFERENCES Article(id) ON DELETE CASCADE
        );
        """
        async with cls._pool.acquire() as conn:
            await conn.execute(create_tables_sql)
        print("✅ Tabelas criadas com sucesso!")


# Executando a inicialização
async def main():
    await Database.init_pool()
    await Database.create_tables()


# Rodando o script
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
