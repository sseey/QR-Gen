import qrcode

img = qrcode.make('https://YOUR_URL')
img.save('qrcode.png')