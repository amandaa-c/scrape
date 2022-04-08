# Import BeautifulSoup
from bs4 import BeautifulSoup

# To read an HTML file with bs
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
print(doc)
# You should now see the Python output of html document
# In order to prettify the document do:
print(doc.prettify()) 

# How to find things by the tag name 
tag = doc.title
print(tag) 

# To access string inside of the tag
tag.string = "hello"
