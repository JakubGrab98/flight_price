CREATE TABLE IF NOT EXISTS flight_details (
    id SERIAL PRIMARY KEY,
    fly_from VARCHAR,
    city_from VARCHAR,
    country_from VARCHAR,
    fly_to VARCHAR,
    city_to VARCHAR,
    country_to VARCHAR,
    local_departure TIMESTAMP,
    local_arrival TIMESTAMP,
    airline VARCHAR,
    flight_no INTEGER,
);