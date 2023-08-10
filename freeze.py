"""
Generates static files
"""

from flask_frozen import Freezer
from app import app
import qrcodegenerator # pylint: disable=unused-import

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
