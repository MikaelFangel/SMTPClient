import base64


# https://stackoverflow.com/questions/38360758/base64-encoded-image-in-email
# Create image attachment part to the message
def createImageAttachment(imageName=''):
    imageBase64 = imageToBase64(imageName) # please convert this with Emil's part
    msg = f'Content-Type: multipart/mixed; boundary="===============0814515963129319972=="\n' \
          f'MIME-Version: 1.0\n' \
          f'\n' \
          f'--===============0814515963129319972==\n' \
          f'Content-Type: image/octet_stream\n' \
          f'MIME-Version: 1.0\n' \
          f'Content-Transfer-Encoding: base64\n' \
          f'Content-Disposition: attachment; filename="{imageName}"\n' \
          '\n' \
          f'{imageBase64}==\n' \
          '\n' \
          '--===============0814515963129319972==--' \

    return msg


# Image to Base64 function
def imageToBase64(imagePath):
    with open(imagePath, "rb") as imgFile:
        return base64.b64encode(imgFile.read())


# Remove when merged
print(createImageAttachment("image.png"))



# Content-Type: multipart/mixed; boundary="===============0814515963129319972=="
# MIME-Version: 1.0
#
# --===============0814515963129319972==
# Content-Type: image/octet_stream
# MIME-Version: 1.0
# Content-Transfer-Encoding: base64
# Content-Disposition: attachment; filename="image.png"
#
# aVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQUFvQUFBQUxDQUlBQUFESkRJdFBBQUFBQVhOU1IwSUFy
# czRjNlFBQUFBUm5RVTFCQUFDeGp3djhZUVVBQUFBSmNFaFpjd0FBRW5RQUFCSjBBZDVtSDNnQUFB
# QW9TVVJCVkNoVFkvaVBGd3dhNlJVclZyUzJ0a0k1WUlBaURaUmpZRUFSb2FMZG1BQ3Y5UC8vQVBR
# a1FlaXdod1loQUFBQUFFbEZUa1N1UW1DQw==
#
# --===============0814515963129319972==--
