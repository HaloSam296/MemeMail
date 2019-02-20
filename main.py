import time as T
import random as R
from MemeMail_Functions import MakeAndSendMemeMail



wait_time = R.radint(60, 3600)
#wait_time = 10


while True:

    MakeAndSendMemeMail()

    T.sleep(wait_time)
