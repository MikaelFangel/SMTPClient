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
        print(recv)


# TODO implement
def send_secure_mail(user_name, password, has_attachment=False):
    # Array's with protocol responses and answers
    smtp_client_responses = ["EHLO mail.example.com\r\n",
                             "STARTTLS\r\n",
                             "AUTH LOGIN\r\n",
                             user_name + "\r\n", password + "\r\n"]
    smtp_server_responses = []

    client_socket = create_socket(secure_server, secure_port)

    # Prepare for tls
    for i in range(2):
        client_socket.send(smtp_client_responses[i].encode())
        recv = client_socket.recv(2048)
        print(recv)

    # Upgrade connection to TLS
    ctx = ssl.create_default_context()
    client_socket = ctx.wrap_socket(client_socket, server_hostname=secure_server)

    # Authenticate and send mail
    for i in range(2, len(smtp_client_responses)):
        client_socket.send(smtp_client_responses[i].encode())
        recv = client_socket.recv(2048)
        print(recv)


def create_socket(server, port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server, port))
    recv = client_socket.recv(2048)
    print(recv)

    return client_socket


if __name__ == '__main__':
    pass
