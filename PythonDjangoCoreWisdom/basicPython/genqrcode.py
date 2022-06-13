import qrcode
img = qrcode.make('https://www.controldata.co.th/mpsicc')
type(img)  # qrcode.image.pil.PilImage
img.save("myqrcode.png")