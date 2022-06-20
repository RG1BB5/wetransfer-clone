from django.test import override_settings, tag, TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@override_settings(ALLOWED_HOSTS=['*'])  # Disable ALLOW_HOSTS
class BaseTestCase(TestCase):
    """
    Provides base test class which connects to the Docker
    container running Selenium.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.chrome = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        cls.chrome.implicitly_wait(10)
        cls.firefox = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        cls.firefox.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.chrome.quit()
        cls.firefox.quit()
        super().tearDownClass()


@override_settings(ALLOWED_HOSTS=['*'])  # Disable ALLOW_HOSTS
class TestUserExperience(BaseTestCase):
    
    @tag('selenium')
    def test_home_page(self):
        self.chrome.get('http://web:8000')
        self.assertEqual('The install worked successfully! Congratulations!', self.chrome.title)
        