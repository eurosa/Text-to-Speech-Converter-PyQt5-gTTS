import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QRadioButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from gtts import gTTS


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 600, 400)
        self.setWindowTitle('Text to Speech Converter')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(self.size())

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)

        hBox1 = QHBoxLayout()
        hBox2 = QHBoxLayout()
        vBox1 = QVBoxLayout()
        vBox2 = QVBoxLayout()

        self.image = QLabel()
        self.image.setPixmap(QPixmap('image.jpg'))
        self.image.setAlignment(Qt.AlignHCenter)

        self.label = QLabel("Enter your text: ")
        self.label.setAlignment(Qt.AlignHCenter)

        self.textBox = QLineEdit()
        self.textBox.move(300, 300)

        self.btn1 = QPushButton('Clear')
        self.btn2 = QPushButton('Convert')

        self.lang_label = QLabel('Select Language (Accent)')
        self.rb1 = QRadioButton('English')
        self.rb2 = QRadioButton('Bangla')

        hBox1.addWidget(self.rb1)
        hBox1.addWidget(self.rb2)
        hBox1.setAlignment(Qt.AlignHCenter)

        vBox2.addWidget(self.lang_label)
        vBox2.addLayout(hBox1)
        vBox2.setAlignment(Qt.AlignHCenter)

        hBox2.addWidget(self.btn1)
        hBox2.addWidget(self.btn2)

        vBox1.addWidget(self.image)
        vBox1.addStretch()
        vBox1.addWidget(self.label)
        vBox1.addWidget(self.textBox)
        vBox1.addLayout(vBox2)
        vBox1.addStretch()
        vBox1.addLayout(hBox2)

        self.setLayout(vBox1)

        self.btn1.clicked.connect(self.btn_click_handler)
        self.btn2.clicked.connect(self.btn_click_handler)

    def btn_click_handler(self):
        sender = self.sender()
        if sender.text() == 'Clear':
            self.textBox.clear()
        else:
            text = self.textBox.text()
            op = 'en'

            if self.rb2.isChecked() == True:
                op = 'bn'

            speech = gTTS(text, op)
            speech.save('speech.mp3')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
