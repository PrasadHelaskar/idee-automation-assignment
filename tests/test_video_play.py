import time
import pytest

from selenium.webdriver.common.by import By
from utils.logger import Logger

from pages.automation_project_tabs import AutomationProjectTabs
from pages.video_action import VideoActions

class ProjectTabHelper(AutomationProjectTabs):
    """
        create the helper function to access the logout method from AutomationProjectTabs POM file

        __test__= False used to pytest should not treat as seperate test and trigger it again     
    """
    __test__= False

log=Logger().get_logger(__name__)
class TestVideoPlay():
    """
        Class Created for performing the action on the video
    """
    @pytest.mark.order(3)
    def test_video_play(self,driver):
        """
            Method Responsible for the Video actions and signput actions
        """
        video_actions=VideoActions(driver)
        time.sleep(15) # Sleep given for making video play and move to 10 sec

        driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0]) # moving the curser to frame 0 to access the jw player

        video_actions.click_pause_button() # Clicking the Pause Button
        time.sleep(2)  # time sleep to have visuals ofthe actions doen on view port
        video_actions.click_play_button() # Clicking the Play Button to continue Playing

        video_actions.sound_adjustments() # Method Dealing wiht sounding adjestments

        video_actions.click_settings_button() # Clicking the setting icon to alter the resolutions
        video_actions.click_480p_resolution() # Altering the resolutions to 480p
        time.sleep(2)  # time sleep to have visuals ofthe actions doen on view port

        video_actions.click_settings_button() # Clicking the setting icon to alter the resolutions
        video_actions.click_720p_resolution() # Altering the resolutions to 720p
        time.sleep(2)  # time sleep to have visuals ofthe actions doen on view port

        video_actions.click_pause_button() # Clicking the Pause Button
        time.sleep(2)  # time sleep to have visuals ofthe actions doen on view port

        driver.switch_to.default_content() # returing to the default frame from the JW player frame
        driver.back() # unable to Locate the back button in JW player so using rhe selenium methodes to go back
        time.sleep(2) # time sleep to have visuals ofthe actions doen on view port

        ProjectTabHelper(driver).click_sign_out() # clicking the signout for the last part of the automation
        time.sleep(2)  # time sleep to have visuals ofthe actions doen on view port
