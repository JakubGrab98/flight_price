CREATE TABLE IF NOT EXISTS bronze_flights (
    id SERIAL PRIMARY KEY,
    api_data JSONB,
    inserted_at TIMESTAMP
);
