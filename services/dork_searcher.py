from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

DRIVERS = {
    "chrome": {
        "driver": webdriver.Chrome,
        "service": ChromeService,
        "driver_manager": ChromeDriverManager,
    },
    "firefox": {
        "driver": webdriver.Firefox,
        "service": FirefoxService,
        "driver_manager": GeckoDriverManager,
    },
}

class DorkSearcher:

    def __init__(self):
        self.driver = None
        for browser, browser_data in DRIVERS.items():
            try:
                self.driver = browser_data["driver"](service=browser_data["service"](browser_data["driver_manager"]().install()))
                break
            except:
                pass

    def search(self, dork):
        url = f"https://www.google.com/search?q={dork}"
        self.driver.get(url)
        results = self.driver.find_elements(by=By.CLASS_NAME, value='MjjYud')
        formatted_results = []
        for result in results:
            try:
                title = result.find_element(by=By.TAG_NAME, value='h3').text
                link = result.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
                snippet = result.find_element(by=By.CLASS_NAME, value='VwiC3b').text
                formatted_results.append({
                    "title": title,
                    "link": link,
                    "snippet": snippet[:50]
                })
            except:
                pass
        return formatted_results
    
    def quit(self):
        self.driver.quit()

