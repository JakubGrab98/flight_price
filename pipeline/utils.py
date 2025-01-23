"""Module providing small useful functions used in the application"""
from datetime import date
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
