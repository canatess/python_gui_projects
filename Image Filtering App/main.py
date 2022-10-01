"""
@Project_Description:
    Apply different filters on uploaded image.

@Author:
    Can Ali Ates
"""

# Import Libraries.
import sys
import cv2 as cv
import numpy as np
from PyQt5 import QtCore
from AppDesign.design import AppWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox


# Class to Run App.
class App(QMainWindow):

    # Initialize App.
    def __init__(self):
        super(App, self).__init__()
        self.UI = AppWindow(self)
        self.UI.browse_image.clicked.connect(self.browse_image)
        self.UI.original_filter.clicked.connect(self.original_filter)
        self.UI.gray_filter.clicked.connect(self.gray_filter)
        self.UI.sharper_filter.clicked.connect(self.sharper_filter)
        self.UI.blur_filter.clicked.connect(self.blur_filter)
        self.UI.bgr_filter.clicked.connect(self.bgr_filter)
        self.show()

    # Upload Image.
    def browse_image(self):
        self.file = QFileDialog.getOpenFileName(self, "Browse Image", "C:\\Users\\Can\\Desktop", "JPG Files (*.jpg);; PNG Files (*.png);; JPEG Files (*.jpeg)")
        self.pixel_array = cv.imread(self.file[0])

    # Check the Existence of Image to Apply Filters.
    def check_image(self):
        if not hasattr(self, "pixel_array"):
            QMessageBox.question(self, "Warning!", "You Can't Browse Image", QMessageBox.Ok)

    # Convert OpenCV image to QPixmap.
    def image_converter(self, image, gray=False):
        h, w, ch = image.shape
        bytes_per_line = ch * w
        converted_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        if gray:
            converted_image = converted_image.convertToFormat(QImage.Format_Grayscale8)
        image = converted_image.scaled(631, 351, QtCore.Qt.KeepAspectRatio)
        return image

    # Original Filter.
    def original_filter(self):
        self.check_image()
        rgb_pixels = cv.cvtColor(self.pixel_array, cv.COLOR_BGR2RGB)
        rgb_image = self.image_converter(rgb_pixels)
        self.pixmap = QPixmap.fromImage(rgb_image)
        self.UI.image.setPixmap(self.pixmap)

    # Gray Filter.
    def gray_filter(self):
        self.check_image()
        gray_pixels = cv.cvtColor(self.pixel_array, cv.COLOR_BGR2RGB)
        gray_image = self.image_converter(gray_pixels, True)
        self.pixmap = QPixmap(gray_image)
        self.UI.image.setPixmap(self.pixmap)

    # BGR Filter.
    def bgr_filter(self):
        self.check_image()
        bgr_image = self.image_converter(self.pixel_array)
        self.pixmap = QPixmap(bgr_image)
        self.UI.image.setPixmap(self.pixmap)

    # Sharper Filter.
    def sharper_filter(self):
        self.check_image()
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        rgb_pixels = cv.cvtColor(self.pixel_array, cv.COLOR_BGR2RGB)
        sharp_pixels = cv.filter2D(rgb_pixels, -1, kernel)
        sharp_image = self.image_converter(sharp_pixels)
        self.pixmap = QPixmap(sharp_image)
        self.UI.image.setPixmap(self.pixmap)

    # Blur Filter.
    def blur_filter(self):
        self.check_image()
        rgb_pixels = cv.cvtColor(self.pixel_array, cv.COLOR_BGR2RGB)
        blurred_pixels = cv.GaussianBlur(rgb_pixels, (15, 15), 0)
        blurred_image = self.image_converter(blurred_pixels)
        self.pixmap = QPixmap(blurred_image)
        self.UI.image.setPixmap(self.pixmap)


# Run Program.
if __name__ == "__main__":
    app_widget = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(app_widget.exec_())
