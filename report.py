from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# service = ChromeService(executable_path="chromedriver")
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://safebrowsing.google.com/safebrowsing/report_phish/?hl=en")
print("Site opened")

########Change this to phish link ################
phishlink = "https://osrecovery.org/"
#captcha = driver.find_element(by=By.CLASS_NAME, value="recaptcha-checkbox")
#captcha = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-spinner")))

WebDriverWait(driver, 20).until(ec.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
print("Captcha Iframe Available")
WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
print("Captcha clicked")
driver.switch_to.default_content()

print("Switched to default content")

driver.implicitly_wait(6)
driver.find_element(by=By.ID, value="url").send_keys(phishlink)
print("Link Inserted")
#captcha.click()
driver.implicitly_wait(6)
print("waited.......")
submitxpath = "//input[@type='submit']"
submitbutton = driver.find_element(by=By.XPATH, value = submitxpath)
submitbutton.click()
print("Submiteeeeeeeeeed")




driver.quit()