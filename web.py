from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json
  
def applicant( driver ) :
    with open('applicant_data.json',encoding="utf-8") as f:
        applicant_data = json.load(f)

    input_field1 = driver.find_element( By.NAME, 'eedb1000.applyName')  
    input_field1.send_keys(applicant_data['applyName'])
    input_field2 = driver.find_element( By.NAME, 'eedb1000.applyId')  
    input_field2.send_keys(applicant_data['applyId'])
    input_field3 = driver.find_element( By.NAME, 'eedb1000.companyAddr')  
    input_field3.send_keys(applicant_data['companyAddr'])

def applicant_company( driver ) :
    with open('applicant_company.json',encoding="utf-8") as f:
        applicant_company = json.load(f)

    input_field1 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[1]/tbody/tr[4]/td[2]/input')
    input_field1.send_keys(applicant_company['banNo'])
    input_field2 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[4]/table/tbody/tr[6]/td[2]/input') 
    input_field2.send_keys(applicant_company['applyId'])

def legal_person( driver ) :
    with open('legalp_data.json',encoding="utf-8") as f:
        legalp_data = json.load(f)

    input_field1 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[2]/td[2]/input')
    input_field1.send_keys(legalp_data['orgCorpName'])
    input_field2 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[3]/td[2]/input') 
    input_field2.send_keys(legalp_data['orgCorpNo'])

def agent( driver ) :
    with open('agent_data.json',encoding="utf-8") as f:
        agent_data = json.load(f)

    select = Select(driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td[2]/select'))
    if agent_data['attorAttrib'] == "會計師" :
        select.select_by_value("1")
    else :
        select.select_by_value("2")

    input_field1 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td[2]/input')
    input_field1.send_keys(agent_data['attorName'])
    input_field2 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[3]/td[2]/input') 
    input_field2.send_keys(agent_data['attorId'])
    input_field3 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[4]/td[2]/input') 
    input_field3.send_keys(agent_data['attorNo'])
    input_field4 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[5]/td[2]/input') 
    input_field4.send_keys(agent_data['attorAddr'])
    input_field5 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[6]/td[2]/input') 
    input_field5.send_keys(agent_data['attorTel'])

def pre() :
    driver = webdriver.Chrome()
    driver.get('https://serv.gcis.nat.gov.tw/eicm/prefixedit/prefixOneEditAction.do')
    driver.implicitly_wait(10)

    alert = driver.switch_to.alert
    alert.dismiss()

    with open('preload.json') as f:
        preload = json.load(f)

    if preload['caseCode'] == "Z1" :
        applicant(driver)
        if preload['roleType'] == 2 :
            button = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[1]/tbody/tr[3]/td[2]/input[2]')
            button.click()
            legal_person(driver)

    elif preload['caseCode'] == "Z2" :
        button = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[1]/tbody/tr[2]/td[2]/input[2]')
        button.click()
        applicant_company(driver)

        if preload['roleType'] == 2 :
            button = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[1]/tbody/tr[3]/td[2]/input[2]')
            button.click()

    if preload['writerType'] == 2 : 
        button = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[1]/tbody/tr[5]/td[2]/input[2]')
        button.click()  
        agent(driver)   

    with open('normal_case.json',encoding="utf-8") as f:
        normal_case = json.load(f)

    input_field1 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[2]/td[2]/input')
    input_field1.send_keys(normal_case['contactName'])
    input_field2 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[3]/td[2]/input') 
    input_field2.send_keys(normal_case['contactTel'])
    input_field3 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[4]/td[2]/input') 
    input_field3.send_keys(normal_case['contactCel'])
    input_field4 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[5]/td[2]/input') 
    input_field4.send_keys(normal_case['contactAddr'])
    
    if normal_case['contactGetKind'] == "自取" :
        button = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[6]/td[2]/input[1]')
        button.click()
    else :
        button = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[2]/tbody/tr[6]/td[2]/input[2]')
        button.click()

    input_field5 = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[3]/tbody/tr[2]/td[2]/input') 
    input_field5.send_keys(normal_case['cmpyRemitEname'])

    select = Select(driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[4]/tbody/tr[4]/td[2]/select'))
    if normal_case['orgnType'] == "股份有限公司" :
        select.select_by_value("01")
        if normal_case['closeCheck'] == "是" :
            button = driver.find_element( By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/table[4]/tbody/tr[4]/td[2]/span/input[1]')
            button.click()
            button = driver.find_element( By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr[2]/td/input[1]')
            button.click()

    elif normal_case['orgnType'] == "有限公司" :
        select.select_by_value("02")
    elif normal_case['orgnType'] == "無限公司" :
        select.select_by_value("03")
    elif normal_case['orgnType'] == "兩合公司" :
        select.select_by_value("04")
    
    print(type(normal_case['companyName']))

    for i in range(len(normal_case['companyName'])):
        print(normal_case['companyName'][i])
        front = "eedb3000Array["
        back = "].companyName"
        temp = front + str(i) + back
        input_field = driver.find_element( By.NAME, temp ) 
        input_field.send_keys(normal_case['companyName'][i])

    sleep(100)
    driver.quit()

def main() :

    success = False
    
    while not success :
        try :
            pre()
            success = True
        except Exception as exp:
            print(exp)

if __name__ == "__main__":
    main()