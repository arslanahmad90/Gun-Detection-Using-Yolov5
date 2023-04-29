from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import subprocess


app = QApplication(sys.argv)

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.label.setScaledContents(True)

        self.button = QPushButton("Open Image", self)

        self.setWindowTitle("Image Viewer")
        self.resize(600, 440)

        self.button.clicked.connect(self.open_image)

    def resizeEvent(self, event):
        self.label.setGeometry(0, 0, self.width(), self.height() - 30)
        self.button.move(int(self.width() / 2 - 50), self.height() - 30)

    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
        print(file_name)
        file_name= "\"" +file_name+"\""
        script="python detect.py --source "+file_name+"  --weights last.pt"
        print("script",script)
        subprocess.call(script, shell=True)
        #subprocess.run(["python", "detect.py --source "+file_name+"  --weights last.pt"])
        if file_name:
            pixmap = QPixmap("Temp.png")
            self.label.setPixmap(pixmap)

viewer = ImageViewer()
viewer.show()

sys.exit(app.exec_())