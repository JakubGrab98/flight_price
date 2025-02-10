{{ config(materialized='table') }}

SELECT
    airline,
    COUNT(*) AS total_flights,
    AVG(price::numeric) AS avg_ticket_price,
    COUNT(DISTINCT departure_airport) AS unique_departure_airports,
    COUNT(DISTINCT arrival_airport) AS unique_arrival_airports
FROM {{ ref('transformed_flights') }}
GROUP BY airline
