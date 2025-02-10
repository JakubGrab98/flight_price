{{ config(materialized='table') }}

SELECT
    departure_airport,
    COUNT(*) AS total_departures,
    AVG(price::numeric) AS avg_departure_price,
    COUNT(DISTINCT arrival_airport) AS unique_destinations
FROM {{ ref('transformed_flights') }}
GROUP BY departure_airport
