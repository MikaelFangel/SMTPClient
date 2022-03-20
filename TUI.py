#for no echo when writing password
from getpass import getpass
from time import sleep
import SMTPClient


# Choice for sending the mail
def doneWriting():
    done = input("Ready to send?  Y/N   ")
    yes = {"Y", "y", "YES", "yes"}
    no = {"N", "n", "NO", "no"}
    if done in yes:
        return True
    elif done in no:
        return False
    else:
        doneWriting()


# Mail client for writing email
def writeMail(username, passWord):
    # Head
    print("\n")
    Msg = "Write mail".center(30) + "\n"
    print(Msg)
    
    # Add content
    sender = input("Sender:\n        ")
    receiver = input("\nReceiver:\n        ")
    topic = input("\nTopic:\n        ")
    body = input("\nBody:\n        ")
    
    attachment = "\nAdd attachment:\n        "
    print(attachment)
    
    if doneWriting():
        if username is None or passWord is None:
            SMTPClient.send_mail(sender, receiver, body)
        else:
            SMTPClient.send_secure_mail(username, passWord, sender,receiver,body)

        print("It worked!")#send_mail(sender, receiver, body, has_attachment=False) + username + passWord
    else:
        writeMail(username, passWord)
        
        
# Login page for mail client
def loginPage():
    # Head of login page
    print("\n")
    loginMsg = "Client login\n".center(30)
    print(loginMsg)
    
    userName = input("Input username:\n                ")
    
    password = getpass("\nInput password:")
    pwLength = len(password)
    print("                " + "*"*pwLength) # Hidden password
    
    sleep(1) # Pause for effect
    writeMail(userName, password) # check for valid usr + pwd?

# Initial page for secure option, else mail client
def beginClient():
    print("")
    top = "Mail Client".center(30) + "\n"
    print(top)
    
    print("Please choose between: \nSecure server: smtp.gmail.com with TLS\n or \nUnsecure server: dist.bhsi.xyz\n")
    serverSecure = {"Secure", "SECURE", "secure", "sec", "s"}
    serverUnsecure = {"unsecure", "Unsecure", "UNSECURE", "un", "u"}
    serverChoice = input("Choose server [secure/unsecure]: ")
    
    if serverChoice in serverUnsecure:
        sleep(1)
        writeMail(username=None, passWord=None)
    if serverChoice in serverSecure:
        sleep(1)
        loginPage()
    else:
        beginClient()


if __name__ == '__main__':
    beginClient() ## Run
