from pytest_bdd import given, when, then
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import USER_INFO
from utils.data_generator import generate_user

@given("the user navigates to the Parabank login page")
def open_login_page(page, base_url):
    page.goto(base_url)
    page.wait_for_load_state("networkidle")


@when("the user registers a new account using dynamically generated credentials")
def register_user(page):
    user = generate_user()
    # store for later login steps
    page.user_data = {
        "username": user["username"],
        "password": user["password"]
    }
    signup_page = SignupPage(page)
    signup_page.fill_registration_form(USER_INFO, user['username'], user['password'])


@when("the user logs in using the generated username and password")
def login_user(page):
    login_page = LoginPage(page)
    login_page.login(page.user_data["username"], page.user_data["password"])


@then("the user should see the account balance on the dashboard")
def verify_balance(page):
    dashboard = DashboardPage(page)
    balance = dashboard.get_account_balance()
    print("Account Balance:", balance)
    assert balance, f"Account balance not found on dashboard"

