from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize


class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon(r"Rewards\images\application\RewardsIcon.ico"))
        self.setGeometry(780, 220, 500, 630)
        
       
        self.initUI()

    def initUI(self):
        self.settingsLayout = QVBoxLayout()

        header = QHBoxLayout()

        self.backArrow = QIcon("Rewards/images/icons/backArrow.png")
     

        self.backButton = QPushButton(" Settings")
        self.backButton.setStyleSheet("QPushButton{background-color: none; border: none;}QPushButton:pressed{padding: 0px}")
        self.backButton.setFont(QFont("Product Sans", 16))
        self.backButton.setIcon(QIcon(self.backArrow))
        self.backButton.setCursor(Qt.PointingHandCursor)


        header.addWidget(self.backButton)
        header.addStretch(1)

        self.settingsLayout.addLayout(header)
        self.settingsLayout.setAlignment(header, Qt.AlignTop)


        self.setLayout(self.settingsLayout)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    settingsPage = SettingsPage()
    settingsPage.show()
    sys.exit(app.exec_())