
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=5432,
        dbname=os.getenv("DB_NAME"),
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )


def test_connection():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT current_database()")
                result = cur.fetchone()
                print("Pidkluchena yspisne!")
                print("Bazza danih:", result[0])
    except (psycopg.Error, OSError, ValueError):
        print("Pomilka pidkluchena do PostgreSQL.")


if __name__ == "__main__":
    test_connection()

