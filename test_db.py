from sqlalchemy import create_engine, text
import pytest

DATABASE_URL = "postgresql+psycopg2://postgres:333@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

@pytest.fixture(scope="function")
def db_conn():
    """Фикстура для чистого подключения на каждый тест"""
    conn = engine.connect()
    trans = conn.begin()
    yield conn
    trans.rollback()
    conn.close()

def test_add_student(db_conn):
    insert_sql = text("INSERT INTO students (name, age) VALUES (:name, :age) RETURNING id")
    result = db_conn.execute(insert_sql, {"name": "John Doe", "age": 20})
    student_id = result.scalar()

    row = db_conn.execute(text("SELECT * FROM students WHERE id = :id"), {"id": student_id}).fetchone()
    assert row is not None

def test_update_student(db_conn):
    # Сначала добавить
    insert_sql = text("INSERT INTO students (name, age) VALUES (:name, :age) RETURNING id")
    result = db_conn.execute(insert_sql, {"name": "Jane Doe", "age": 22})
    student_id = result.scalar()
    # Обновить
    db_conn.execute(text("UPDATE students SET age = :age WHERE id = :id"), {"age": 23, "id": student_id})

    updated = db_conn.execute(text("SELECT age FROM students WHERE id = :id"), {"id": student_id}).fetchone()
    assert updated[0] == 23

def test_delete_student(db_conn):
    # Сначала добавить
    insert_sql = text("INSERT INTO students (name, age) VALUES (:name, :age) RETURNING id")
    result = db_conn.execute(insert_sql, {"name": "Alex Smith", "age": 19})
    student_id = result.scalar()
    # Удалить
    db_conn.execute(text("DELETE FROM students WHERE id = :id"), {"id": student_id})
    deleted = db_conn.execute(text("SELECT * FROM students WHERE id = :id"), {"id": student_id}).fetchone()
    assert deleted is None