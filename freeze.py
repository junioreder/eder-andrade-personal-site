"""
Generates static files
"""

from flask_frozen import Freezer
from app import app
from qrcodegenerator import generateQRCode

generateQRCode()

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
