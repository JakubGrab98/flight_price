SELECT DISTINCT
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
    {{ dbt.current_timestamp() }} AS created_at
FROM {{ source('public', 'bronze_flights') }}
