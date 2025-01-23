import os
import requests
import logging
import json
from datetime import datetime
import pandas as pd
import const as ct
import utils as ut

logger = logging.getLogger(__name__)

API_KEY = os.getenv("KIWI_API")
LOCATION_URL = "https://api.tequila.kiwi.com/locations/query"
SEARCH_URL = "https://api.tequila.kiwi.com/v2/search?"

HEADERS = {
    "apikey": API_KEY,
}

def get_european_iata_codes():
    iata_codes = pd.read_csv(r"C:\Users\kubag\PycharmProjects\flight_price\data\raw\iata_codes.csv")
    euro_countries = iata_codes[
        (iata_codes["latitude"].between(35, 72))
        & (iata_codes["longitude"].between(25, 65))
    ]
    return euro_countries["iata"]

def get_flight_data(params: dict):
    """Search flight detail based on user parameters

    Args:
        params (dict): Flight parameters for retrieving data from KIWI api.

    Returns:
        FlightData | None: Return flight data if there is flight with provided params.
    """
    response = requests.get(ct.SEARCH_URL, headers=HEADERS, params=params)

    try:
        data = response.json()["data"][0]
        logger.info("Flight data was retrieved!")
        return data
    except IndexError as e:
        logger.error(e.add_note("No flight available with such parameters"))
        return None
    #
    # flight_data = FlightData(
    #     price=data["price"],
    #     origin_city=data["route"][0]["cityFrom"],
    #     origin_airport=data["route"][0]["flyFrom"],
    #     destination_city=data["route"][0]["cityTo"],
    #     destination_airport=data["route"][0]["flyTo"],
    #     departure_date=data["route"][0]["local_departure"].split("T")[0],
    #     departure_time=data["route"][0]["local_departure"].split("T")[1][0:5],
    #     return_date=data["route"][1]["local_departure"].split("T")[0],
    #     return_time=data["route"][1]["local_departure"].split("T")[1][0:5],
    # )
    # return flight_data
def save_to_json(json_data: dict, target_dir: str, file_name: str):
    """
    Saves data to JSON file within the /data/raw/ directory.
    :param json_data: Data to be saved.
    :param target_dir: Directory where data should be saved.
    :param file_name: Name of the file to be saved.
    """
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file = os.path.join(target_dir, f"{current_timestamp}-{file_name}.json")
    with open(file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    params = {
        "fly_from": "WAW",
        "date_from": ut.get_future_date(),
        "date_to": ut.get_future_date(num_months=6),
        "return_from": ut.get_future_date(3),
        "return_to": ut.get_future_date(num_days=3, num_months=6),
        "max_stopovers": 1,
        "curr": "PLN",
    }

    data = get_flight_data(params)
    save_to_json(data, r"C:\Users\kubag\PycharmProjects\flight_price\data\raw", "flight_details")
