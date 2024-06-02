import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

url = input("Enter the Wikipedia URL: ")
response = requests.get(url)

# print(page.text)
soup = BeautifulSoup(response.text,"html.parser")

# Prining the title
print("TITLE:")
print(soup.title.text)


# page_title = soup.find('h1', id='firstHeading').text.strip()
# printing the 1st para
print("1st PARA")
i=0
paragraphs =soup.find_all("p")
for paragraph in paragraphs:
 if (i<2):
   print(paragraph.text)
   i=i+1

# printing the external links
print("LINKS:")
# all_links=soup.find_all("a")
# for links in all_links:
#    print(links.text)
external_links = []
for link in soup.find_all('a', href=True):
    if 'http' in link['href']:
        external_links.append(link['href'])
for link in external_links:
  print(link)
 
 
# printing images:
images = []
for img in soup.find_all('img'):
    img_url = img['src']
    images.append({'url': img_url})

print("IMAGES:")
for img in images:
   print(img)
        

        
