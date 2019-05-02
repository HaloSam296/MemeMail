
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
    import quantumrandom as Qran                #quantumrandom is like random, but it uses a newer method to get better random 
    import smtplib                              #number. It's called quantumrandom because it uses newer quantum computer
    from email.mime.text import MIMEText        #technology.
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import os.path
    import time as T
    from NamesAndImagesLists import image_list
    from NamesAndImagesLists import email_list
    
    start_time = T.time() #The timer starts here

    #the program picks the meme with this
    ran_meme = round(Qran.randint(1,9))
    meme = image_list[ran_meme]
    print(meme, '\n')


    #this program picks the email to send to
    ran_email = round(Qran.randint(1, 6))      
    email = email_list[ran_email]

    
    #for the two parts that randomly get the meme and email, be sure to set the number after Qran.randint. The second number
    #should be the amount you have. I.e., if I have 3 memes and 2 emails it should look like this:
    #    ran_meme = round(Qran.randint(1,3))
    #    ran_email = round(Qran.randint(1, 2))   

    print('Starting\n')

    #This is for setting up the email in the code. Look at the readme for the guide on what settings you have to change
    #in the email
    sender = 'example@gmail.com'
    password = 'password'
    send_to_email = email 

    #This is where you set the subject and text of the email
    subject = "You've got MemeMail"
    message = ""


    #This is the program taking the parameters we've set previously in the script and formatting them to be an email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = send_to_email
    msg['Subject'] = subject
    
    #This is converting the image into something that can be sent via email
    msg.attach(MIMEText(message, 'plain'))
    attachment = open(meme, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % meme)
    msg.attach(part)
    
    
    print('Email Fully Built\n')
    print('Email is being sent to ', send_to_email, ' ')
    
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)        #This part is the program connecting to the server and 
        server.starttls()                                   #attempting to send the email
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, send_to_email, text)
        server.quit()
        print('Success...?')
    except:
        print('Failed to either connect to server or to send the email')
        
    end_time = T.time() #The end of the timer
    
    print("Ending Program\n", "Finished in", end_time - start_time, "seconds.\n")   #Final message stating completion
                                                                                    #and how long it took



