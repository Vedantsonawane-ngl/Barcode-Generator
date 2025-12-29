import qrcode
url = input("Enter your URL - ").strip()
file_path = "Desktop\\Desktopqrcode.png"


qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("Ur QRCODE is generated !!")