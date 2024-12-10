from kiwi_api.flight_search import get_flight_data, save_to_json


parameters_dict = {
    "fly_from": "WAW",
    "date_from": "20/01/2025",
    "date_to": "24/01/2025",
    "one_per_date": 1,
}

if __name__ == "__main__":
    data = get_flight_data(parameters_dict)
    save_to_json(data, "data/raw", "flight_details")