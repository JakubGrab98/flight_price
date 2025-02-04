{{ config(
    materialized='incremental',
    unique_key=['flight_id', 'api_id']
) }}


SELECT
    flight_id,
    api_id,
    (fare_json->>'adults')::NUMERIC AS fare_adults,
    (fare_json->>'children')::NUMERIC AS fare_children,
    (fare_json->>'infants')::NUMERIC AS fare_infants
FROM {{ ref('staging_flights') }}
