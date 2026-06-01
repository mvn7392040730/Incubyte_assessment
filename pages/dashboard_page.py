from utils.loggers import get_logger
logger = get_logger(__name__)


class DashboardPage:
    def __init__(self, page):
        self.page = page
        #locator for account balance
        self.balance_locator = "#accountTable tbody tr td:nth-child(2)"

    
    def get_account_balance(self):
        logger.info("Waiting for account balance to appear.")
        self.page.wait_for_selector(self.balance_locator)
        balance = self.page.locator("#accountTable tbody tr td:nth-child(2)").first.inner_text()
        return balance
