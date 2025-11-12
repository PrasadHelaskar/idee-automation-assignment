import os
import time
import pytest
from dotenv import load_dotenv

from utils.logger import Logger
from utils.jsonOperation import jsonRead

from pages.login_page import LoginPage

log=Logger().get_logger(__name__)

class TestLogin():
    """
        Method to execute the Login funcationality with the data actual data
    """
    @pytest.mark.order(1)
    def test_login(self,driver):
        """
            Function to test the login with the given PIN
            URL: Fatched from Json file
            PIN: Fatched from env file
        """
        load_dotenv("config/.env")
        driver.get(jsonRead("URL"))
        login=LoginPage(driver)
        login.type_text_box_pin(os.getenv("PIN"))
        time.sleep(5)
        login.click_sign_in()