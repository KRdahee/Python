import qrcode

data = "BEGIN:VCARD" + "\n"
data += "VERSION:3.0" + "\n"
data += "FN:Dahee Lee" + "\n"
data += "TEL;TYPE=WORK;CELL:010 0000 0000" + "\n"
data += "EMAIL;TYPE=WORK:Home Protector lol" + "\n"
data += "URL;TYPE=youtube:https://youtu.be/SIL4kaJD2Cg?\n"
data += "END:VCARD" + "\n"

img = qrcode.make(data)

#img.save('c:/Users/samsung/PythonQR/new/myqrcode.png')

qr = qrcode.QRCode(version = 1, box_size = 10, border = 1)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(back_color=('#FAFAA0'),edge_color=('#FFB914'),center_color=('#FFC31E'))

img.save('c:/Users/samsung/PythonQR/new/Hello Babo.png')
