import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
# Create USER_INFO dict directly from environment variables
USER_INFO = {
    "first_name": os.getenv("FIRST_NAME"),
    "last_name": os.getenv("LAST_NAME"),
    "address": os.getenv("ADDRESS"),
    "city": os.getenv("CITY"),
    "state": os.getenv("STATE"),
    "zipcode": os.getenv("ZIPCODE"),
    "phone": os.getenv("PHONE"),
    "ssn": os.getenv("SSN")
}
