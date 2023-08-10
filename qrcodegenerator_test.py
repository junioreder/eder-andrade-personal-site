import os

def test_if_qrcode_file_is_successfully_created():
	assert os.path.exists("./static/images/qrcode.svg")