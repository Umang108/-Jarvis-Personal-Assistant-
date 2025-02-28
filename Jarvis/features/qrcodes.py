import pyautogui
import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def generate_and_show_qr_code(data):
    filename = "qr_code.png"
    generate_qr_code(data, filename)
    pyautogui.alert(f"A QR code for '{data}' has been generated. Check {filename}.")
