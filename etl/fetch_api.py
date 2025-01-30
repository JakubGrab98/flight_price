import os
import requests
import logging
import json
from datetime import datetime
import time
import psycopg2
from config import DB_CONFIG
import const as ct
import utils as ut


logger = logging.getLogger(__name__)

API_KEY = os.getenv("KIWI_API_KEY")

HEADERS = {
    "apikey": API_KEY,
}

def get_flight_data(params: dict):
    """Search flight detail based on user parameters

    Args:
        params (dict): Flight parameters for retrieving data from KIWI api.

    Returns:
        FlightData | None: Return flight data if there is flight with provided params.
    """
    try:
        response = requests.get(ct.SEARCH_URL, headers=HEADERS, params=params)
        data = response.json()
        logger.info("Flight data was retrieved!")
        return data
    except IndexError as e:
        logger.error(e.add_note("No flight available with such parameters"))
        return None
    except Exception as e:
        logger.error(f"An error occurred {e}")

def store_api_data(responses: list) -> None:
    """
    Inserts raw API data to bronze table within postgres.
    :param responses: List of retrieved JSON responses.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS bronze_flights (
                        id SERIAL PRIMARY KEY,
                        api_data JSONB,
                        inserted_at TIMESTAMP
                    );
                    """
                )
                for response in responses:
                    cur.execute(
                        """
                        INSERT INTO bronze_flights (api_data, inserted_at)
                        VALUES (%s, %s)
                        """,
                        (json.dumps(response), datetime.now())
                   )
                conn.commit()
                logger.info("Data inserted successfully!")
        except Exception as e:
            logger.error(f"An error occurred {e}")
        finally:
            conn.close()

def main():
    params = {
        "fly_from": "WAW",
        "date_from": ut.get_future_date(),
        "date_to": ut.get_future_date(num_months=6),
        "return_from": ut.get_future_date(3),
        "return_to": ut.get_future_date(num_days=3, num_months=6),
        "max_stopovers": 1,
        "curr": ct.CURRENCY,
    }

    all_responses = []

    for index, code in enumerate(ct.AIRPORT_CODES, 1):
        params["fly_to"] = code
        response = get_flight_data(params)
        if index % 30 == 0 or index == len(ct.AIRPORT_CODES):
            store_api_data(all_responses)
            all_responses = []
            time.sleep(60)
        if response:
            all_responses.append(response)

if __name__ == "__main__":
    main()
