import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Input the path to your ChromeDriver executable
chrome_driver_path = r"C:\Users\calgo\Downloads\forscraping\chromedriver-win32\chromedriver.exe"

# Define the base URL
base_url = 'https://www.propertyguru.com.my/property-agents/kuala-lumpur/'

# Define the number of pages you want to scrape (e.g., 1 to 100)
start_page = 1
end_page = 85

# Initialize an empty list to store all href attributes
href_attributes = []

# Loop through the pages
for page_num in range(start_page, end_page + 1):
    # Create a new WebDriver instance for each page
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Construct the URL for the current page
    current_url = f'{base_url}{page_num}'

    # Navigate to the current page
    driver.get(current_url)

    # Find all elements matching the XPath
    agent_elements = driver.find_elements(By.XPATH, '//div[@class="agent-info-name"]/a')

    # Extract href attributes from all matching elements on the current page
    page_href_attributes = [agent_element.get_attribute('href') for agent_element in agent_elements]

    # Extend the list of href attributes with those from the current page
    href_attributes.extend(page_href_attributes)

    # Quit the WebDriver for the current page
    driver.quit()
driver.quit()

# Initialize an empty list to store the scraped data
data = []

# Loop through the first 10 href attributes
for href in href_attributes[:30]:  # Adjust the number 10 to the desired number of links to scrape
    # Create a new WebDriver instance for each link
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Navigate to the agent's page
    driver.get(href)

    try:
        # Scrape the required data
        full_name = driver.find_element(By.XPATH, '//h1[@class="agent-fullname"]').text
        company = driver.find_element(By.XPATH, '//div[@class="agent-agency"]').text
        region = driver.find_element(By.XPATH, '//div[@class="region-item region-highlight"][1]').text
        contact_number = driver.find_element(By.XPATH,
                                             '//span[@class="agent-phone-number  agent-phone-number-original visible-print"]').get_attribute(
            "innerText")

        # Append the scraped data to the list
        data.append([full_name, company, region, contact_number])

    except Exception as e:
        print(f"Error scraping data from {href}: {str(e)}")
        # If there's an error, append a placeholder (e.g., "N/A") to the data
        data.append(['N/A', 'N/A', 'N/A', 'N/A'])

    # Quit the WebDriver for the current link
    driver.quit()

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=['Full_Name', 'Company', 'Region', 'Contact_Number'])

# Save the data to an Excel file
df.to_excel('Overalll_property_agents_data.xlsx', index=False)

driver.quit()