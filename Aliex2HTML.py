import requests
from bs4 import BeautifulSoup
import sys

class AliexpressProuct:
	Url = ""
	Title = ""
	Image = ""

def GetProductinfo(ProductUrl):
    Product = AliexpressProuct()
    page = requests.get(ProductUrl)

    soup = BeautifulSoup(page.content, 'html.parser')
    Product.Url = ProductUrl
    Product.Title = soup.find("meta", property="og:title").get('content')
    Product.Image = soup.find("meta", property="og:image").get('content')
    return(Product)


if __name__ == "__main__":
	f = open(sys.argv[1])

    #Style
	file = open("Output.html","w") 
	file.write("<!DOCTYPE html><html><head><style>table,th,td{border:1px solid black;border-collapse:collapse}</style></head><body>")
	file.write("<center><table><tr><th>Picture</th><th>Name</th></tr>")	
	file.close()

	lines = f.readlines()
	for line in lines:
		file = open('Output.html', 'a')
		Product = GetProductinfo(line)
		file.write("<tr>")
		file.write("<th>"+"<img width='150px' src='"+Product.Image+"'/>"+"</th>") 
		file.write("<th><a href='"+Product.Url+"'>"+Product.Title+"</a></th>") 
		file.write("</tr>")
