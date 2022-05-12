#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 23:54:01 2022
auto filing
@author: mirac

"""
import time
from selenium import webdriver
import PyPDF2 
name ="Mirac"
surname="Gokmen"
fullname = "Mirac Gokmen"
email="kabatasmirac0@gmail.com"
phone="8594409414"
address="300 Alumni Dr"
city = "Lexington"
state="Kentucky"
country = "Fayette"
postcode="40503"

file = open('/home/mirac/İndirilenler/cv_cover_letter/Mirac_Gokmen_Cover_Letter.pdf', 'rb')

# creating a pdf reader object
coverletter = PyPDF2.PdfFileReader(file)


file = open('/home/mirac/İndirilenler/cv_cover_letter/Mirac_Gokmen_Resume__.pdf', 'rb')

# creating a pdf reader object
resume = PyPDF2.PdfFileReader(file)


substring = "Apply"
browser = webdriver.Firefox()
link = 'https://neea-careers.hiringthing.com/job/417367/data-analyst-commercial-integrated-systems?s=inp'
browser.get(link)
app=browser.find_element_by_xpath("//button[@type='button' and contains(., 'Apply')]")
time.sleep(10)
python_button = browser.find_elements_by_link_text(app.find(substring))
python_button.click()


#find all form input fields via form name
_inputs = browser.find_elements_by_xpath('//form[@id="job-application-form"]//input')

for input in _inputs:                                                             
    #print attribute name of each input element 
    print (input.get_attribute('name'))
    
wname = browser.find_element_by_id("user.first_name")
wname.send_keys(name)
wsurname = browser.find_element_by_id("user.first_name")
wsurname.send_keys(surname)
wemail = browser.find_element_by_id("user.email")
wname.send_keys(email)
wname = browser.find_element_by_id("user.first_name")
wname.send_keys(name)
wname = browser.find_element_by_id("user.first_name")
wname.send_keys(name)
wname = browser.find_element_by_id("user.first_name")
wname.send_keys(name)
wname = browser.find_element_by_id("user.first_name")
wname.send_keys(name)