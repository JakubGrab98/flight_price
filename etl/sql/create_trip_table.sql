CREATE TABLE IF NOT EXISTS trip (
    id SERIAL PRIMARY KEY,
    departure_date TIMESTAMP,
    return_date TIMESTAMP,
    departure_flight_id VARCHAR,
    return_flight_id VARCHAR,
    price NUMERIC,
);
