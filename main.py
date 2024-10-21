from operator import index
from re import match
from sys import executable
from textwrap import indent

from Tools.scripts.fixnotice import process
from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

import json

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://online.gs1tr.org/login")

time.sleep(3)


with open("items.json") as file:
    items = json.load(file)

def register_EAN(item: dict):

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe"))

    #set_language to EN
    lang_selectors = driver.find_elements(By.NAME, "lang")

    for lang_selector in lang_selectors:
        Select(lang_selector).select_by_value("en")

    #select_new
    gcp_id_new_selector = driver.find_element(By.XPATH, '//select[@formcontrolname="gcpIdNew"]')
    Select(gcp_id_new_selector).select_by_value("85302")

    time.sleep(2)

    # click the new barcode button
    new_barcode_button = driver.find_element(By.CLASS_NAME, "swal2-cancel")
    new_barcode_button.click()

    #wait for it to load
    time.sleep(2)

    #enter the brand name
    brand_name_text_input = driver.find_element(By.XPATH, "//input[@type='text' and @maxlength='70']")
    brand_name_text_input.send_keys(item["Brand"])

    # enter the product name
    item_name_text_input = driver.find_element(By.XPATH, "//input[@type='text' and @maxlength='500']")
    item_name_text_input.send_keys(item["Item Name"])

    # select target market default: "Tüm Dünya"
    target_market_selector = driver.find_element(By.XPATH, '//select[@class="form-control col-md-10 col-lg-11 ng-untouched ng-pristine ng-invalid"]')
    Select(target_market_selector).select_by_value("260")

    # enter net amount, default: "1"
    net_amount_text_input = driver.find_element(By.XPATH, "//input[@type='text' and @maxlength='20']")
    net_amount_text_input.send_keys("1")

    # select amount unit, default: "Adet"
    amount_unit_selector = driver.find_element(By.XPATH, '//select[@class="form-control ng-untouched ng-pristine ng-invalid"]')
    Select(amount_unit_selector).select_by_value("1")

    # select the segment of the product
    segment_selector = driver.find_element(By.NAME, "select_segment")
    Select(segment_selector).select_by_value(str(item["Segment"]))

    time.sleep(2)

    # select the family of the product
    family_selector = driver.find_element(By.NAME, "select_family")
    Select(family_selector).select_by_value(str(item["Family"]))

    time.sleep(2)

    # select the class of the product
    class_selector = driver.find_element(By.NAME, "select_class")
    Select(class_selector).select_by_value(str(item["Class"]))

    time.sleep(2)

    # select the brick of the product
    brick_selector = driver.find_element(By.NAME, "select_brick")
    Select(brick_selector).select_by_value(str(item["Brick"]))

    time.sleep(2)

    # click the submit button to create ean
    submit_button = driver.find_element(By.XPATH, '//button[@class="btn btn-gs1orange mx-1"]')
    submit_button.click()

    #wait for it to load
    time.sleep(2)

    #check the box to agree
    checkbox = driver.find_element(By.ID, "swal2-checkbox")
    checkbox.click()

    # click to confirm TEST: CLICK CANCEL
    confirm_button = driver.find_element(By.CLASS_NAME, "swal2-confirm")
    confirm_button.click()

    time.sleep(2)

    ean_div = driver.find_element(By.ID, "swal2-content")
    text = ean_div.text
    match = re.search(r'(\d{13})', text)


    if match:
        ean = match.group(1)
        ok_button = driver.find_element(By.CLASS_NAME, "swal2-confirm")
        ok_button.click()
        driver.switch_to.default_content()
        return int(ean)
    else:
        ok_button = driver.find_element(By.CLASS_NAME, "swal2-confirm")
        ok_button.click()
        driver.switch_to.default_content()
        return ""

input("Solve the captcha and login. Navigate to the barcode form and press enter.")

for item in items:

    ean_number = register_EAN(item)

    item["EAN"] = ean_number
    print(item)
    print(f"Processed: {items.index(item)}/{len(items)}")
    time.sleep(2)

with open("items.json", "w") as json_file:
    json_data = json.dumps(items, indent=4)
    json_file.write(json_data)

print(items)

input("Script ended. Press Enter to exit...")

driver.quit()

