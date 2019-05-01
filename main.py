import time as T
import random as R
from MemeMail_Functions import MakeAndSendMemeMail



wait_time = R.radint(60, 3600)      #This makes it wait between one minutes to an hour (60 means 60 seconds), delete or comment    
                                    #this out to have no delay between the MemeMails


while True:

    MakeAndSendMemeMail()

    T.sleep(wait_time)
