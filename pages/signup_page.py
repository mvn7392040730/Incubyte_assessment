import time
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
        self.page.click(self.register_link)
    

    def fill_registration_form(self, user_info, username, password):
        self.open_registration_form()
        self.page.wait_for_selector(self.first_name)
        self.page.fill(self.first_name, user_info["first_name"])
        self.page.fill(self.last_name, user_info["last_name"])
        self.page.fill(self.address, user_info["address"])
        self.page.fill(self.city, user_info["city"])
        self.page.fill(self.state, user_info["state"])
        self.page.fill(self.zip_code, user_info["zipcode"])
        self.page.fill(self.phone, user_info["phone"])
        self.page.fill(self.ssn, user_info["ssn"])
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.fill(self.confirm_password, password)
        self.page.click(self.register_button)


    def validate_registration(self, username):
        self.welcome_locator = self.page.locator(self.welcome_locator)
        self.welcome_locator.wait_for(state="visible")
        welcome_text = self.welcome_locator.inner_text()
        print("Welcome text:", welcome_text)
        assert username in welcome_text, f"Username {username} not shown in welcome message: {welcome_text}"

