#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tqdm import tqdm
import datetime




# Specify the website to visit
website = 'https://www.reddit.com/user/Kolya19'

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get(website)

# Wait for the "load more" button to become clickable
button_xpath = '//a[@class="_1JNzvBgvzSnX27gUBKqqmJ "][1]'
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
button.click()
time.sleep(4)

# Scroll down to the end of the page
while True:
    # Get current height of the page
    prev_height = driver.execute_script("return document.body.scrollHeight")
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for the page to load
    time.sleep(2)
    # Calculate new height of the page
    new_height = driver.execute_script("return document.body.scrollHeight")
    # Check if the page has reached the end
    if new_height == prev_height:
        break

# Extract the links from the page
Dls_Links = driver.find_elements("xpath", '//a[@data-click-id="body"]')
list_of_links = []
for dls_link in Dls_Links:
    list_of_links.append(dls_link.get_attribute('href'))
    
alldetails = []
for i in tqdm(range(len(list_of_links))):
    driver.get(list_of_links[i])
    time.sleep(2)
    
    # Extract the post title
    try:
        Title = driver.find_elements("xpath", '//h1[@slot="title"]')[0].text
    except:
        Title = driver.find_elements("xpath", '//div[@class="_2SdHzo12ISmrC8H86TgSCp _29WrubtjAcKqzJSPdQqQ4h "]/h1')[0].text
    # Extract the context
    try:
        Date = driver.find_elements("xpath", '//div[@class="bottom-row text-12 leading-normal flex"]/faceplate-timeago')[0].text
    except:
        Date = driver.find_elements("xpath", '//span[@class="_2VF2J19pUIMSLJFky-7PEI"]')[0].text
    
    try:
        Community_Group = driver.find_elements("xpath", '//div[@class="top-row font-semibold"]/span/faceplate-tracker/faceplate-hovercard/a')[0].get_attribute('innerText')
    except:
        Community_Group = driver.find_elements("xpath", '//span[@class="_19bCWnxeTjqzBElWZfIlJb"]')[0].get_attribute('innerText')
    #Vote=driver.find_elements("xpath", '//*[@id="vote-arrows-t3_7tevrj"]/div')[0].get_attribute('innerText')

    # Extract the full detail link
    Full_Detail = driver.current_url

    tempj = {'Post Title': Title, 'Date_Post Age': Date, 'Group/Community': Community_Group, 'Full Detail': Full_Detail}  # add the 'Full Detail' key to the dictionary
    alldetails.append(tempj)

Post_Data = pd.DataFrame(alldetails)
driver.quit()
# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get(website)

# Wait for the "load more" button to become clickable
button_xpath = '//a[@class="_1JNzvBgvzSnX27gUBKqqmJ "][2]'
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
button.click()
time.sleep(4)

# Scroll down to the end of the page
while True:
    # Get current height of the page
    prev_height = driver.execute_script("return document.body.scrollHeight")
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for the page to load
    time.sleep(2)
    # Calculate new height of the page
    new_height = driver.execute_script("return document.body.scrollHeight")
    # Check if the page has reached the end
    if new_height == prev_height:
        break

# Extract the links, dates, and comments from the page
Dls2_Links = driver.find_elements("xpath", '//a[@class="_1sA-1jNHouHDpgCp1fCQ_F"]')
list2_of_links = []
for dls_link in Dls2_Links:
    list2_of_links.append(dls_link.get_attribute('href'))

Comments = driver.find_elements("xpath", '//div[@class="_3CecFEZvC8MFSvLsfuVYUs"]')
commento=[]
for Comment in Comments:
    commento.append(Comment.get_attribute('innerText'))
    
Dates = driver.find_elements("xpath", '//a[@class="_1sA-1jNHouHDpgCp1fCQ_F"]')
Datez=[]
for Date in Dates:
    Datez.append(Date.get_attribute('innerText'))    


# Create a Pandas dataframe
Comment_Data = pd.DataFrame({'Comments': commento, 'Date_Comment Age': Datez, 'Full Detail': list2_of_links})

driver.quit()

# Get current date and time
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M")

# Save data to Excel with current date and time in the filename
Post_Data.to_excel(f"Post Data {date_time}.xlsx", index=False)
Comment_Data.to_excel(f"Comment Data {date_time}.xlsx", index=False)


# In[ ]:




