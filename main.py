from img_fetcher import img_fetch
from img_fetcher import get_soup
doc_list = ['pan card','aadhar card', 'passport','driving license']

for items in doc_list:
    img_fetch(items,items)
