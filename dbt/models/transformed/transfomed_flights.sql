{{ config(
    materialized='incremental',
    unique_key=['flight_id', 'api_id']
) }}


SELECT
    flight_id,
    api_id,
    departure_airport,
    arrival_airport,
    arrival_city,
    departure_city,
    price,
    jsonb_array_elements_text(airlines_json) AS airline,
    created_at
FROM {{ ref('staging_flights') }}
