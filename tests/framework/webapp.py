from selenium import webdriver
from data.config import settings
# compatible with py 2 and 3
try: 
    from urllib.parse import urljoin
except:
    from urlparse import urljoin


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/billyquick/Downloads/chromedriver')

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def login(self):
        username = "qa_user_01"
        password = "HcaR3$!v3%8J"
        inputUsername = self.driver.find_element_by_xpath('//*[@id="username"]')
        inputUsername.send_keys(username)
        inputPass = self.driver.find_element_by_xpath('//*[@id="password"]')
        inputPass.send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[6]/div/div/input').click()

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def verify_component_exists(self, component):
        # Simple implementation
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)


webapp = WebApp.get_instance()
