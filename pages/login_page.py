from selenium.webdriver.common.by import By
from utils.baseMethods import BaseMethods
from utils.logger import Logger

log=Logger().get_logger(__name__)

class LoginPage(BaseMethods):
    """
        Class Created for the elements Present in the login page and Action that needs to be done
    """
    __private_text_box_pin=(By.ID, "pin")
    __private_button_sign_in=(By.ID, "sign-in-button")
    __private_button_accept_cookie=(By.XPATH, "(//button[@class='cky-btn cky-btn-accept'])[1]")

    def type_text_box_pin(self, pin):
        """
            Method created for to Send the PIN in the designated text box

            Parameters:
                text (string) : Text to input the Pin in the located element
        """
        self.send_keys(self.__private_text_box_pin, pin)

    def click_sign_in(self):
        """
            Method created for to click on sign-in button to start the sign-in backend validation.
        """
        self.click(self.__private_button_sign_in)

    def click_accept_cookies(self):
        """
            Method created for to click on accept button to remove the cookie consent modal.
        """
        self.click(self.__private_button_accept_cookie)
