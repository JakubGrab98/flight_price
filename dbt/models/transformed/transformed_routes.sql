SELECT
    flight_id,
    route->>'id' AS segment_id,
    route->>'flyFrom' AS departure_airport,
    route->>'cityFrom' AS departure_city,
    route->>'flyTo' AS arrival_airport,
    route->>'cityTo' AS arrival_city,
    (route->>'flight_no')::INTEGER AS flight_number,
    route->>'airline' AS airline,
    (route->>'local_departure')::TIMESTAMP AS departure_time,
    (route->>'local_arrival')::TIMESTAMP AS arrival_time,
    (route->>'utc_departure')::TIMESTAMP AS utc_departure,
    (route->>'utc_arrival')::TIMESTAMP AS utc_arrival,
    (route->>'vehicle_type') AS vehicle_type
FROM {{ ref('staging_flights') }},
LATERAL jsonb_array_elements(route_json) AS route
