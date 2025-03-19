import qrcode
import argparse


def generate_qrcode(data, filename):
    qr_code =qrcode.QRCode (
        version=1,
        box_size=10,
        border=4,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    qr_code.add_data(data)
    qr_code.make(fit=True)

    image = qr_code.make_image(fill="black", back_color="white")
    image.save(filename)

    if __name__== "__main__":
        parser = argparse.ArgumentParser(description="Generate a QR code from a given message or URL ")
        parser.add_argument("message", help="The message or url to encofr in the QR code.")
        parser.add_argument("filename", help="The file name to save the QR code image")
        agrs = parser.parse_args()
        generate_qrcode(agrs.message , agrs.filename)