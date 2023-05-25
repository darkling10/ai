#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import schedule
import time

def show_name():
    print("my name is swapnil")
    
def play():
    print("i am playing football")
    
def sleep():
    print("i am going to sleep")
    
def work():
    print("i am working")
    
def tournament():
    print("lets play tournament")
    
schedule.every(5).seconds.do(show_name)
schedule.every(1).minutes.do(play)
schedule.every(1).to(2).minutes.do(work)
schedule.every().day.at("00:00").do(sleep)
schedule.every().monday.at("18:50").do(tournament)


while 1:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:





# In[ ]:




