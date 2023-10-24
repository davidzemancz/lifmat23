import qrcode
import sqlite3

sukl_path = "https://prehledy.sukl.cz/prehled_leciv.html#/detail-reg/"
qrcode_path = {}


con = sqlite3.connect("data.db") 
cur = con.cursor()
cur.execute('SELECT KOD_SUKL from leky')
rows = cur.fetchall()
for row in rows:
    lek = row[0]
    # Create a QR code object with a larger size and higher error correction
    qr = qrcode.QRCode(version=3, box_size=25, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Define the data to be encoded in the QR code
    data = f'{sukl_path}{lek}'

    # Add the data to the QR code object
    qr.add_data(data)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code with a black fill color and white background
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save(f'qrcodes/qr_code_{lek}.png')

    #Save qrcode path to dict
    qrcode_path[lek] = f'qrcodes/qr_code_{lek}.png'