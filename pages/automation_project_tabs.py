from selenium.webdriver.common.by import By

from utils.baseMethods import BaseMethods
from utils.logger import Logger

log=Logger().get_logger(__name__)

class AutomationProjectTabs(BaseMethods):
    """
        Class Created for the elements Present in the brand page and home page to perform Action that needs to be done
    """
    __private_all_titles_logo=(By.ID, "brd-01fvc8gs4sa9kjs8wxs6gnsn76")
    __private_test_automation_project=(By.CSS_SELECTOR, "img[alt='Test automation project']")
    __private_details_section=(By.ID, "detailsSection")
    __private_video_section=(By.CSS_SELECTOR, "a[id='videosSection']")
    __private_button_video_play=(By.CSS_SELECTOR, "button[class='icon-width-gen wds-cursor-pointer']")
    __private_button_sign_out=(By.ID, "signOutSideBar")

    def click_all_title_logo(self):
        """
            Method created for to click on all titles button to contiune on next page.
        """
        self.click(self.__private_all_titles_logo)
        log.info("Clicked the all title tab")

    def click_test_automation_project(self):
        """
            Method created for to click on test automation project tile to contiune on next page.
        """
        self.click(self.__private_test_automation_project)
        log.info("Clicked the test automation project tab")

    def click_details_section(self):
        """
            Method created for to click on details scetion to contiune on next page.
        """
        self.click(self.__private_details_section)
        log.info("Clicked the details tab")

    def click_video_section(self):
        """
            Method created for to click on video scetion to contiune on next page.
        """
        self.click(self.__private_video_section)
        log.info("Clicked the video tab")

    def click_video_play(self):
        """
            Method created for to click on video play button.
        """
        self.click(self.__private_button_video_play)
        log.info("Clicked the video play button")


    def click_sign_out(self):
        """
            Method created for to click on sign out button to contiune sign-out.
        """
        self.click(self.__private_button_sign_out)
        log.info("Clicked the sign-out button")
