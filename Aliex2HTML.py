import json
from bs4 import BeautifulSoup
import requests
import re
import time
import sys


class AliexpressProuct:
	Url = ""
	Title = ""
	Image = ""
	Price = ""
	Rating = ""
	Orders = ""

def GetProductinfo(ProductUrl):
	Product = AliexpressProuct()

	AliRequest = requests.get(ProductUrl)
	ProductHtml = AliRequest.text
	HtmlSoup = BeautifulSoup(ProductHtml, "lxml")
	
	Product.Url = (AliRequest.url)
	Product.Title = (HtmlSoup.select('h1.product-name')[0].string)
	Product.Price = (HtmlSoup.select(".p-price")[0].string)
	Product.Image = (HtmlSoup.select('meta[property=og:image]')[0].attrs['content'])
	Product.Rating = (HtmlSoup.select('span[itemprop=ratingValue]')[0].string)
	Product.Orders = (HtmlSoup.select('span.order-num')[0].string)
	
	return Product
	
		
if __name__ == "__main__":
	f = open(sys.argv[1])
	
	#Style
	file = open("Output.html","w") 
	file.write("<!DOCTYPE html><html><head><style>table,th,td{border:1px solid black;border-collapse:collapse}</style></head><body>")
	file.write("<center><table><tr><th>Picture</th><th>Name</th><th>Rating</th><th>Orders</th><th>Price</th></tr>")	
	file.close()

	
	lines = f.readlines()
	for line in lines:
	
		file = open('Output.html', 'a')
		
		Product = GetProductinfo(line)
		
		file.write("<tr>")
		file.write("<th>"+"<img width='150px' src='"+Product.Image+"'/>"+"</th>") 
		file.write("<th>"+Product.Title+"</th>") 
		file.write("<th>"+Product.Rating+"</th>") 
		file.write("<th>"+Product.Orders+"</th>") 
		#file.write("<th>"+Product.Price+"$"+"</th>") 
		file.write("</tr>")