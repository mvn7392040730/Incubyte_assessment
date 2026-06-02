from utils.loggers import get_logger
logger = get_logger(__name__)


class SignupPage:
    def __init__(self, page):
        self.page = page

        #initializing the locators
        self.register_link = "text=Register"
        self.first_name = "input[name='customer.firstName']"
        self.last_name = "input[name='customer.lastName']"
        self.address = "input[name='customer.address.street']"
        self.city = "input[name='customer.address.city']"
        self.state = "input[name='customer.address.state']"
        self.zip_code = "input[name='customer.address.zipCode']"
        self.phone = "input[name='customer.phoneNumber']"
        self.ssn = "input[name='customer.ssn']"
        self.username = "input[name='customer.username']"
        self.password = "input[name='customer.password']"
        self.confirm_password = "input[name='repeatedPassword']"
        self.register_button = "input[value='Register']"
        self.welcome_locator = "#rightPanel h1.title"
    

    def open_registration_form(self):
        logger.info("Clicking Register button.")
        self.page.click(self.register_link)
    

    def fill_registration_form(self, user_info, username, password):
        self.open_registration_form()
        self.page.wait_for_selector(self.first_name)
        self.page.screenshot(path="screenshots/registration_form.png", full_page=True)
        logger.info("Form is visible. Entering user details.")
        logger.info("Entering First Name")
        self.page.fill(self.first_name, user_info["first_name"])
        logger.info("Entering Last Name")
        self.page.fill(self.last_name, user_info["last_name"])
        logger.info("Entering Address")
        self.page.fill(self.address, user_info["address"])
        logger.info("Entering City")
        self.page.fill(self.city, user_info["city"])
        logger.info("Entering State")
        self.page.fill(self.state, user_info["state"])
        logger.info("Entering Zip Code")
        self.page.fill(self.zip_code, user_info["zipcode"])
        logger.info("Entering Phone number")
        self.page.fill(self.phone, user_info["phone"])
        logger.info("Entering SSN")
        self.page.fill(self.ssn, user_info["ssn"])
        logger.info("Entering Generated Username")
        self.page.fill(self.username, username)
        logger.info("Entering Generated Password")
        self.page.fill(self.password, password)
        logger.info("Confirming Password")
        self.page.fill(self.confirm_password, password)
        self.page.screenshot(path="screenshots/form_filled.png", full_page=True)
        logger.info("Clicking on register button to create the user.")
        self.page.click(self.register_button)


    def validate_registration(self, username):
        logger.info("Waiting for Registration")
        self.welcome_locator = self.page.locator(self.welcome_locator)
        self.welcome_locator.wait_for(state="visible")
        welcome_text = self.welcome_locator.inner_text()
        self.page.screenshot(path="screenshots/welcome_user.png", full_page=True)
        assert username in welcome_text, f"Username {username} not shown in welcome message: {welcome_text}"
        logger.info(f"Registration Successful. {welcome_text}")
