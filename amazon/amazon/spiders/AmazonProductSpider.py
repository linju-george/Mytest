# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
  name = "AmazonDeals"
  allowed_domains = ["amazon.com"]
  
  #Use working product URL below
  start_urls = [
"https://www.amazon.com/adidas-Mens-Originals-Blackbird-Logo/dp/B07466L947/ref=pd_sim_309_8?_encoding=UTF8&refRID=KAX1Q9F0W9VZQA4ZRNTH",
     ]

 
  def parse(self, response):
  	 items = AmazonItem()
 	 title = response.xpath('//h1[@id="title"]/span/text()').extract()
 	 sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
 	 category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
 	 availability = response.xpath('//div[@id="availability"]//text()').extract()
 	 items['product_name'] = ''.join(title).strip()
 	 items['product_sale_price'] = ''.join(sale_price).strip()
 	 items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
 	 items['product_availability'] = ''.join(availability).strip()
 	 yield items

