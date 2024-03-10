from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time

# LOADING SELENIUM
print("Loading...")
options = uc.ChromeOptions()
options.add_argument("--enable-javascript")
# !!! SET YOUR CHROME PROFILE PATH !!!
chrome_profile_path = "CHROME_PROFILE_PATH"
options.add_argument(f"user-data-dir={chrome_profile_path}")
# !!! SET YOUR CHROMEDRIVER PATH !!!
driver = uc.Chrome(options=options, executable_path=r'CHROMEDRIVER_PATH')
driver.implicitly_wait(30)

# GET TO THE SITE AND CLICK THE CHARACTER
driver.get("https://beta.character.ai/")
# !!! ENTER YOUR CHARACTER BUTTON XPATH HERE !!!
char = driver.find_element(By.XPATH, 'CHARACTER_BUTTON_XPATH')
char.click()
time.sleep(5)

# TALK WITH THE CHARACTER
while True:
    your_message = input("Message: ")
    # If the message sent is exit, quit the program
    if your_message == "exit":
        break

    input_box = driver.find_element(By.ID, "user-input")
    input_box.send_keys(your_message)
    time.sleep(2)
    input_box.send_keys(Keys.ENTER)
    # Waiting for answer
    time.sleep(25)

    time.sleep(2)

    # Clean the message and print (do whatever you want with the message)
    messages = driver.find_elements(By.CLASS_NAME, "swiper-no-swiping")
    messages = messages[-1].text
    messages = messages.replace('☆', '')
    messages = messages.strip()
    print(f"Answer: {messages}")

driver.quit()
