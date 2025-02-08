import psycopg2
import json
def save_route_to_db(request_id, optimal_route):
    conn = psycopg2.connect("dbname=logistics user=postgres password=postgres host=localhost")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO optimized_routes (request_id, optimal_route)
        VALUES (%s, %s)
    """, (request_id, json.dumps(optimal_route)))
    conn.commit()

def fetch_optimal_route(request_id):
    conn = psycopg2.connect("dbname=logistics user=postgres password=postgres host=localhost")
    cur = conn.cursor()
    cur.execute("""
        SELECT optimal_route FROM optimized_routes WHERE request_id = %s
    """, (request_id,))
    result = cur.fetchone()
    return result[0] if result else None