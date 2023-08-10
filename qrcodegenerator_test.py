import os
from qrcodegenerator import generateQRCode

QR_CODE_IMAGE_PATH = './static/images/qrcode.svg'

if os.path.exists(QR_CODE_IMAGE_PATH):
	os.remove(QR_CODE_IMAGE_PATH)

def test_if_qrcode_file_is_successfully_created():
	generateQRCode()
	assert os.path.exists(QR_CODE_IMAGE_PATH)