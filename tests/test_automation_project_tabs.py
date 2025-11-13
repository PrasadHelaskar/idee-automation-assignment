import time
import pytest

from utils.logger import Logger

from pages.automation_project_tabs import AutomationProjectTabs

log=Logger().get_logger(__name__)
class TestNavigateProjectTabs():
    """
        Class Created to perform tha tab related actions in the automation project
    """
    @pytest.mark.order(3)
    def test_navigate_project_tabs(self,driver):
        """
            Method responsible to handling the automtions related to tabs 
        """
        brand_page_nevigations=AutomationProjectTabs(driver)

        brand_page_nevigations.click_all_title_logo() # clicking the all title logo
        brand_page_nevigations.click_test_automation_project() # clicking the test automation project
        time.sleep(2)  # time sleep to see the default landing section 
        brand_page_nevigations.click_details_section() # click the details tab to visit the details section
        time.sleep(10) # time sleep to keep the video section on the view port
        brand_page_nevigations.click_video_section() # click the details tab to visit the video section

        brand_page_nevigations.click_video_play() # click the play button to play the video