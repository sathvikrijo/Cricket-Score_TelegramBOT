import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores"
live_match = []
live_match_links = []
completed_match = []
completed_match_links = []
all_matches = []
ongoing_matches = ""
finished_matches = ""
live_match_len = 0
completed_match_len = 0

def match():
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    headers = soup.find_all(class_="cb-col cb-col-100 cb-lv-main")


    first_links = soup.find(class_='text-hvr-underline text-bold')
    first_links.decompose()

    global live_match
    global completed_match
    global live_match_links
    global completed_match_inks
    
    live_match.clear()
    completed_match.clear()
    live_match_links.clear()
    completed_match_links.clear()

    for head in headers:
        match_live = head.find_all(class_="cb-lv-scrs-well cb-lv-scrs-well-live")
        match_completed = head.find_all(class_="cb-lv-scrs-well cb-lv-scrs-well-complete")
        for match in match_live:
            live_match.append(match['title'])
            live_match_links.append(match['href'])
        for match in match_completed:
            completed_match.append(match['title'])
            completed_match_links.append(match['href'])

    global live_match_len
    global completed_match_len
    live_match_len = len(live_match)
    completed_match_len = len(completed_match)
    
    print(live_match_len)
    print(completed_match_len)

    all_matches_string = ""
    count = 1
    
    if live_match_len > 0:
        all_matches_string += "*************LIVE MATCHES*************\n"
        for i in range(0,live_match_len):
            print(live_match[i])
            print(url + live_match_links[i])
            all_matches_string += str(count) + " >>> " + live_match[i] + "\n\n"
            count+=1
        all_matches_string += "\n\n"

    if completed_match_len > 0:
        all_matches_string += "*********COMPLETED MATCHES*********\n"
        for i in range(0,completed_match_len):
            print(completed_match[i])
            print(url + completed_match_links[i])
            all_matches_string += str(count) + " >>> " + completed_match[i] + "\n\n"
            count+=1
    
    if live_match_len==0 and completed_match_len==0:
        all_matches_string = "Currently, There is neither no live matches nor recently ended matches."
    return all_matches_string

def extract_live_match(match_url):
    match_page = requests.get("https://www.cricbuzz.com/" + match_url)
    soup = BeautifulSoup(match_page.text,'html.parser')

    match_details = ""
    main_content = soup.find(class_="cb-col cb-col-67 cb-nws-lft-col cb-comm-pg")

    match_header = main_content.find(class_="cb-min-bat-rw")

    prevSession = main_content.find_all(class_="cb-col cb-col-67 cb-scrs-wrp")
    prevSession = prevSession[0]
    info = prevSession.find_all(class_="cb-text-stump")
    if info == []:
        info = prevSession.find_all(class_="cb-text-inprogress")
        if info == []:
            info = prevSession.find_all(class_="cb-text-lunch")
            if info == []:
                info = prevSession.find_all(class_="cb-text-rain")
                if info == []:
                    info = prevSession.find_all(class_="cb-text-tea")
    info = info[0].contents[0]
    prevSession = prevSession.find(class_="cb-text-gray cb-font-16")
    if prevSession is not None:
        prevSession = prevSession.contents[0][1:]
        match_details += "Previous session: " + prevSession + "\n\n"

    rr = main_content.find(class_="cb-font-12 cb-text-gray")
    rr = rr.find_all("span")
    rr = rr[1].text

    match_score = match_header.find(class_="cb-font-20 text-bold")
    #match_current_status =  match_current_status[0]

    match_details += "Current session: " + match_score.contents[0][1:] + "\n"
    match_details += "Current RR: " + rr +"\n" + info

    print(match_details)
    print()
    return match_details

def extract_completed_match(match_url):
    match_page = requests.get("https://www.cricbuzz.com/" + match_url)
    soup = BeautifulSoup(match_page.text,'html.parser')
    
    abandon = 0
    match_details = ""
    
    main_content = soup.find(class_="cb-col cb-col-67 cb-nws-lft-col cb-comm-pg")
    result = main_content.find(class_="cb-col cb-col-100 cb-min-stts cb-text-mom")
    if result is None:
        result = main_content.find(class_="cb-col cb-col-100 cb-min-stts cb-text-complete")
        if result is None:
            result = soup.find(class_="cb-col cb-col-100 cb-font-18 cb-toss-sts cb-text-abandon")
            abandon = 1
    result = result.contents[0]

    if abandon == 0:
        match_header = main_content.find_all(class_="cb-col cb-col-100 cb-col-scores")
        match_header = match_header[0]

        Session = match_header.find(class_="cb-col cb-col-100 cb-min-tm cb-text-gray")
        match_details += Session.contents[0] + "\n"

        Session = match_header.find(class_="cb-col cb-col-100 cb-min-tm")
        match_details += Session.contents[0] + "\n\n"

    match_details += result
    print(match_details)
    return match_details

if __name__ == "__main__":
    match()
