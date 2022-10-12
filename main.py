from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

user_name = "your username"
pw = "your password"

chrome_driver_path = "/Users/mohan/Development/chromedriver"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3303250508&f_AL=true&f_E=2&keywords=python%20developer"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(URL)

time.sleep(5)
sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/a[1]')
sign_in.click()

# sign in to your LinkedIn account
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(user_name)

pw_field = driver.find_element(By.ID, "password")
pw_field.send_keys(pw)

login_button = driver.find_element(By.CLASS_NAME, "login__form_action_container ")
login_button.click()

# find all job elements from left hand column
driver.maximize_window()
job_elements = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

# create list from elements
all_jobs = [job.text for job in job_elements]
print(all_jobs)
# click individual job element then click apply now
x = range(len(all_jobs))
for n in x:
    try:
        job_elements[n].click()

        time.sleep(5)
        apply_now = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_now.click()
        # check for Submit application button vs Next (stores button text as button_text)
        button = driver.find_element(By.CSS_SELECTOR, "form button span")
        button_text = button.text
        print(button_text)

        # if Next, close window and click discard button, then continue loop
        # if Submit application, click button, break loop
        if button_text == "Next":
            dismiss = driver.find_element(By.XPATH, '//*[@aria-label="Dismiss"]')
            dismiss.click()
            discard = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard.click()
        else:
            submit = driver.find_element(By.XPATH, '//*[@aria-label="Submit application"]')
            submit.click()
            time.sleep(5)
            close_popup = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal--layer-default button")
            close_popup.click()
            break
    except NoSuchElementException as e:
        print(f"Error: {e}")
        continue