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
        Class to execute the Login funcationality with the data actual data
    """
    @pytest.mark.order(1)
    def test_login(self,driver):
        """
            Function to test the login with the given PIN
            URL: Fatched from Json file
            PIN: Fatched from env file
        """
        load_dotenv("config/.env")
        # Loading the URL from the Json file
        driver.get(jsonRead("URL"))

        # Initializing the POM class LoginPage
        login=LoginPage(driver)

        login.type_text_box_pin(os.getenv("PIN")) # Entering the PIN in text box fetched from .env file
        time.sleep(5) # Forced sleep reason: To show the action done by the script
        login.click_sign_in()  # Clicking the sign-in button
        login.click_accept_cookies() # accepting the cookies prevent it reciving click 