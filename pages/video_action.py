import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from utils.baseMethods import BaseMethods
from utils.logger import Logger

log=Logger().get_logger()

class VideoActions(BaseMethods):
    """
        Class Created for the elements Present in the video page to perform Action that needs to be done
    """
    __private_div_jw_player=(By.XPATH, "//div[@class='jw-reset jw-old-rail']")
    __private_button_play=(By.CSS_SELECTOR, "div[class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']")
    __private_button_sound=(By.CSS_SELECTOR, "div[role='group']")
    __private_sound_knob=(By.XPATH, "(//div[@class='jw-knob jw-reset'])[2]")
    __private_button_setting=(By.CSS_SELECTOR, "svg[class='jw-svg-icon jw-svg-icon-settings']")
    __private_button_480p=(By.CSS_SELECTOR, "button[aria-label='480p']")
    __private_button_720p=(By.CSS_SELECTOR, "button[aria-label='720p']")

    def click_play_button(self):
        """
            Method created for to click on play button  to play video.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_play)).click().perform()

    def click_pause_button(self):
        """
            Method created for to click on play button  to play video.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_play)).click().perform()

    def sound_adjustments(self):
        """
            Method created for to hover on sound button to see the silder and
            then move it so to make souf 50%
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_sound)).perform()
        time.sleep(2)
        actions.move_to_element(self.find_element_wait(self.__private_sound_knob)).click_and_hold().move_by_offset(50,0).release().perform()

    def click_settings_button(self):
        """
            Method created for to click on settings button to open the resulations panel.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_setting)).click().perform()

    def click_480p_resolution(self):
        """
            Method created for to click on 480 resulation.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_480p)).click().perform()

    def click_720p_resolution(self):
        """
            Method created for to click on 720 resulation.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_720p)).click().perform()