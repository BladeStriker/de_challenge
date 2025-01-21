import sqlite3
import pytest
from de.main import gen_ratings, comp_monthly_agg, find_top_prod

# Create an in-memory SQLite database for testing
@pytest.fixture
def db():
    conn = sqlite3.connect(':memory:')
    yield conn
    conn.close()

# Test the gen_ratings function
def test_gen_ratings(db):
    gen_ratings(db)
    cur = db.cursor()
    cur.execute('SELECT COUNT(*) FROM Ratings')
    count = cur.fetchone()[0]
    assert count == 100000

# Test the comp_monthly_agg function
def test_comp_monthly_agg(db):
    gen_ratings(db)
    comp_monthly_agg(db)
    cur = db.cursor()
    cur.execute('SELECT COUNT(*) FROM RatingsMonthlyAggregates')
    count = cur.fetchone()[0]
    assert count > 0

# Test the find_top_prod function
def test_find_top_prod(db):
    gen_ratings(db)
    comp_monthly_agg(db)
    top_products = find_top_prod(db)
    assert len(top_products) > 0