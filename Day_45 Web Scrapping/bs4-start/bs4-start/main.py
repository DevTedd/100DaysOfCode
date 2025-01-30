from bs4  import BeautifulSoup
import lxml#backup parser
import os


with open(r"C:\Users\tkmwangi\Documents\GitHub\100DaysOfCode\Day_45 Web Scrapping\bs4-start\bs4-start\website.html") as file:
    contents = file.read()

#path = 'Day_45 Web Scrapping\bs4-start\bs4-start\website.html'

#with open("Day_45 Web Scrapping\bs4-start\bs4-start\website.html") as file:
#    contents= file.read()
    
soup = BeautifulSoup(contents, 'html.parser')

#print(soup.title.string) Actual string of the title 

#print(soup)#This prints out the entire html code
#print(soup.prettify) # Makes it indented 
#print(soup.a)
#print(soup.h1.string)

#How to Get SPECIFIC SECTIONS

all_anchor_tags = soup.find_all(name = 'a')
#print(all_anchor_tags)

#To just get the text in the first anchor tag
for tag in all_anchor_tags:
    #print(tag.getText()) - to get the texts
    #print(tag.get("href"))  - just for the links
    pass
    
#Get the values in a specific element 
heading = soup.find(name = 'h1',id='name')
#print(heading)

#Using the class attribute
section_heading = soup.find(name = 'h3', class_ = 'heading')
#print(section_heading)# 
# print(section_heading.text)
# print(section_heading.name)
# print(section_heading.text)

#Narrowing it down to a specific section of the website using CSS Selectors
# company_url = soup.select_one(selector='p a')
# print(company_url)

# name = soup.select_one(selector='#name')
# print(name)

headig_list = soup.select(selector='.heading')
print(headig_list)
