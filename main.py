#you tube comments on  you tube orignal Ai series.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)
search=driver.find_element(By.NAME,"search_query")
search.clear()
# type name of video or any keyword this will only find the first video of your search
search.send_keys("Launch of LVM3-M4/CHANDRAYAAN-3 Mission from Satish Dhawan Space Centre (SDSC) SHAR, Sriharikota")

search.send_keys(Keys.ENTER)
sleep(5)
link=driver.find_element(By.XPATH,"""//*[@id="video-title"]/yt-formatted-string""")
link.click()
sleep(10)
for i in range(20):
    driver.execute_script("window.scrollBy(0,700)","")
    sleep(2)
sleep(10)

# Extract usernames and comments
comments = driver.find_elements(By.XPATH, """//*[@id="content-text"]""")
usernames = driver.find_elements(By.XPATH, """//*[@id="author-text"]/span""")

# Create a list to store usernames and comments
data = []

# Iterate over both lists and combine them
for user, comment in zip(usernames, comments):
    data.append({"username": user.text.strip(), "comment": comment.text.strip()})

# Print the data
for entry in data:
    print(entry)

# Save to a CSV
import pandas as pd
df = pd.DataFrame(data)
df.to_csv("youtube_comments_with_usernames.csv", index=False)
assert "No results found." not in driver.page_source
driver.close()