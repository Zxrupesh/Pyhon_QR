import os
import qrcode

data = input("Enter the name or link: ")
filename = input("Enter the name for the Qr code file: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit = True)

#create a folder if it doesnot exit and save all QR codes in the same folder
folder_name = input("Enter the name of folder to save: ")
os.makedirs(folder_name,exist_ok=True)

img=qr.make_image(fill_color="black", back_color="white")
img.save(f"{folder_name}/{filename}.png")
