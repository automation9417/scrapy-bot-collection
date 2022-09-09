import os,re
from clicknium import clicknium as cc, locator
import requests

tab = cc.chrome.open("https://www.dpm.org.cn/online_search/cid/1005847.html")
elements = tab.find_elements(locator.dpm.a_查看)
for element in elements:
    href = element.get_property("href")
    new_tab = tab.browser.new_tab("https://www.dpm.org.cn/{}".format(href))
    src = new_tab.find_element(locator.dpm.iframe_pdf).get_property("src")
    url = "https://www.dpm.org.cn/Uploads/{}".format(src.split("=")[-1])
    sinfo = new_tab.find_element(locator.dpm.div_title).get_property("sinfo")
    file_name = ""
    for s in re.findall(r'-?\d+\.?\d*', sinfo):
        file_name += s
     
    pdf_file = requests.get(url)
    temp_file = os.path.join(os.getcwd(), "{}.pdf".format(file_name))
    open(temp_file, 'wb').write(pdf_file.content)
    new_tab.close()