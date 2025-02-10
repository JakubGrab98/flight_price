SELECT
    flight_id,
    api_id,
    departure_airport,
    arrival_airport,
    arrival_city,
    departure_city,
    price,
    jsonb_array_elements_text(airlines_json) AS airline,
    inserted_at
FROM {{ ref('staging_flights') }}
