# MemeMail
A Python3 program that will pick a random meme and email out of a list and send the meme to the email. Not only that, but it will repeat this process at anytime between one minute and one hour (it's the best kind of spam bot, it's a meme spam bot).

The bulk of the code is in MemeMail_Functions. Main.py is the file to execute the program, and it is its own seperate file to keep the execution clean and simple. Plus whenever you want to remeove the wait time you don't have to add or remove a ton of indentions (like I had to before I had two seperate files of the code).
  



Setup:

Most of the functions used should be built into Python, but you have to install quantumrandom (pip install quantumrandom)
and you might need to install smtplib (pip install stmplib)

For the email (it is recommended to create a new account for this), I use an account from Google. If you also use one, first make the email or login to an existing one that you plan to use for this script, go to https://myaccount.google.com/security (or the security tab for your account), find "Less Secure App Access" and set that to on. Just a warning, I haven't purposely put any secuity flaws in this program, but I also haven't made many efforts to keep this very secure, be careful with who you send the emails to if you use a personal account.
                                                         
