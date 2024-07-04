import qrcode

data = 'YES YOU BABOOOOOOOOO'

img = qrcode.make(data)

#img.save('c:/Users/samsung/PythonQR/new/myqrcode.png')

qr = qrcode.QRCode(version = 1, box_size = 10, border = 1)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = '#4BAF4B', back_color = '#006400')
img.save('c:/Users/samsung/PythonQR/new/myqrcode1.png')