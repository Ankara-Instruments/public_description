# https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

def createQR(urlString, filename):
    # Generate QR code
    url = pyqrcode.create(urlString)
    # Create and save the png file naming "myqr.png"
    url.png(filename, scale = 6)

createQR(urlString= "https://www.ankarainstruments.medogan.com/", filename="AI_www.png")