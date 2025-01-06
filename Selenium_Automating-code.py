from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-data-dir=/path/to/your/chrome/user/data")
driver = webdriver.Chrome(options=options)
driver2 = webdriver.Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    """
})
driver.get("https://mail.google.com/")
time.sleep(5)
print("Please try manual login as Google restricts automation.")
time.sleep(5)
emails = driver.find_elements(By.XPATH, '//tr[@class="zA zE" or @class="zA yO"]')
for email in emails:
    sender = email.find_element(By.CLASS_NAME, 'yX').text 
    subject = email.find_element(By.CLASS_NAME, 'bog').text
    preview = email.find_element(By.CLASS_NAME, 'y2').text.strip(' - ')
    print(f"Sender: {sender}")
    print(f"Subject: {subject}")
    print(f"Preview: {preview}")
    driver2.get('http://127.0.0.1:5000/')
    time.sleep(2)
    textarea = driver2.find_element(By.NAME, 'message')
    email_content = f"{preview}"
    textarea.clear()
    textarea.send_keys(email_content)
    submit_button = driver2.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()
    time.sleep(3) 
driver.quit()
