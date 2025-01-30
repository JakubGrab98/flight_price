import os
from dotenv import load_dotenv

load_dotenv()

KIWI_BASE_URL="https://api.tequila.kiwi.com/v2/search?"

KIWI_HEADERS = {
    "apikey": os.getenv("KIWI_API_KEY"),
}