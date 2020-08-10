import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

wdriver = webdriver.Chrome('/Users/facu/PycharmProjects/Supermarkets/chromedriver')

wdriver.get('https://www.disco.com.ar/Comprar/Home.aspx#_atCategory=false&_atGrilla=true&_id=446243')

#time.sleep(30)

navigationStart = wdriver.execute_script("return window.performance.timing.navigationStart")
responseStart = wdriver.execute_script("return window.performance.timing.responseStart")
domComplete = wdriver.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

html = wdriver.page_source
soup = BeautifulSoup(html, 'lxml')
product_info_box = soup.find_all('div', {'class': 'grilla-producto-informacion'})

#driver.quit()

for item in product_info_box:
    descripcion = item.find('div', {'class': 'grilla-producto-descripcion'}).string
    print(descripcion)
    #tag_precio = item.find('div', {'class': 'grilla-producto-precio'})
    #precio = tag_precio.get_text()
    #print(precio)
    unidades = item.find('div', {'class': 'grilla-producto-unidades'}).text
    print(unidades)

"""
product_info_box = wdriver.find_elements_by_class_name('grilla-producto-informacion')
for item in product_info_box:
    tag_prod = item.find_elements_by_class_name('grilla-producto-descripcion')
    producto = tag_prod.get_attribute('textContent')
    print(producto)
    tag_precio = item.find_elements_by_class_name('grilla-producto-precio')
    precio = tag_precio.tag_prod.get_attribute('textContent')
    print(precio)
"""
#for item in product_info_box:
#   print(item)
#r = requests.get('https://www.disco.com.ar/Comprar/Home.aspx#_atCategory=false&_atGrilla=true&_id=446243')
#r = requests.get('https://www.disco.com.ar/', verify=False)

#r = requests.get('https://www.disco.com.ar/Login/PreHome.aspx')
#'https://www.disco.com.ar/Login/PreHome.aspx'
#url = 'https://www.infobae.com/?noredirect'

#r = requests.get(url)

#soup = BeautifulSoup(r.text, 'html_parser')
#
#product_info_box = soup.find_all('div', {'class': 'grilla-producto-informacion'})
#


