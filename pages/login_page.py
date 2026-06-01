class LoginPage:
    def __init__(self, page):
        self.page = page

        #initializing the locators
        self.username = "input[name='username']"
        self.password = "input[name='password']"
        self.login_button = "input[value='Log In']"
    

    def login(self, username, password):
        self.page.wait_for_selector(self.username)
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)