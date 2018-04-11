import requests
from bs4 import BeautifulSoup

#load_web_sourcecode is an object of the get class
load_web_sourcecode = requests.get("http://pythonhow.com/example.html")
#grab content for sourcecode


web_content = load_web_sourcecode.content
#print(web_content)

#beautifulsoup parses the source code of the webpage

#pasing_content is an object of the class BeautifulSoup
parsing_content = BeautifulSoup(web_content,"html.parser")

#find the tag of the page you need
#! using find_all() finds the list of possible divs
divs_we_need = parsing_content.find_all("div", {"class":"cities"})
#type(divs_we_need) = lists so we can use indexing

#!using find() finds a particular tag
#ivs_we_need_with_find = parsing_content.find("div", {"classe":"citites"})
#print (parsing_content.prettify())
print(len(divs_we_need))
print(divs_we_need[0])
#print(divs_we_need_with_find"\n")'



# to extract the h2 of the div1
h2_for_div1 = divs_we_need[0].find_all("h2")[0]
print(h2_for_div1.text)


# to extract the h2 of the div2
h2_for_div2 = divs_we_need[1].find_all("h2")[0]
print(h2_for_div2.text)
# to extract the h2 of the div3
h2_for_div3 = divs_we_need[2].find_all("h2")[0]
print(h2_for_div3.text)


#using for loops
for div in divs_we_need:
    print(div.find_all("h2")[0].text)