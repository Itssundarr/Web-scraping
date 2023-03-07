from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import csv 
import pandas as pd

driver = webdriver.Chrome(executable_path="C:\\SUNDAR\\Chromedriver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.karunya.edu/cse/faculty")

names = driver.find_elements(By.TAG_NAME,"strong")
info = driver.find_elements(By.TAG_NAME,"span")

names_list=[]
C=1
for x in names:
    if x.text.strip()=="" or C==1:
        C+=1
        continue
    else:
        names_list.append(x.text.strip())

info_list = []
mail_id = []
designation = []

for x in info:
    if x.text.strip() == "" or x.text.strip()=="Profile":
        continue
    else:
        info_list.append(x.text.strip())

flag = True
for x in info_list:
    if(x!=""):
        c=1
        splitting = x.split("\n")
        for y in splitting:
            if(y=="Adjunct Professor"):
                flag=False
                break
            else:
                if(c==1):
                    designation.append(y)
                    c+=1
                elif(c==2):
                    mail_id.append(y)
        if(flag==False):
            break

with open("faculty_details.csv", mode = "w", newline="") as f:
     writer = csv.writer(f)
     writer.writerow(["Names", "Designation", "Mail ID"])
     f.write("\n")
     for x,y,z in zip(names_list,designation,mail_id):
        writer.writerow([x,y,z])

data = pd.read_csv("faculty_details.csv")
data.dropna()

print(data)