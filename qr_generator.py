import qrcode

def generate_qr():
    link = "https://youtu.be/TMY1g8pAktk?list=RDTMY1g8pAktk"
    img = qrcode.make(link)
    img.save("my_qrcode.png")
    img.show()
    print("QR Code generated and displayed")

generate_qr()
