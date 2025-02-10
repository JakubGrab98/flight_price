{{ config(materialized='table') }}

SELECT
    DATE_TRUNC('month', departure_time) AS month,
    AVG(price::numeric) AS avg_ticket_price,
    COUNT(*) AS total_flights
FROM {{ ref('transformed_routes') }} r
INNER JOIN
    {{ ref('transformed_flights') }} f
        ON r.flight_id = f.flight_id
WHERE r.departure_airport = 'WAW'
GROUP BY month
ORDER BY month
