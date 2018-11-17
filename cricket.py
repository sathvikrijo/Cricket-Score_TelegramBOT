import requests
from emoji_handler import *
from bs4 import BeautifulSoup
from emoji import emojize

url = "https://www.cricbuzz.com/cricket-match/live-scores"

def match():
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    headers = soup.find_all(class_="cb-col cb-col-100 cb-lv-main")

    live_match = []
    live_match_links = []
    completed_match = []
    completed_match_links = []
    all_matches = []
    count = 1
    all_matches_string = ""
    ongoing_matches = ""
    finished_matches = ""

    first_links = soup.find(class_='text-hvr-underline text-bold')
    first_links.decompose()

    for head in headers:
        match_live = head.find_all(class_="cb-lv-scrs-well cb-lv-scrs-well-live")
        match_completed = head.find_all(class_="cb-lv-scrs-well cb-lv-scrs-well-complete")
        for match in match_live:
            live_match.append(match['title'])
            live_match_links.append(match['href'])
        for match in match_completed:
            completed_match.append(match['title'])
            completed_match_links.append(match['href'])

    for i in range(0,len(live_match)):
        print(live_match[i])
        print(url + live_match_links[i])
        emoji = get_emoji(count)
        all_matches_string += str(emoji) + "  " + live_match[i] + "\n"
        count+=1
    print()
    for i in range(0,len(completed_match)):
        print(completed_match[i])
        print(url + completed_match_links[i])
        emoji = get_emoji(count)
        all_matches_string += str(emoji) + "  " + completed_match[i] + "\n"
        count+=1

    return all_matches_string
if __name__ == "__main__":
    match()
