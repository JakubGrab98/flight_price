WITH ranked_flights AS (
    SELECT
        id AS flight_id,
        (api_data::jsonb)->>'id' AS api_id,
        (api_data::jsonb)->>'flyFrom' AS departure_airport,
        (api_data::jsonb)->>'flyTo' AS arrival_airport,
        (api_data::jsonb)->>'cityTo' AS arrival_city,
        (api_data::jsonb)->>'cityFrom' AS departure_city,
        (api_data::jsonb->>'price')::NUMERIC AS price,
        (api_data::jsonb)->'airlines' AS airlines_json,
        (api_data::jsonb)->'fare' AS fare_json,
        (api_data::jsonb)->'route' AS route_json,
        inserted_at,
        ROW_NUMBER() OVER (
            PARTITION BY
                (api_data::jsonb)->>'id'
            ORDER BY inserted_at DESC
        ) AS row_num
    FROM {{ source('public', 'bronze_flights') }}
)

SELECT
    flight_id,
    api_id,
    departure_airport,
    arrival_airport,
    arrival_city,
    departure_city,
    price,
    airlines_json,
    fare_json,
    route_json,
    inserted_at,
    row_num
FROM ranked_flights
WHERE row_num = 1
