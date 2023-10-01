# PyQt5
import typing
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap, QFont, QKeySequence, QColor, QRegion, QPainterPath, QBitmap, QPainter
from PyQt5.QtCore import QThread, QRunnable, QThread, QThreadPool, pyqtSignal, QObject, QEvent, Qt, QTimer, QFile, QPropertyAnimation, QMetaObject, QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QComboBox, QDesktopWidget, QLabel, QCheckBox, QFrame, QSlider, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFileDialog, QProgressBar, QSizePolicy, QSpacerItem, QGroupBox, QRadioButton, QButtonGroup, QScrollArea, QScrollArea, QShortcut, QMessageBox, QDialog, QGraphicsDropShadowEffect

# Libraries
import pyautogui as gui
import threading
import sys
import keyboard


# Files
from initialize import Initialize
from search import Searches
import settings as s
import dailySet
import morePromotions
import search
import utils
from errorPage import ErrorPage
from settingsPage import SettingsPage


class RewardsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Fonts
        self.sans8 = QFont("Product Sans", 8)
        self.sans9 = QFont("Product Sans", 9)
        self.sans12 = QFont("Product Sans", 12)
        self.sans20 = QFont("Product Sans", 20)
        self.nunitoMedium = QFont("Nunito Medium", 9)
        self.nunitoBlack = QFont("Nunito Black", 9)
       

        # Main Layout
        self.mainLayout = QVBoxLayout()        

        # Header
        headerLayout = QHBoxLayout()

        self.welcomeLabel = QPushButton("Auto Rewards")
        self.welcomeLabel.setFont(QFont("Product Sans", 16))
        self.welcomeLabel.setStyleSheet("QPushButton{background-color: none; border: none;}QPushButton:pressed{padding: 0px}")
        self.welcomeLabel.setCursor(Qt.PointingHandCursor)
        #self.welcomeLabel.clicked.connect(self.setPageMain)
        self.welcomeLabel.adjustSize()

        
        # Settings Button
        self.settingsButton = QPushButton(" Settings")
        self.settingsButton.setFont(QFont("Product Sans", 10))
        self.settingsButton.setIcon(QIcon("Rewards/images/Icons/settingsIcon.png"))
        self.settingsButton.setStyleSheet("QPushButton{background-color:#D9D9D9;border:none;border-radius:5px;padding:5px;}QPushButton:hover{background-color:#CACACA;}QPushButton:pressed{background-color:#B5B5B5;}")
        self.settingsButton.setCursor(Qt.PointingHandCursor) # type: ignore
        #self.settingsButton.clicked.connect(self.setPageSettings)



        headerLayout.addWidget(self.welcomeLabel)
        headerLayout.addStretch(1)
        headerLayout.addWidget(self.settingsButton)

        self.mainLayout.addLayout(headerLayout)


        self.divFrame = QFrame()
        self.divFrame.setFrameShape(QFrame.StyledPanel)
        self.divFrame.setStyleSheet('background-color: #DADADA; border: 0 0 0 0; border-radius:5px')
        settingsLayout = QVBoxLayout(self.divFrame)
        self.mainLayout.addWidget(self.divFrame)

        settingsLabelLayout = QHBoxLayout()

        self.settingsIcon = QLabel()
        self.settingsIcon.setPixmap(QPixmap("Rewards/images/icons/settings.png"))
        self.settingsIcon.setAlignment(Qt.AlignTop | Qt.AlignLeft) # type: ignore
        settingsLabelLayout.addWidget(self.settingsIcon)


        self.settingsLabel = QLabel("Settings")
        self.settingsLabel.setFont(QFont("Nunito Black", 9))
        self.settingsLabel.adjustSize()
        settingsLabelLayout.addWidget(self.settingsLabel) 
        settingsLabelLayout.addStretch(1)
        settingsLayout.addLayout(settingsLabelLayout)

        optionsLayout = QHBoxLayout()

        self.randomSearchBox = QCheckBox("Search")
        #self.randomSearchBox.stateChanged.connect(self.randomSearchBoxFunc))
        self.randomSearchBox.setCursor(Qt.PointingHandCursor) # type: ignore
        self.randomSearchBox.setFont(QFont("Nunito Medium", 9))
        self.randomSearchBox.setStyleSheet(
                                "QCheckBox::indicator"
                               "{"
                               "border : 2px solid black;"
                               "width : 15px;"
                               "height : 16px;"
                               "border-radius :9px;"
                               "}"
                               "QCheckBox::indicator::checked"
                                "{"
                                "image: url(Rewards/images/checkboxPressed.png);"
                                "}")
        self.randomSearchBox.setChecked(True)
        optionsLayout.addWidget(self.randomSearchBox)
        

        self.tasksBox = QCheckBox("Tasks")
        #self.tasksBox.stateChanged.connect(self.tasksBoxFunc)
        self.tasksBox.move(200,345)
        self.tasksBox.resize(320,40)
        self.tasksBox.setCursor(Qt.PointingHandCursor) # type: ignore
        self.tasksBox.setFont(QFont("Nunito Medium", 9))
        self.tasksBox.setStyleSheet(
                                "QCheckBox::indicator"
                               "{"
                               "border : 2px solid black;"
                               "width : 15px;"
                               "height : 16px;"
                               "border-radius :9px;"
                               "}"
                               "QCheckBox::indicator::checked"
                                "{"
                                "image: url(Rewards/images/checkboxPressed.png);"
                                "}")
        self.tasksBox.setChecked(True)
        optionsLayout.addStretch()

        optionsLayout.addWidget(self.tasksBox)
      

        self.gameBox = QCheckBox("Game")
        #self.gameBox.stateChanged.connect(self.gameBoxFunc)
        self.gameBox.move(310,345)
        self.gameBox.resize(320,40)
        self.gameBox.setCursor(Qt.PointingHandCursor) # type: ignore
        self.gameBox.setFont(QFont("Nunito Medium", 9))
        self.gameBox.setChecked(False)
        self.gameBox.setStyleSheet(
                                "QCheckBox::indicator"
                               "{"
                               "border : 2px solid black;"
                               "width : 15px;"
                               "height : 16px;"
                               "border-radius :9px;"
                               "}"
                               "QCheckBox::indicator::checked"
                                "{"
                                "image: url(Rewards/images/checkboxPressed.png);"
                                "}")
        optionsLayout.addStretch()
        optionsLayout.addWidget(self.gameBox)
        optionsLayout.setContentsMargins(60, 0, 60, 0)
        settingsLayout.addLayout(optionsLayout)

        speedLayout = QHBoxLayout()

        self.speedText = QLabel()
        self.speedText.setPixmap(QPixmap('Rewards/icons/speed.png'))
        speedLayout.addWidget(self.speedText)

        self.speedSlider = QSlider(Qt.Horizontal) # type: ignore
        self.speedSlider.setMinimumWidth(210)
        self.speedSlider.setRange(0, 200)
        self.speedSlider.setCursor(Qt.PointingHandCursor) # type: ignore
        self.speedSlider.setSingleStep(1)
        self.speedSlider.setPageStep(1)
        self.speedSlider.setTickInterval(100)
        self.speedSlider.move(130, 384)
        self.speedSlider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 10px;
                border-radius: 5px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #bbb, stop:1 #ccc);
            }
            QSlider::handle:horizontal {
                width: 20px;
                margin: -8px 0 -8px 0;
                border-radius: 5px;
                background-color: #49c3ff;
            }
            QSlider::handle:horizontal:hover {
                background-color: #49b6ff;
            }
            QSlider::handle:horizontal:pressed {
                background-color: #49aaff;
                border-radius: 7px;
            }
            QSlider::groove:horizontal:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #b0b0b0, stop:1 #bbb);
            }
        """)

        self.animation = QPropertyAnimation(self.speedSlider, b"palette")
        self.animation.setDuration(200)
        self.animation.setStartValue(self.speedSlider.palette())
        self.animation.setEndValue(QColor("#aaa"))

        speedLayout.addWidget(self.speedSlider)

        # Set the initial value and connect the signal to the slot
        self.speedSlider.setValue(0)
        #self.speedSlider.valueChanged.connect(self.sliderChange)


        self.speedLabel = QLineEdit("0")
        self.speedLabel.move(355, 389)
        self.speedLabel.setFixedSize(40,20)
        self.speedLabel.setAlignment(Qt.AlignCenter) # type: ignore
        self.speedLabel.setStyleSheet("background-color:#C3C3C3; border-radius: 3px;")
        #self.speedLabel.textChanged.connect(self.textChange)
        self.speedLabel.setMaxLength(4)
        speedLayout.addWidget(self.speedLabel)
        settingsLayout.addLayout(speedLayout)


        startLayout = QHBoxLayout()

        self.startButton = QPushButton("Start")
        self.startButton.setCursor(Qt.PointingHandCursor) # type: ignore
        self.startButton.setFont(self.sans12)
        self.startButton.setFixedHeight(70)
        self.startButton.setObjectName("startButton")
        self.startButton.setStyleSheet("QPushButton::hover{background-color: #1ABCE3;}QPushButton{background-color: #91b8f8; color: white; border-radius: 6px; font-weight: bold;}QPushButton::pressed{background-color: #189BBB;}")
        #self.startButton.clicked.connect(self.startThread)

        self.dropdownBackground = QFrame()
        self.dropdownBackground.setFrameShape(QFrame.StyledPanel)
        self.dropdownBackground.setStyleSheet('background-color: #DADADA; border: 0 0 0 0; border-radius:5px')
        self.dropdownBackground.setFixedHeight(70)

        self.taskIcon = QLabel("")
        self.taskIcon.setPixmap(QPixmap("Rewards/images/icons/task.png"))
        self.taskLabel = QLabel("Task")
        self.taskLabel.setFont(QFont("Nunito Black", 9))
        self.taskLabel.adjustSize()


        self.dropDownMenu = QComboBox()
        self.dropDownMenu.addItems(['All', 'Bing Quiz', 'This or That', 'Supersonic Quiz', 'Turbocharge Quiz', 'Warpspeed Quiz'])
        self.dropDownMenu.setFont(self.sans8)
        self.dropDownMenu.setCursor(Qt.PointingHandCursor) # type: ignore
        #self.dropDownMenu.currentTextChanged.connect(self.grayOutSettings)
        self.dropDownMenu.setStyleSheet('''
            QComboBox {
                background-color: #dadada;
                border-radius: 5px;
                padding: 5px;
                min-width: 100px;
                padding-left: 8px;
            }
            QComboBox::hover {
                background-color: #D0D0D0;
            }
            QComboBox::drop-down {
                border: none;
                background-color: transparent;
                
            }
            QComboBox::down-arrow {
                image: url(Rewards/images/icons/expand.png);
                width: 25px;
                height: 25px;
                margin-right: 9px;
            }
            QComboBox QAbstractItemView {
                background-color: #f0f0f0;
                border-radius: 5px;
                selection-background-color: #1ABCE3;
            }
        ''')

        dropdownTasksLayout = QHBoxLayout()
        dropdownTasksLayout.addWidget(self.taskIcon)
        dropdownTasksLayout.addWidget(self.taskLabel)
        dropdownTasksLayout.setAlignment(Qt.AlignLeft) # type: ignore

        dropdownLayout = QVBoxLayout()
        dropdownLayout.addLayout(dropdownTasksLayout)
        dropdownLayout.addWidget(self.dropDownMenu)
        dropdownLayout.setContentsMargins(10, 5, 10, 5)
        self.dropdownBackground.setLayout(dropdownLayout)

        startLayout.setContentsMargins(15, 0, 15, 10)
        startLayout.addWidget(self.startButton)
        startLayout.addSpacing(10)
        startLayout.addWidget(self.dropdownBackground)
        self.mainLayout.addStretch(1)
        self.mainLayout.addLayout(startLayout)

        self.setLayout(self.mainLayout)



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Auto Rewards")
        self.setWindowIcon(QIcon(r"Rewards\images\application\RewardsIcon.ico"))
        self.setGeometry(960, 540, 500, 630)
        self.center()
        self.UIComponents()
        self.show()

        keyboard.add_hotkey(s.quitHotkey, QApplication.quit, suppress=True)
  


    def UIComponents(self):

        self.rewardsPage = self.initRewardsPage()
        self.setCentralWidget(self.rewardsPage)

    def initRewardsPage(self):
        rewardsPage = RewardsPage()
        rewardsPage.settingsButton.clicked.connect(self.setPageSettings)
        return rewardsPage
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def startThread(self):
        s.initThread = threading.Thread(target=self.start, daemon=True)
        s.initThread.start()


    def start(self):
        Initialize().runInitialize()
        Searches().runSearches()


    def setPageMain(self):
        self.rewardsPage = self.initRewardsPage()
        self.setCentralWidget(self.rewardsPage)

    def setPageSettings(self):
        #if self.settingsPage is None:
        self.settingsPage = SettingsPage()
        self.settingsPage.backButton.clicked.connect(self.setPageMain)
        self.setCentralWidget(self.settingsPage)

    def setPageError(self):
        self.setCentralWidget(ErrorPage())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    window = MainWindow()
    window.show()
    app.exec()