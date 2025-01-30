SELECT
    flight_id,
    (fare_json->>'adults')::NUMERIC AS fare_adults,
    (fare_json->>'children')::NUMERIC AS fare_children,
    (fare_json->>'infants')::NUMERIC AS fare_infants
FROM {{ ref('staging_flights') }}
