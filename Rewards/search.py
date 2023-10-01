import requests
import json
from datetime import date, timedelta
import settings as s
import pyautogui as gui
from time import sleep

class Searches:
    def getTrends(self, wordsCount: int) -> list:
        searchTerms: list[str] = []
        i = 0
        while len(searchTerms) < wordsCount:
            i += 1
            currentDate = (date.today() - timedelta(days=i)).strftime("%Y%m%d")
            r = requests.get(f"https://trends.google.com/trends/api/dailytrends?hl=en-US&ed={currentDate}&geo=US&ns=15")
            trends = json.loads(r.text[6:])
            for topic in trends["default"]["trendingSearchesDays"][0]["trendingSearches"]:
                searchTerms.append(topic["title"]["query"].lower())
                searchTerms.extend(
                    relatedTopic["query"].lower()
                    for relatedTopic in topic["relatedQueries"]
                )
            searchTerms = list(set(searchTerms))
        del searchTerms[wordsCount : (len(searchTerms) + 1)]
        return searchTerms
    
    def typeSearches(self, terms):
        searches = 0
        for searchQuery in terms:
            gui.hotkey("ctrl", "e")
            gui.typewrite(searchQuery, 0.005)
            gui.press("enter")
            sleep(0.5 + s.speed)
            searches += 1
            if searches == s.desktopSearches + s.edgeBonusSearches and s.mobileSearches > 0:
                sleep(.3 + s.speed)
                gui.hotkey("ctrl", "shift", "i")
                sleep(1.5 + s.speed)
                gui.hotkey("ctrl", "shift", "m")
                sleep(.5 + s.speed)
        # After all the searches
        sleep(1 + s.speed)
        gui.hotkey("ctrl", "shift", "m")
        sleep(0.3 + s.speed)
        gui.hotkey("ctrl", "w")
    
    def runSearches(self):
        searchTerms = self.getTrends(s.desktopSearches + s.edgeBonusSearches + s.mobileSearches)
        print(searchTerms)
        self.typeSearches(searchTerms)

if __name__ == "__main__":
    # The ctrl e shortcut triggers the search files in vscode
    searchClass = Searches()
    searchClass.runSearches()
    