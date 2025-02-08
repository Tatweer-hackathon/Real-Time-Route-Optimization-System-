
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE delivery_points (
   point_id BIGSERIAL PRIMARY KEY,
   location GEOGRAPHY(POINT,4326),
   delivery_window_start TIME,
   delivery_window_end TIME,
   average_service_time INT
);

CREATE TABLE historical_deliveries (
   delivery_id BIGSERIAL PRIMARY KEY,
   route_id BIGINT,
   point_id BIGINT REFERENCES delivery_points(point_id),
   actual_arrival_time TIMESTAMP,
   actual_service_time INT,
   traffic_factor DECIMAL(3,2),
   weather_condition VARCHAR(50)
);
