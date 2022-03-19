#for no echo when writing password
from getpass import getpass
from time import sleep

# Function for printing out login screen
def tuiLogin(userName, password):
    top = "Mail Client".center(30) + "\n"
    print("\n"+"\n" + top)
    loginMsg = ("Login to client").center(30) + "\n"
    print(loginMsg)
    
    if userName:
        print("\n"+"Username: " + userName)
    if password:
        pwLength = len(password)
        print("Password: " + "*"*pwLength + "\n") # Hidden password
        #writeMail(userName, password) send til tjek ??

# Function for printing out mail client screen
def tuiWriteMail(sender, receiver, topic, body, attachment, sendMail):
    top = "Mail Client".center(30) + "\n"
    print("\n"+"\n" + top)
    Msg = ("Write mail").center(30) + "\n"
    print(Msg)
    
    if sender:
        print("Sender: \n        " + sender + "\n")
    if receiver:
        print("Reciever: \n        " + receiver + "\n")
    if topic:
        print("Topic:\n        " + topic + "\n")
    if body:
        print("Body:\n        " + body + "\n")
    if attachment:
        print(attachment)
    if sendMail:
        print(sendMail)
        
    #print("\n"+"\n" + top)
    
def doneWriting():
    done = input("Ready to send?  Y/N") # This is meant as a choice for sending the mail

# Mail client for writing email
def writeMail(username, passWord):
    # Initial head
    top = "Mail Client".center(30) + "\n"
    print("\n" + top)
    
    sender = input("Add sender: ")
    tuiWriteMail(sender, receiver=None, topic=None, body=None, attachment=None, sendMail=None)
    receiver = input("Add receiver: ")
    tuiWriteMail(sender, receiver, topic=None, body=None, attachment=None, sendMail=None)
    topic = input("Add topic: ")
    tuiWriteMail(sender, receiver, topic, body=None, attachment=None, sendMail=None)
    body = input("Add body: ")
    tuiWriteMail(sender, receiver, topic, body, attachment=None, sendMail=None)
    attachment = "Add attachment: "
    tuiWriteMail(sender, receiver, topic, body, attachment=None, sendMail=None)
    done = input("Ready to send?  Y/N") # This is meant as a choice for sending the mail
    doneWriting()
    yes = {"Y": True, "y": True, "YES": True, "yes": True}
    no = {"N": False, "n": False, "NO": False, "no": False}
    if done in yes:
        print("done")
        #send_mail(sender, receiver, body, has_attachment=False) + username + passWord
    elif done in no:
        print("not done")
    else:
        #doneWriting()
        print("other")
    
# Initiates login page for mail client
def loginPage():
    # Head of login page
    print("")
    loginMsg = ("Login to client\n").center(30)
    print(loginMsg)
    
    userName = input("Input username: ")
    tuiLogin(userName, password=None)
    
    password = getpass("Input password: ") + "\n"
    tuiLogin(userName, password)
    
    sleep(3) # Wait for effect
    print("waited 3 secs")
    #if secure
        #writeMail(userName, passWord) #start med userName og password ??

# Initial page for secure option, else mail client
def beginClient():
    print("")
    top = "Mail Client".center(30) + "\n"
    print(top)
    
    print("Please choose between: \nSecure server: smtp.gmail.com with TLS\n or \nUnsecure server: dist.bhsi.xyz\n")
    serverSecure = {"Secure", "SECURE", "secure", "sec"}
    serverUnsecure = {"unsecure", "Unsecure", "UNSECURE", "un"}
    serverChoice = input("Choose server [secure/unsecure]: ")
    
    if serverChoice in serverUnsecure:
        writeMail(username=None, passWord=None)
    if serverChoice in serverSecure:
        loginPage()
    else:
        beginClient()

beginClient() ## Run