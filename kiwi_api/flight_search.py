import requests
import os
import json
from datetime import datetime
import kiwi_api.const as ct

parameters_dict = {
    "fly_from": "WAW",
    "date_from": "20/01/2025",
    "date_to": "24/01/2025",
    "one_per_date": 1,
}

def get_flight_data(parameters: dict):
    """
    Retrievies data about flights from Tequila KIWI API.
    :param parameters: Dictionary with parameters.
    :return: JSON file with flight's data.
    """
    try:
        response = requests.get(ct.KIWI_BASE_URL, headers=ct.KIWI_HEADERS, params=parameters)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"{e}")

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
    data = get_flight_data(parameters_dict)
    save_to_json(data, "flight_details")
