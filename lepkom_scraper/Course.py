import re
from dotenv import load_dotenv
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from .Browser import Browser

# Dot Env
load_dotenv()
dotenv = dotenv_values()
USERNAME = dotenv.get('USERNAME')
PASSWORD = dotenv.get('PASSWORD')

# Web Driver
CHROMEDRIVER_PATH = './chromedriver'
WINDOW_SIZE = '1920,1080'

driver_options = Options()
# driver_options.add_argument('--headless')
driver_options.add_argument(f"--window-size={WINDOW_SIZE}")

browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                           options=driver_options)

url = "https://kursusvmlepkom.gunadarma.ac.id/login/index.php"
browser.get(url)


def user_input(courses):
    """Generate list of courses that user can choose."""
    for idx, course in enumerate(courses.keys(), 1):
        print(f'{idx}. {course}')
    while True:
        try:
            welement = input("Silahkan pilih kursus yang diinginkan: ")
            if welement.isdigit() and int(welement) <= len(courses.keys()):
                welement = int(welement) - 1
                welement = list(courses.keys())[int(welement)]
                welement = courses.get(welement)
                welement.send_keys(Keys.ENTER)
                return welement
            else:
                assert int(welement) < len(courses.keys()), "Silahkan masukkan angka yang benar."
        except:
            print("Silahkan masukkan angka yang benar.")


class Course:
    def __init__(self, driver) -> None:
        self.driver = Browser(driver)

    def __name__(self):
        return f"{self.driver.title}: {self.driver.current_url}"

    def get_course_list(browser):
        """Get list of all courses."""
        courses = browser.find_elements(By.CLASS_NAME, "coursebox")
        course_names = {
            course.find_element_by_tag_name("a").text:
            course.find_element_by_tag_name("a")
            for course in courses
            if not course.find_element_by_tag_name("a").text.startswith("ACTIVITY")
        }
        return course_names
