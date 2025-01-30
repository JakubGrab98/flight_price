"""Module providing small useful functions used in the application"""
import os
import json
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

DATE_FORMAT = '%d/%m/%Y'

def get_future_date(num_days: int=1, num_months: int=0, num_years: int=0) -> str:
    """Retrieves future data from current local date
    Args:
        num_days (int): number of days to be added to current date
        num_months (int): number of months to be added to current date
        num_years (int): number of years to be added to current date

    Returns:
        str: current date plus number of months from month_quantity
    """
    current_date = date.today()
    future_date = current_date + relativedelta(
        days=+num_days, months=+num_months, years=+num_years
    )

    formatted_date = future_date.strftime(DATE_FORMAT)
    return formatted_date

def load_sql_script(file_path):
    with open(file_path, "r") as file:
        return file.read()

def save_to_json(json_data: list, target_dir: str, file_name: str):
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
