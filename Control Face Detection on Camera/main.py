"""
@Project_Description:
    Control the face detection of camera with an app.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import sys
import cv2
import numpy as np
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread


# Class to Reflect Camera Frame to PyQt5 App.
class VideoThread(QThread):

    # Create PyQtSignal Object to Reflection.
    change_pixmap_signal = pyqtSignal(np.ndarray)

    # Initialize Object.
    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.detect_face = False
        self.face_cascade = cv2.CascadeClassifier("XML File/face_recognition.xml")

    # Run the Thread.
    def run(self):

        # Create Camera Object.
        camera = cv2.VideoCapture(0)

        # Check Status of Program.
        while self._run_flag:

            # Read Frame and Status From Camera Object.
            ret, frame = camera.read()

            # Frame Can Read From Camera.
            if ret:

                # Convert Frame to Gray Scale.
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect Faces According to User Choice.
                if self.detect_face:

                    # Detect Faces.
                    faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

                    # Show Count of Faces on Camera.
                    frame = cv2.putText(frame, f"Face Count: {len(faces)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

                    # Draw Rectangle Around Faces.
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Reflect Frame to PyQt5 App.
                self.change_pixmap_signal.emit(frame)

            # Frame Can't Read From Camera.
            else:
                print("Frame Can't Read From Camera...")
                break

            # Terminate Program with ESC.
            if cv2.waitKey(1) & 0xFF == 27:
                break

        # Terminate Camera.
        camera.release()

    # Stop the Thread.
    def stop(self):
        self._run_flag = False
        self.wait()


# Class to Design App and Control Workflow..
class App(QWidget):

    # Initialize App.
    def __init__(self):

        # Initialize Window Settings.
        super().__init__()
        self.setWindowTitle("Face Detection App")
        self.display_width = 960
        self.display_height = 720

        # Create Label to Hold Camera Frame.
        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)

        # Create Text Label.
        self.textLabel = QLabel("")

        # Create a Vertical Box Layout and Add the Two Labels.
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)

        # Set the Vbox Layout as the Widgets Layout.
        self.setLayout(vbox)

        # Create the Video Capture Thread.
        self.thread = VideoThread()

        # Create Checkbox to Control Face Detection of Camera.
        self.activation = QtWidgets.QPushButton("Detect Face", self)
        self.activation.setCheckable(True)
        self.activation.setStyleSheet("QPushButton:checked {color: white; background-color: green;}")
        self.activation.clicked.connect(self.click_box)
        self.activation.move(16, 750)
        self.activation.resize(960, 24)

        # Connect Thread Signal to Update Frame Simultaneously.
        self.thread.change_pixmap_signal.connect(self.update_image)

        # Start the Thread.
        self.thread.start()

    # Stop the Thread.
    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    # Update Frame Simultaneously.
    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    # Convert an OpenCV Image to QPixmap.
    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    # Function to Control Activation Button.
    def click_box(self):
        if self.activation.isChecked():
            self.thread.detect_face = True
        else:
            self.thread.detect_face = False


# Run Program.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
