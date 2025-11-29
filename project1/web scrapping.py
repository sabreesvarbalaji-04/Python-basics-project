import requests
import csv
#pip install BeautifulSoup
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
res=requests.get(url)

# header={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36"
# }

soup=BeautifulSoup(res.text,"html.parser")
quote_block=soup.find_all("div",class_="quote")

with open("scrapped.csv","w",newline="") as f:
    writer= csv.writer(f)
    writer.writerow(["Quote","Author"])


    for block in quote_block:
        q_content=block.find("span",class_="text").get_text(strip=True)
        author=block.find("small",class_="author").get_text(strip=True)
        # print("Quote:",q_content)
        # print("Author:",author)
        writer.writerow([q_content,author])
    
next_button=soup.find("li",class_="next")
if next_button:
    base_url=next_button.find("a")["href"]
    page_url=url+base_url
    print(page_url)
else:
    print("no next page")