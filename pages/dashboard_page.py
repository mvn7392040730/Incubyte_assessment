class DashboardPage:
    def __init__(self, page):
        self.page = page
        #locator for account balance
        self.balance_label = "text=Account Balance"
        self.balance_container = f"{self.balance_label} >> .. >> div"

    
    def get_account_balance(self):
        self.page.wait_for_selector(self.balance_container)
        balance_text = self.page.locator(self.balance_container).inner_text()
        return balance_text
