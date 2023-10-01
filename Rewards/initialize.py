# Files
import settings as s
import utils
# Libraries
import pyautogui as gui
from webbrowser import register, get, BackgroundBrowser
from time import sleep
import pytesseract
import cv2
import numpy as np
import os


class Initialize:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nisch\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    def openEdge(self, edgePath, rewardsUrl):
        # Register Microsoft Edge as the preferred browser
        if os.path.exists(edgePath):
            register("edge", None, BackgroundBrowser(edgePath))
            get("edge").open(rewardsUrl)
        else:
            utils.error("Edge path is incorrect")
      

    def loadWindow(self, maxLoadTime):
        images = [("Rewards/images/reloadPage.png", (21, 54, 277, 45)),
                  ("Rewards/images/reloadPageDarkTheme.png", (11, 46, 265, 58))]
        loadTime = 0.0
        breakFromLoop = False
        while loadTime <= maxLoadTime:
            for image, region in images:
                if gui.locateOnScreen(image, confidence=0.9, grayscale=True, region=region) is not None:
                    # Set variable to true to break from the while loop
                    breakFromLoop = True
                    # Break out of for loop
                    break
            # Break out of while loop
            if breakFromLoop == True:
                sleep(0.5+s.speed)
                print("Page loaded")
                break
            else:
                loadTime += 0.5
                sleep(0.5 + s.speed)
                

    def dismissPopups(self):
        # Set page to correct zoom, close notifications, default browser popup, check for shopping popup, close the promotion box
        gui.hotkey("ctrl", "0")

        # notification = gui.locateCenterOnScreen("Rewards/images/closenotif.png", region=(1599, 457, 321, 550), grayscale=True)
        # if notification != None:
        #     gui.click(notification)
        #     sleep(0.3+s.speed)

        # defaultbrowser = gui.locateCenterOnScreen("Rewards/images/defaultbrowser.png", region=(1526, 153, 394, 147))
        # if defaultbrowser != None:
        #     gui.click(defaultbrowser)
        #     sleep(0.2+s.speed)

        # popup = gui.locateCenterOnScreen("Rewards/images/closestuff.png", region=(984, 0, 933, 703))
        # if popup != None:
        #     gui.click(popup)

        # for _ in range(5):
        #     sneakpeak = gui.locateOnScreen('Rewards/images/sneakpeak.png', region=(1317, 873, 510, 135))
        #     if sneakpeak is not None:
        #         break
        #     gui.click(1758, 951)
        #     gui.moveTo(1832, 951)
        #     sleep(.1 + s.speed)
        # else:
        #     # Click the back to daily set button
        #     gui.click(211, 967)
        while True:
            promotionBanner = gui.locateOnScreen("Rewards/images/closepromotionBanner.png", region=(1697, 889, 120, 122))
            if promotionBanner is not None:
                gui.click(promotionBanner)
                sleep(0.5+s.speed)
            else:
                break

    def getStartingPoints(self):
        img = np.array(gui.screenshot(region=(220, 433, 193, 68)))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # type: ignore
        self.startingPoints = pytesseract.image_to_string(img).strip()
        print(self.startingPoints)

    def runInitialize(self):
        self.openEdge(s.edgePath, s.rewardsUrl)
        self.loadWindow(8)
        sleep(2+s.speed)
        self.dismissPopups()
        self.getStartingPoints()

    


if __name__ == "__main__":
    setupClass = Initialize()
    setupClass.runInitialize()
