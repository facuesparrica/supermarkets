from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

wdriver = webdriver.Chrome('/Users/facu/PycharmProjects/Supermarkets/chromedriver')

wdriver.get('https://www.disco.com.ar/Login/PreHome.aspx')
delay = 20 # seconds
time.sleep(delay)


html = wdriver.page_source
soup = BeautifulSoup(html, 'lxml')
all_li_items = soup.find_all('li')


categories = [item.text for item in all_li_items if item.has_attr('data-second-level-id')]
id_category = [item['data-second-level-id'] for item in all_li_items if item.has_attr('data-second-level-id')]
print(f'# Categorias: {len(categories)}')
print(f'# Ids:{len(id_category)}')
#for category,id_nb in zip(categories,id_category):

#    print(f'{category}: {id_nb}')

# sample_ids = id_category[:100]

#for item in sample_ids:
#    print(item)


for categ_id, categ_name in  zip(id_category, categories):
    print(f'Getting {categ_name}')
    url = f'https://www.disco.com.ar/Comprar/Home.aspx#_atCategory=false&_atGrilla=true&_id={categ_id}'
    #wdriver.refresh()
    #wdriver.get(f'https://www.disco.com.ar/Comprar/Home.aspx#_atCategory=false&_atGrilla=true&_id={categ_id}')
    time.sleep(3)
    wdriver.get(url)
    time.sleep(3)
    wdriver.refresh()
    time.sleep(delay)
    html = wdriver.page_source
    #wdriver.close()
    soup = BeautifulSoup(html, 'lxml')
    product_info_box = soup.find_all('div', {'class': 'grilla-producto-informacion'})
    #print(len(product_info_box))

    # driver.quit()
    producto = []
    precio_unitario = []
    for item in product_info_box:
        descripcion = item.find('div', {'class': 'grilla-producto-descripcion'}).string
        producto.append(descripcion)
        # print(descripcion)
        tag_precio = item.find('div', {'class': 'grilla-producto-precio'}).text
        #precio = tag_precio.get_text()
        # print(precio)
        unidades = item.find('div', {'class': 'grilla-producto-unidades'}).text
        precio_unitario.append(unidades)
        # print(unidades)
        data_tuples = zip(producto, tag_precio, precio_unitario)
        df = pd.DataFrame(data_tuples, columns=['descripcion', 'precio', 'precio_unit'])
        name = categ_name.lower()
        name = name.replace(' ', '_')
        print('TO CSV')
        df.to_csv(f'{categ_id}_{name}.csv')

