SELECT
    id AS flight_id,
    data->>'flyFrom' AS departure_airport,
    data->>'flyTo' AS arrival_airport,
    data->>'cityTo' AS arrival_city,
    data->>'cityFrom' AS departure_city,
    (data->>'price')::NUMERIC AS price,
    data->'airlines' AS airlines_json,
    data->'fare' AS fare_json,
    data->'route' AS route_json,
    created_at
FROM {{ source('public', 'bronze_flights') }}
