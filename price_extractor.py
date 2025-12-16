# Step 1 - Install Reauired libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import time

def extract_last_page_number():
    url = "https://unique.com.mm/collections/mobile-phone"

    # request data from the website
    data = requests.get(url)
    # extract web code html, css, js, etc.
    web_data = data.text
    print("Status: ", data)
    print("\n")

    # clean extracted web data and create beautifulsoup object
    bsObj = BeautifulSoup(web_data, "html5lib")

    # Extract Last Page Number
    # find tag that contains all page numbers
    page_nums_tag = bsObj.find('div', class_='pagination__nav')
    # find all page number tags
    page_num_tag_list = bsObj.find_all('a', class_='pagination__nav-item link')
    last_page_num_tag = page_num_tag_list[-1] # get the last tag
    last_page_num = int(last_page_num_tag.text)
    
    return last_page_num

def extract_product_name(tag):
    """Extract product name from the dummy tag."""
    # extract product's name tag
    product_name_tag = tag.find('a', class_='product-item__title text--strong link')
    # extract product's name using text attribute
    product_name = product_name_tag.text
    return product_name

def extract_product_price(tag):
    """Extract product price from the dummy tag."""
    # extract product's price tag
    product_price_tag = tag.find('span', class_='price')
    # extract product's price using text attribute
    product_price = product_price_tag.text
    # remove unwanted characters from price
    product_price = product_price.replace("K", "")
    product_price = product_price.replace(",", "")
    product_price = product_price.replace("From ", "")
    product_price = float(product_price) # change str to int type
    return product_price

def extract_product_status(tag, class_name):
    """Extract product status from the dummy tag."""
    # extract product's status tag
    product_status_tag = tag.find('span', class_=class_name)
    # extract product's status using text attribute
    product_status = product_status_tag.text
    return product_status

# Create empty lists to store extracted data
product_name_list = [] # to store extracted product name
product_price_list = [] # to store extracted product price
product_status_list = [] # to store extracted product status

def main():
    # Extract Last Page Number
    last_page_number = extract_last_page_number()

    for page_num in tqdm(range(1, last_page_number+1)):
        url = "https://unique.com.mm/collections/mobile-phone" + "?page=" + str(page_num)   
        # request data from the website
        data = requests.get(url)
        # extract web code html, css, js, etc.
        web_data = data.text
        #print("Status: ", data)
        #print("\n")

        # clean extracted web data and create beautifulsoup object
        bsObj = BeautifulSoup(web_data, "html5lib")

        # find main div tags
        main_tags = bsObj.find_all('div', class_='product-item__info-inner')

        for dummy_tag in main_tags:
            try:
                product_name_2 = extract_product_name(dummy_tag)
                product_name_list.append(product_name_2)

                product_price_2 = extract_product_price(dummy_tag)
                product_price_list.append(product_price_2)
                
                # create status classes list to handle different class names
                status_classes = ['product-item__inventory inventory',
                                  'product-item__inventory inventory inventory--high',
                                  'product-item__inventory inventory inventory--low']
                
                for status_class_name in status_classes:
                    try:
                        product_status_2 = extract_product_status(dummy_tag, status_class_name)
                        product_status_list.append(product_status_2)
                    except:
                        continue
                
                time.sleep(0)
            except:
                print(dummy_tag)
                raise
                break

    # Export data as an Excel file.
    data_dic = {"Product Name":product_name_list,
                "Product Price":product_price_list,
                "Product Status":product_status_list}

    # Create a dataframe
    df = pd.DataFrame(data_dic)
    # Create filename version and save as excel file.
    time_str = datetime.now().strftime("%H-%M-%S")
    df.to_excel("Output " + time_str + ".xlsx", index=False)

    print("All steps are completed!")
    
if __name__=="__main__":
    main()