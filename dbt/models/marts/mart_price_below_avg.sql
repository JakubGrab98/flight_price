{{ config(materialized='table') }}

WITH avg_price AS (
    SELECT
        departure_airport,
        arrival_airport,
        AVG(price::numeric) AS avg_price
    FROM
        {{ ref('transformed_flights') }}
    GROUP BY
        departure_airport,
        arrival_airport
)

SELECT
    flight_id,
    f.departure_airport,
    f.arrival_airport,
    price
FROM
    {{ ref('transformed_flights') }} AS f
INNER JOIN avg_price AS a
    ON f.departure_airport = a.departure_airport
        AND f.arrival_airport = a.arrival_airport
WHERE
    price::numeric < a.avg_price
ORDER BY
    price::numeric
