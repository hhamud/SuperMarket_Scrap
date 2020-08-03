import requests
import xml.etree.ElementTree as ET 
import json
url_list = 'https://groceries.asda.com/sitemap-products.xml'
site_index = requests.get(url_list)
with open('site_index_links.xml', 'wb') as f:
    f.write(site_index.content)
parse_file = ET.parse('site_index_links.xml')
file_root = parse_file.getroot()
prod_id_list = [] 
for i in file_root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    prod_link = i.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text 
    prod_id = prod_link.split("/")[-1] 
    prod_id_list.append(prod_id)

print(len(prod_id_list))


