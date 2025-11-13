import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from utils.baseMethods import BaseMethods
from utils.logger import Logger

log=Logger().get_logger(__name__)

class VideoActions(BaseMethods):
    """
        Class Created for the elements Present in the video page to perform Action using the actions chains.
    """
    __private_div_jw_player=(By.XPATH, "//div[@class='jw-reset jw-old-rail']")
    __private_button_play=(By.CSS_SELECTOR, "div[class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']")
    __private_button_sound=(By.CSS_SELECTOR, "div[role='group']")
    __private_slider=(By.XPATH, "(//div[@class='jw-slider-container jw-reset'])[2]")
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
        log.info("Clicked the Play Button")

    def click_pause_button(self):
        """
            Method created for to click on play button  to play video.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_play)).click().perform()
        log.info("Clicked the Pause Button")

    def sound_adjustments(self):
        """
            Method created for to hover on sound button to see the silder and
            then move it so to make souf 50%
        """
        # calculation of the slider to make 50& volume
        slider=self.find_element_wait_presence(self.__private_slider)
        slider_lenght = slider.size['height']
        movement = int(slider_lenght*((100 - 50) / 100.0))
        
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_sound)).perform()
        log.info("Hovering on the sound button")
        time.sleep(2)
        actions.move_to_element(self.find_element_wait(self.__private_sound_knob)).click_and_hold().move_by_offset(0,movement).release().perform()
        log.info("Adjested the sound percentage to 50%")

    def click_settings_button(self):
        """
            Method created for to click on settings button to open the resulations panel.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_setting)).click().perform()
        log.info("Clicked the settings icon to open the resoultions tab")

    def click_480p_resolution(self):
        """
            Method created for to click on 480 resolution.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_480p)).click().perform()
        log.info("Clicked the 480p to make video 480p resolution")

    def click_720p_resolution(self):
        """
            Method created for to click on 720 resolution.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_wait_presence(self.__private_div_jw_player)).perform()
        actions.move_to_element(self.find_element_wait(self.__private_button_720p)).click().perform()
        log.info("Clicked the 720p to make video 7200p resolution")