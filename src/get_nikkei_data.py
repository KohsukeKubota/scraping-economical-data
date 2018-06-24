from selenium.webdriver import Chrome, ChromeOptions
import sys
import os
import csv
import urllib


if not os.path.isdir('../data/raw-data/'):
    os.makedirs('../data/raw-data/')
options = ChromeOptions()
options.add_argument('--headless')
driver = Chrome('../chromedriver', options=options)
driver.get('https://vdata.nikkei.com/economicdashboard/macro/')

# Get rid of 's'
str_list = [chr(i) for i in range(97, 97+18)]
str_list.remove('n')
str_list.remove('r')

content_list = driver.find_elements_by_class_name('content__section')
section_lists = [content.find_elements_by_class_name("a-section") for content in content_list]
element_index_list = [list(range(1, len(section_list)+1)) for section_list in section_lists]

title_list = []
i = 0

for (str_, section_list, element_index) in zip(str_list, section_lists, element_index_list):
    text_list = ["//*[@id='{}{}']/div/h5/span[1]".format(str_, element) for element in element_index]
    for text_, section_, element_ in zip(text_list, section_list, element_index):
        driver.execute_script("document.getElementById('{}{}').style.display='block';".format(str_, element_))
        title = section_.find_element_by_xpath("//*[@id='{}{}']/div/h5/span[1]".format(str_, element_)).text
        title_list.append(title)
        url = section_.find_element_by_xpath("//*[@id='{}{}']/div/div[2]/p[3]/a".format(str_, element_)).get_attribute("href")
        urllib.request.urlretrieve(url, '../data/raw-data/{}-{}.csv'.format(i, title))
        i += 1
        print(i)
