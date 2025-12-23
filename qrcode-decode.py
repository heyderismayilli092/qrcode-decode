from PIL import Image
from pyzbar.pyzbar import decode
import cv2
import sys
import datetime
import mimetypes

# control
if len(sys.argv) < 2:
  print("Select QR code image !")
  sys.exit(1)
imagefile = sys.argv[1]
mime_type = mimetypes.guess_type(imagefile)[0]  # get selected file mimetype
if mime_type != "image/png" and mime_type != "image/jpeg":
  print("Please insert the correct image file!")
  sys.exit(1)
  
image = cv2.imread(imagefile)  # read selected image file
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert grayscale format
pil_image = Image.fromarray(image_rgb)

# scanning QR codes in screenshot photo
qr_codes = decode(pil_image)

# finding the content of the QR code and writing it on the screen
getdate = datetime.datetime.now().strftime("%d-%m-%Y__%H:%M:%S")
for qr_code in qr_codes:
    qr_data = qr_code.data.decode('utf-8')
    print(f"QR Code content: {qr_data}")
    qrdata_file = open("qrcode_data_"+getdate+".txt", "w")
    qrdata_file.write(qr_data)
    qrdata_file.close()

if not qr_codes:
    print("No QR code found")
