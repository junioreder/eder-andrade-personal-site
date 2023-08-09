import os
import qrcode
import qrcode.image.svg

img = qrcode.make('https://www.linkedin.com/in/edertech/', image_factory=qrcode.image.svg.SvgImage)

#this should be separ
qrCodePath = './static/images/qrcode.svg'
if not os.path.exists(qrCodePath):
    img.save(qrCodePath)