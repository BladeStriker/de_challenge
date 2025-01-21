import sqlite3
import random
import datetime
from de.utils import load_queries

queries = load_queries('de/queries.yaml')

# Function to generate ratings
def gen_ratings(conn):
    cur = conn.cursor()
    cur.execute(queries['create_ratings_table'])
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    date_range = (end_date - start_date).days

    for _ in range(100000):
        random_date = start_date + datetime.timedelta(days=random.randint(0, date_range))
        user_id = random.randint(1, 1000)
        product_id = random.randint(1, 1000)
        rating = random.randint(1, 5)
        cur.execute(queries['insert_rating'].format(random_date, user_id, product_id, rating))
    
    conn.commit()

# Function to compute monthly aggregates
def comp_monthly_agg(conn):
    cur = conn.cursor()
    cur.execute(queries['create_ratings_monthly_aggregates_table'])
    cur.execute(queries['insert_ratings_monthly_aggregates'])
    conn.commit()

# Function to find top products
def find_top_prod(conn):
    cur = conn.cursor()
    cur.execute(queries['find_top_prod'])
    return cur.fetchall()

# Main execution
if __name__ == '__main__':
    conn = sqlite3.connect('ratings.db')
    gen_ratings(conn)
    comp_monthly_agg(conn)
    top_products = find_top_prod(conn)
    for product in top_products:
        print(product)
    conn.close()