from pytest_bdd import given, when, then, scenario
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import USER_INFO
from utils.data_generator import generate_user
from utils.loggers import get_logger
logger = get_logger(__name__)


@scenario("../features/parabank_login.feature",
          "User creates a new account and logs in successfully")
def test_parabank_flow():
    pass

@given("the user navigates to the Parabank login page")
def open_login_page(page, base_url):
    logger.info(f"Going to link: {base_url}")
    page.goto(base_url)
    logger.info("Waiting for page to get load")
    page.wait_for_load_state("networkidle")


@when("the user registers a new account using dynamically generated credentials")
def register_user(page):
    logger.info("Generating unique user")
    user = generate_user()
    # store for later login steps
    logger.info(f"Unique user generated: {user['username']}")
    page.user_data = {
        "username": user["username"],
        "password": user["password"]
    }
    signup_page = SignupPage(page)
    signup_page.fill_registration_form(USER_INFO, user['username'], user['password'])
    signup_page.validate_registration(user['username'])


@when("the user logs in using the generated username and password")
def login_user(page):
    login_page = LoginPage(page)
    # Performing logout after registration
    login_page.logout()
    # Performing login with registered user
    login_page.login(page.user_data["username"], page.user_data["password"])


@then("the user should see the account balance on the dashboard")
def verify_balance(page):
    dashboard = DashboardPage(page)
    balance = dashboard.get_account_balance()
    assert balance, f"Account balance not found on dashboard"
    logger.info(f"Account Balance: {balance}.")

