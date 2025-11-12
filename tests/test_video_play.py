import time
import pytest

from selenium.webdriver.common.by import By
from utils.logger import Logger

from pages.automation_project_tabs import AutomationProjectTabs
from pages.video_action import VideoActions

class ProjectTabHelper(AutomationProjectTabs):
    __test__=False

log=Logger().get_logger(__name__)
class TestVideoPlay():
    """
        Class Created for performing the action on the video  
    """
    @pytest.mark.order(3)
    def test_video_play(self,driver):
        video_actions=VideoActions(driver)
        time.sleep(15)
        driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
        
        video_actions.click_pause_button()
        time.sleep(2)
        video_actions.click_play_button()

        video_actions.sound_adjustments()

        video_actions.click_settings_button()
        video_actions.click_480p_resolution()
        time.sleep(2)
        video_actions.click_settings_button()
        video_actions.click_720p_resolution()

        video_actions.click_pause_button()
        time.sleep(2)

        driver.switch_to.default_content()
        driver.back()
        time.sleep(2)
        ProjectTabHelper(driver).click_sign_out()
        time.sleep(2)
