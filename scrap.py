import requests
from bs4 import BeautifulSoup
import csv

def scarp():
    f = csv.writer(open('csvFILE.csv','w'))
    f.writerow(['Name', 'Link'])

    pages = []
    for i in range(1,5):
        url = "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ" + str(i) + ".htm"
        pages.append(url)

    for item in pages:
        page = requests.get(item)

        soup = BeautifulSoup(page.text,'html.parser')
        #print (soup.prettify())

        last_links = soup.find(class_='AlphaNav')
        last_links.decompose()

        all_artist_page = soup.find(class_='BodyText')
        all_artist_name_list = all_artist_page.find_all('a')

        for artist_name in all_artist_name_list:
            name = artist_name.contents[0]
            link = "https://web.archive.org" + artist_name.get('href')
            f.writerow([name, link])

if __name__ == "__main__":
    scarp()
