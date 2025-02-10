SELECT
    flight_id,
    api_id,
    (fare_json->>'adults')::NUMERIC AS fare_adults,
    (fare_json->>'children')::NUMERIC AS fare_children,
    (fare_json->>'infants')::NUMERIC AS fare_infants,
    inserted_at
FROM {{ ref('staging_flights') }}
