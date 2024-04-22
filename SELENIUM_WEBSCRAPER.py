from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook


driver = webdriver.Chrome()


driver.get("https://docs.google.com/document/d/1rL1bDfmnDETXuz4KomaxhGqtBNWbpPoHIjHodbqrpkw/edit")


time.sleep(5)


doc_content = driver.find_element(By.XPATH, "//div[@aria-label='Document content']")
text_content = doc_content.text.split('\n')  # Split the text content by newline to get rows


driver.quit()


wb = Workbook()
ws = wb.active

current_heading = None  


row_idx = 1
for line in text_content:
    if line.startswith("Heading"):
        current_heading = line
    else:
        if current_heading:
            ws.cell(row=row_idx, column=1, value=current_heading)
            ws.cell(row=row_idx, column=2, value=line)
            row_idx += 1


wb.save("extracted_data.xlsx")
