from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
config = dotenv_values(".env")
chrome_driver_path = config.get('OWM_API_KEY')


class MenuItem:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def interact(self, option):
        if option == 1:
            self.driver.get("https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815")
            price = self.driver.find_element_by_id("price")
            new_price = price.text.partition('\n')[0]
            print(new_price)

        elif option == 2:
            self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
            article_count = self.driver.find_element_by_css_selector("#articlecount a")
            print(article_count.text)  # all_portals.click()
            all_portals = self.driver.find_element_by_link_text("All portals")
            all_portals.click()

        elif option == 3:
            self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
            search = self.driver.find_element_by_id("searchInput")
            search.send_keys("Python")
            search.send_keys(Keys.ENTER)

        elif option == 4:
            self.driver.get("https://www.python.org/")
            event_times = self.driver.find_elements_by_css_selector(".event-widget time")
            event_names = self.driver.find_elements_by_css_selector(".event-widget li a")
            events = {}

            for n in range(len(event_times)):
                events[n] = {
                    "time": event_times[n].text,
                    "name": event_names[n].text
                }
            print(events)

        else:
            self.driver.get("http://secure-retreat-92358.herokuapp.com/")
            first_name = self.driver.find_element_by_name("fName")
            first_name.send_keys("Juan")
            last_name = self.driver.find_element_by_name("lName")
            last_name.send_keys("Perez")
            email = self.driver.find_element_by_name("email")
            email.send_keys("youremail@gmail.com")
            sign_up = self.driver.find_element_by_css_selector("form button")
            sign_up.click()
