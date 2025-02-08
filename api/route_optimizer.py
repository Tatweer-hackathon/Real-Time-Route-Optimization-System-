import psycopg2
import networkx as nx

def calculate_optimal_route(origin, destinations):
    # Connect to PostgreSQL
    conn = psycopg2.connect("dbname=logistics user=postgres password=postgres host=localhost")
    cur = conn.cursor()

    # Fetch real-time traffic data and distances
    cur.execute("""
        WITH traffic_data AS (
            SELECT 
                d1.point_id AS origin_id,
                d2.point_id AS destination_id,
                ST_Distance(d1.location, d2.location) AS distance,
                COALESCE(rt.speed_kmh, hd.traffic_factor * 50) AS speed  -- Default speed if no real-time data
            FROM delivery_points d1
            CROSS JOIN delivery_points d2
            LEFT JOIN realtime_traffic rt ON ST_Intersects(
                ST_MakeLine(d1.location::geometry, d2.location::geometry),
                rt.coordinates::geometry
            )
            LEFT JOIN historical_deliveries hd ON hd.point_id = d2.point_id
            WHERE d1.point_id = %s AND d2.point_id IN %s
        )
        SELECT origin_id, destination_id, distance / speed AS travel_time
        FROM traffic_data
    """, (origin, tuple(destinations)))

    # Build graph with real-time travel times
    G = nx.Graph()
    for origin_id, dest_id, travel_time in cur:
        G.add_edge(origin_id, dest_id, weight=travel_time)

    # Calculate shortest path
    return nx.shortest_path(G, source=origin, weight='weight')