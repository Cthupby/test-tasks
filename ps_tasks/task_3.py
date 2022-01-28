# requirement lxml
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_upcoming_events():
    ''' Url of document for a parsing '''
    url = "https://www.python.org/"
    r = requests.get(url=url)
    ''' Making soup '''
    soup = BeautifulSoup(r.text, "lxml")
    ''' To parse a document into div and li to find events '''
    div = soup.find_all("div", class_="shrubbery")
    events = div[1].find_all("li")
    ''' To store events data '''
    events_dict = {}
    ''' Iteration for events dict '''
    for event in events:
        events_dict['title'] = event.find("a").text.strip()
        events_dict['url'] = f"https://www.python.org/{event.get('href')}"
        event_date = event.find("time").get("datetime")
        event_date_iso = datetime.fromisoformat(event_date)
        events_dict['date'] = datetime.strftime(event_date_iso, '%Y/%m/%d')
        print("{ed[title]} | {ed[url]} | {ed[date]}".format(ed=events_dict))


if __name__ == '__main__':
    print(get_upcoming_events())
