import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QDialog, QLineEdit, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
import sys

app = QApplication(sys.argv)

class SignupDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Username: "))
        layout.addWidget(self.username)
        layout.addWidget(QLabel("Password: "))
        layout.addWidget(self.password)
        self.setLayout(layout)

        self.setWindowTitle("Sign Up")
        self.resize(200, 100)

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.label.setScaledContents(True)

        self.open_image_button = QPushButton("Open Image", self)
        self.signup_button = QPushButton("Sign Up", self)

        self.setWindowTitle("Image Viewer")
        self.resize(400, 340)

        self.open_image_button.clicked.connect(self.open_image)
        self.signup_button.clicked.connect(self.show_signup)

    def resizeEvent(self, event):
        self.label.setGeometry(0, 0, self.width(), self.height() - 30)
        self.open_image_button.move(int(self.width() / 3 - 50), self.height() - 30)
        self.signup_button.move(int(2 * self.width() / 3 - 50), self.height() - 30)
        
    def open_image(self):
        if self.signup_dialog.username.text() == "admin" and self.signup_dialog.password.text() == "admin":
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
            file_name= "\"" +file_name+"\""
            script="python detect.py --source "+file_name+"  --weights last.pt"
            print("script",script)
            subprocess.call(script, shell=True)
            if file_name:
                pixmap = QPixmap("Temp.png")
                self.label.setPixmap(pixmap)
        else:
            QMessageBox.warning(self, "Sign Up", "Incorrect username or password.")

    def show_signup(self):
        self.signup_dialog.exec_()

viewer = ImageViewer()
viewer.signup_dialog = SignupDialog()
viewer.show()

sys.exit(app.exec_())
