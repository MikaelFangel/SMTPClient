import base64
import ssl
from socket import *

unsecure_server = "dist.bhsi.xyz"
unsecure_port = 2525

secure_server = "smtp.gmail.com"
secure_port = 587


def send_mail(mail_from, mail_to, body, has_attachment=False):
    # SMTP protocol message
    smtp_client_responses = ["EHLO mail.example.com\r\n",
                             "MAIL FROM: <" + mail_from + ">\r\n",
                             "RCPT TO: <" + mail_to + ">\r\n",
                             "DATA\r\n",
                             f"{body}\r\n",
                             ".\r\n",
                             "QUIT\r\n"]
    smtp_server_responses = []

    client_socket = create_socket(unsecure_server, unsecure_port)

    # Send mail
    # TODO Remove the need for checking if i = 4
    for i in range(len(smtp_client_responses)):
        client_socket.send(smtp_client_responses[i].encode())
        if i == 4:
            client_socket.send(smtp_client_responses[i + 1].encode())
        recv = client_socket.recv(2048)


# TODO implement
def send_secure_mail(user_name, password, mail_from, mail_to, body,  has_attachment=False):
    # Converter user name and password to base64
    user_name = base64_string_converter(user_name)
    password = base64_string_converter(password)

    # Array's with protocol responses and answers
    smtp_client_responses = ["EHLO mail.example.com\r\n",
                             "STARTTLS\r\n",
                             "AUTH LOGIN\r\n",
                             user_name + "\r\n", password + "\r\n",
                             "MAIL FROM: <" + mail_from + ">\r\n",
                             "RCPT TO: <" + mail_to + ">\r\n",
                             "DATA\r\n",
                             f"{body}\r\n.\r\n",
                             "QUIT\r\n"]
    smtp_server_responses = []

    client_socket = create_socket(secure_server, secure_port)

    # Prepare for tls
    for i in range(2):
        client_socket.send(smtp_client_responses[i].encode())
        recv = client_socket.recv(2048)

    # Upgrade connection to TLS
    ctx = ssl.create_default_context()
    client_socket = ctx.wrap_socket(client_socket, server_hostname=secure_server)

    # Authenticate and send mail
    for i in range(2, len(smtp_client_responses)):
        client_socket.send(smtp_client_responses[i].encode())
        recv = client_socket.recv(2048)


def create_socket(server, port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server, port))
    recv = client_socket.recv(2048)

    return client_socket


def imageToBase64(imagePath):
    with open(imagePath, "rb") as imgFile:
        return base64.b64encode(imgFile.read())


def base64_string_converter(string):
    string_in_bytes = string.encode('utf-8')
    string_in_base64 = base64.b64encode(string_in_bytes)
    result_as_string = string_in_base64.decode('utf-8')
    return result_as_string

def base64ToString(bytes):
    return bytes.decode('utf-8')

def createImageAttachment(imageName=''):
    imageBase64 = base64ToString(imageToBase64(imageName))
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
