import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data("www.linkedin.com/in/cromwell-samuel-56b27519a")

img = qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.jpg")