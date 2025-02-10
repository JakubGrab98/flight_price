{{ config(materialized='table') }}

SELECT
    departure_airport,
    arrival_airport,
    COUNT(*) AS total_flights,
    AVG(price::numeric) AS avg_ticket_price,
    SUM(price::numeric) AS total_revenue
FROM {{ ref('transformed_flights') }}
GROUP BY departure_airport, arrival_airport
ORDER BY total_revenue DESC
