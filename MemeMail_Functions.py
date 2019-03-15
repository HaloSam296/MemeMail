def get_meme():
    from NamesAndImagesLists import image_list
    ran_meme = ran.randint(1,9) 
    meme = image_list[ran_meme]
    print(meme, '\n')

def get_email():
    from NamesAndImagesLists import email_list
    ran_email = ran.randint(1, 6) 
    email = email_list[ran_email]



def download_meme():
    #this is for downloading a meme online and assigning it a name
    try:
        memenumgen = ran.randint(1,10001)
        memenumgen_to_str = str(memenumgen)
        print("...\n")
        #for png:
        #urllib.request.urlretrieve('', 'meme-' + memenumgen_to_str + ".png")
        #for jpg:
        #urllib.request.urlretrieve('' + memenumgen_to_str + ".jpg")
    except:
        print(":( \n")



def MakeAndSendMemeMail():
    import smtplib
    import urllib.request
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import os.path
    import random as ran
    from NamesAndImagesLists import image_list
    from NamesAndImagesLists import email_list



    #the next part of the code picks the meme from the selection
    ran_meme = ran.randint(1,9)
    meme = image_list[ran_meme]
    print(meme, '\n')

    #this part picks the email for the meme to be sent to   
    ran_email = ran.randint(1, 6)  
    email = email_list[ran_email]


    print('Starting\n')

    sender = 'example@email.sam'
    password = 'password'
    send_to_email = email 



    subject = "You've got mememail"
    message = ""
    #file_location = [specific meme]

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    attachment = open(meme, "rb")
    
    
    #this part converts the image into base64 so it can be sent with the email
    #This bit of code is an algamation of code from online, it is not entirely credited towards me.
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % meme)
    msg.attach(part)

    

    print('Email Fully Built\n')
    print('Email is being sent to ', send_to_email, ' ')



    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, send_to_email, text)
        server.quit()
        print('Success...?')
    except:
        print('Failed to either connect to server or to send the email')



