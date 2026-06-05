import qrcode
url="https://www.linkedin.com/in/kavana-yelshetty-770954381/"

img = qrcode.make(url)
img.save("linkdin_qr.png")
print("linkdin qrcode created")