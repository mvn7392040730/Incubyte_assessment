from utils.loggers import get_logger
logger = get_logger(__name__)
import time

class LoginPage:
    def __init__(self, page):
        self.page = page

        #initializing the locators
        self.username = "input[name='username']"
        self.password = "input[name='password']"
        self.login_button = "input[value='Log In']"
        self.logout_button = "text=Log Out"
    

    def login(self, username, password):
        retries = 3 #retrying login 3 times in case of unstable website
        for attempt in range(1, retries + 1):
            try:
                self.page.screenshot(path="screenshots/login_screen.png", full_page=True)
                logger.info("Waiting for login")
                self.page.wait_for_selector(self.username)
                logger.info("Entering username")
                self.page.fill(self.username, username)
                logger.info("Entering password")
                self.page.fill(self.password, password)
                self.page.screenshot(path="screenshots/credentials_entered.png", full_page=True)
                logger.info("Clicking login button")
                self.page.click(self.login_button)
                self.page.wait_for_selector("text=Accounts Overview", timeout=5000)
                self.page.screenshot(path="screenshots/accounts_overview.png", full_page=True)
                logger.info("Login Successful. Able to see Accounts Overview")
                return
            except TimeoutError:
                logger.info(f"Login attempt {attempt} failed. Retrying...")
                assert attempt != retries, f"Retry limit reached."
                time.sleep(1)  # optional wait before retrying


    def logout(self):
        logger.info("Clicking on logout button")
        self.page.click(self.logout_button)
        # wait for login page to enter credentials again
        logger.info("Waiting for login again with registered credentials.")
        self.page.wait_for_selector(self.username)

