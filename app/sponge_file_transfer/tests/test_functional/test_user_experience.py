from django.test import override_settings, tag, TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        # title = self.chrome.find_element_by_tag_name('title').text
        # body = self.chrome.find_element_by_tag_name('body').text
        # print('TITLE2', self.chrome.title, title, self.chrome.current_url)
        # print('BODY', body)
        # self.driver.find_element_by_id('id_title').send_keys("test title")
        # self.driver.find_element_by_id('id_body').send_keys("test body")
        # self.driver.find_element_by_id('submit').click()
        # self.assertIn("http://localhost:8000/", self.driver.current_url)
        self.assertEqual('Home | WeTransferClone', self.chrome.title)
        
    @tag('selenium')
    def test_home_page_can_upload_file(self):
        self.chrome.get('http://web:8000')
        submit_button = self.chrome.find_element(By.TAG_NAME, "button")
        self.assertEqual('Share Files', submit_button.text)
        self.chrome.find_element_by_id('id_files').send_keys('/usr/src/app/sponge_file_transfer/static/img/test-image.jpg')
        self.chrome.find_element_by_id('id_email').send_keys('r.o.gibbs94@gmail.com')
        submit_button.click()
        WebDriverWait(self.chrome, 15).until(EC.visibility_of_element_located((By.TAG_NAME, 'h2')))
        success_msg = self.chrome.find_element(By.TAG_NAME, 'h2').text
        self.assertIn('Download started', success_msg)


    # @tag('selenium')
    # def test_transfer_page(self):
    #     self.chrome.get('http://web:8000/transfers/')
    #     download_button = self.chrome.find_element(By.TAG_NAME, "button")
    #     self.assertEqual('Download', download_button.text)
    #     download_button.click()
    #     WebDriverWait(self.chrome, 15).until(EC.visibility_of_element_located('.success-msg'))
    #     success_msg = self.chrome.find_element(By.CLASS_NAME, 'success-msg')
    #     self.assertIn('Successfully', success_msg)

        