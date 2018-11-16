import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores"

def match():
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')

    headers = soup.find_all(class_="cb-col-100 cb-col cb-schdl")
    count = 1;
    match_details = ""
    ascii = ['','1⃣ ','2⃣ ','3⃣ ','4⃣ ','5⃣ ','6⃣ ','7⃣ ','8⃣ ','9⃣ ','🔟','1⃣1⃣ ','1⃣2⃣ ','1⃣3⃣ ','1⃣4⃣ ','1⃣5⃣ ']
    for head in headers:
        match_heading = head.find(class_="cb-lv-scr-mtch-hdr inline-block")
        if match_heading is not None:
            con = match_heading.find('a')
            match_title = con.contents[0]
            match_details += ascii[count] + " " + match_title[:-1] + "\n"
            count+=1
    print(match_details)
    return match_details
