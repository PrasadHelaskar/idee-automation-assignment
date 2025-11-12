import sys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from utils.baseMethods import baseMethods
from utils.logger import Logger

log=Logger().get_logger(__name__)

class LoginPage(baseMethods):
    """
        Class Created for the elements Present in the login page and Action that needs to be done
    """
    __private_text_box_pin=(By.ID, "pin")
    __private_button_sign_in=(By.ID, "sign-in-button")

    def type_text_box_pin(self, pin):
        """
            Method created for to Send the PIN in the designated text box

            Parameters:
                text (string) : Text to input the Pin in the located element
        """
        try:
            self.send_keys(self.__private_text_box_pin, pin)
        except NoSuchElementException as e:
            log.error("Failed to locate the element in the view port")
            log.info(e)
            sys.exit()

    def click_sign_in(self):
        """
            Method created for to click on sign-in button to start the sign-in backend validation.
        """
        try:
            self.click(self.__private_button_sign_in)
        except NoSuchElementException as e:
            log.error("Failed to locate the element in the view port")
            log.info(e)
            sys.exit()