from selenium import webdriver

from test.project_lib import ProjectMantisHelper
from fixture.session_helper import SessionHelper


class Application():
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognize browser %s' % browser)

        self.session = SessionHelper(self)
        self.base_url = base_url
        self.project = ProjectMantisHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def restore(self):
        wd = self.wd
        wd.quit()
