# Temperature from TMD official website version 2.0
# This file is part of CPE-203 Project
# Copyright 2020 by Teeraphat Kullanankanjana
# Last update 05-02-2020


from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from googletrans import Translator


def temperature_generate(province_id):  # function for reference data from TMD website and generate data
    try:
        url = "https://www.tmd.go.th/province.php?id=" + str(province_id)  # TMD URL and ID is province that we need to know the temp
        web_open = req(url)  # open website from URL
        page_html = web_open.read()  # read entire of website and the result will be HTML text
        web_open.close()  # close website

        data = soup(page_html, "html.parser")  # convert html text to Beautiful Soup Object

        temp = data.findAll("td", {"class": "strokeme"})  # find element of Temperature (Element name "strokeme")
        province = data.findAll("span", {"class": "title"})  # find element of province (Element name "title")

        pv = province[0].text.replace(" ",
                                      " ")  # clear junk or unreadable character  then the remain will be province data
        result = temp[0].text  # clear junk or unreadable character  then the remain will be temp data

        trans = Translator()  # assign "trans" for translator function
        t = trans.translate(str("province" + pv), src="th", dest="en")  # translate province string from TH to EN
        print("จังหวัด: {} อุณหภูมิ {}".format(pv, result))  # display data (TH)
        print("{} temperature: {}".format(t.text, result))  # display data (EN)
    except:
        print("No result yet")  # display when Index out of range(can't find element from website)


for i in range(1, 82):  # Loop for province ID (For more information please open "province ID .xlsx  file ")
    print(i)  # display province ID
    temperature_generate(i)  # call function using province ID  as parameter
