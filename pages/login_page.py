from utils.loggers import get_logger
logger = get_logger(__name__)


class LoginPage:
    def __init__(self, page):
        self.page = page

        #initializing the locators
        self.username = "input[name='username']"
        self.password = "input[name='password']"
        self.login_button = "input[value='Log In']"
        self.logout_button = "text=Log Out"
    

    def login(self, username, password):
        logger.info("Waiting for login")
        self.page.wait_for_selector(self.username)
        logger.info("Entering username")
        self.page.fill(self.username, username)
        logger.info("Entering password")
        self.page.fill(self.password, password)
        logger.info("Clicking login button")
        self.page.click(self.login_button)


    def logout(self):
        logger.info("Clicking on logout button")
        self.page.click(self.logout_button)
        # wait for login page to enter credentials again
        logger.info("Waiting for login again with registered credentials.")
        self.page.wait_for_selector(self.username)

