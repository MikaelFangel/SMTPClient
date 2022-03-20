# for no echo when writing password
from getpass import getpass
import SMTPClient


# Choice for sending the mail
def done_writing():
    done = input("Ready to send?  Y/N   ")
    yes = {"Y", "y", "YES", "yes"}
    no = {"N", "n", "NO", "no"}
    if done in yes:
        return True
    elif done in no:
        return False
    else:
        done_writing()


# Mail client for writing email
def write_mail(username, password, attachment_path=''):
    # Head
    print("\n")
    msg = "Write mail".center(30) + "\n"
    print(msg)

    # Add content
    sender = input("Sender:\n        ")
    receiver = input("\nReceiver:\n        ")
    subject = input("\nSubject:\n        ")
    body = input("\nBody:\n        ")

    email_body = f'FROM:{sender}\n' \
                 f'TO:{receiver}\n' \
                 f'Subject:{subject}\n'

    if attachment_path != '':
        email_body = email_body + f'{SMTPClient.create_image_attachment(body, attachment_path)}\n'

    email_body = email_body + '\n' + SMTPClient.create_make_body_mailable(body)

    if done_writing():
        if username is None or password is None:
            SMTPClient.send_mail(sender, receiver, email_body)
        else:
            SMTPClient.send_secure_mail(username, password, sender, receiver, email_body)

        print("It worked!")  # send_mail(sender, receiver, body, has_attachment=False) + username + passWord
    else:
        write_mail(username, password)


# Login page for mail client
def login_page():
    # Head of login page
    print("\n")
    login_msg = "Client login\n".center(30)
    print(login_msg)

    user_name = input("Input username:\n                ")

    password = getpass("\nInput password:")
    pw_length = len(password)
    print("                " + "*" * pw_length)  # Hidden password

    write_mail(user_name, password)  # check for valid usr + pwd?


# Initial page for secure option, else mail client
def begin_client():
    print("")
    top = "Mail Client".center(30) + "\n"
    print(top)

    print("Please choose between: \nSecure server: smtp.gmail.com with TLS\n or \nUnsecure server: dist.bhsi.xyz\n")
    server_secure = {"Secure", "SECURE", "secure", "sec", "s"}
    server_unsecure = {"unsecure", "Unsecure", "UNSECURE", "un", "u"}
    server_choice = input("Choose server [secure/unsecure]: ")

    if server_choice in server_unsecure:
        write_mail(username=None, password=None)
    if server_choice in server_secure:
        login_page()
    else:
        begin_client()


if __name__ == '__main__':
    begin_client()
