from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import base64


# https://stackoverflow.com/questions/38360758/base64-encoded-image-in-email
# Create MIME message.
def createMIME(imageName=''):
    msg = MIMEMultipart()

    # Add more attachments if needed
    #
    #

    if imageName != '':
        image = MIMEImage(imageToBase64(imageName), _subtype='octet_stream')
        image.add_header('Content-Disposition', 'attachment', filename='image.png')
        msg.attach(image)

    return msg


# Image to Base64 function
def imageToBase64(imagePath):
    with open(imagePath, "rb") as imgFile:
        return base64.b64encode(imgFile.read())


# Remove when merged
print(createMIME("image.png").as_string())


