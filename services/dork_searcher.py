from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")

DRIVERS = {
    "chrome": {
        "driver": webdriver.Chrome,
        "service": ChromeService,
        "driver_manager": ChromeDriverManager,
        "options": chrome_options
    },
    "firefox": {
        "driver": webdriver.Firefox,
        "service": FirefoxService,
        "driver_manager": GeckoDriverManager,
        "options": firefox_options
    },
}

class DorkSearcher:

    def __init__(self):
        self.driver = None
        for _, browser_data in DRIVERS.items():
            try:
                self.driver = browser_data["driver"](
                    service=browser_data["service"](browser_data["driver_manager"]().install()),
                    options=browser_data["options"]
                )
                break
            except:
                pass


    def search(self, dork, pages):
        page = 1
        all_results = []
        while page <= pages:
            start = ((page - 1) * 10) + 1
            url = f"https://www.google.com/search?q={dork}&start={start}"
            self.driver.get(url)
            results = self.get_results()
            all_results = all_results + results
            if len(results) == 0 or page == pages:
                break
            page += 1

        return all_results

    def get_results(self):
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
                    "snippet": snippet[:100] + "..."
                })
            except:
                pass
        return formatted_results

    def quit(self):
        self.driver.quit()

