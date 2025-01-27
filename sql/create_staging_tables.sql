CREATE TABLE IF NOT EXISTS trip_staging (
    id SERIAL PRIMARY KEY,
    departure_date TIMESTAMP,
    return_date TIMESTAMP,
    departure_flight_id VARCHAR,
    return_flight_id VARCHAR,
    price NUMERIC,
);

CREATE TABLE IF NOT EXISTS flight_details_staging (
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