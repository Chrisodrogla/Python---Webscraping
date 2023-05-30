import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

email = "excample@gmail.com"
password = "Password123"

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)

url = "https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&ifkv=Af_xneEy2mxZtJxV0z1vKRl8FgidCyurHfbNZRM7iSsBa8VHk7qa5FPRMsqkRnQn8zo0i3JRRppy8g&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

driver.get(url)

email_input = driver.find_element(By.XPATH, '//input[@class="whsOnd zHQkBf"]')
email_input.send_keys(email)

log_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
log_button.click()

time.sleep(10)

password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys(password)
time.sleep(10)

log1_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
log1_button.click()

time.sleep(20)

search_input = driver.find_element(By.XPATH, '//*[@id="gs_lc50"]/input[1]')
time.sleep(5)
search_input.send_keys('from:(john@venturebnb.io) subject:(Traveler Housing Request) john@venturebnb.io')

search_button = driver.find_element(By.XPATH, '//*[@id="aso_search_form_anchor"]/button[4]')
search_button.click()

Dls_Links = driver.find_elements("xpath", '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[1]/div/table/tbody/tr')
time.sleep(10)
n=driver.find_element("xpath", '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[1]/div/table/tbody/tr[1]')
n.click()

data = {
    'Tenant': [],
    'Date': [],
    'Email': [],
    'Phone': [],
    'Travelers': [],
    'LOS': [],
    'Traveling To': [],
    'Facility': [],
    'Staff Composition': [],
    'Pet': [],
    'Note': []
}

while True:
    cargo_elements = driver.find_elements(By.XPATH, '//div[@style="line-height:15px"]/p')

    for i in range(1, len(cargo_elements), 22):
        title_element = cargo_elements[i].text
        date_element = cargo_elements[i + 8].text
        email_element = cargo_elements[i + 2].text
        phone_element = cargo_elements[i + 4].text
        travelers_element = cargo_elements[i + 6].text
        LOS_element = cargo_elements[i + 10].text
        facility_element = cargo_elements[i + 12].text
        staffComp_element = cargo_elements[i + 16].text
        pet_element = cargo_elements[i + 18].text
        note_element = cargo_elements[i + 20].text
        travto_element = cargo_elements[i + 10].text

        data['Tenant'].append(title_element)
        data['Date'].append(date_element)
        data['Email'].append(email_element)
        data['Phone'].append(phone_element)
        data['Travelers'].append(travelers_element)
        data['LOS'].append(LOS_element)
        data['Traveling To'].append(travto_element)
        data['Facility'].append(facility_element)
        data['Staff Composition'].append(staffComp_element)
        data['Pet'].append(pet_element)
        data['Note'].append(note_element)
    try:
        next_button = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]')
        next_button.click()
    except:
        break
        
df = pd.DataFrame(data)
df1 = df.loc[df.index % 2 == 0]
print(df1)

excel_file = "output.xlsx"
df1.to_excel(excel_file, index=False)