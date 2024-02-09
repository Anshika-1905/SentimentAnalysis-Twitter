#imports every exposed object in Tkinter into your current namespace
import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import simpledialog
# pyplot as plt gives an unfamiliar reader a hint that pyplot is a module, rather than a function 
#which could be incorrectly assumed from the first form.
import matplotlib.pyplot as plt
#when you call the statement import numpy as np , you are shortening the phrase "numpy" to "np" 
#to make your code easier to read.
import numpy as np
#Importing pandas means bringing all of the pandas functionality to your finger tips in your python script or jupyter notebook
import pandas as pd
from PIL import Image
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from tweepy import *
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
import tweepy

import tweepy as tw


# he os module is a part of the standard library, or stdlib, within Python 3. This means that it comes with your Python installation,
#but you still must import it. 
import os
#stanadard string
fields = 'Enter Name','Enter Tweet'
#arraylist initialization
tweets = []
specific_tweets = []
posWords = []
negWords = []
#counters initializations
level1_posTweets = 0
level1_negTweets = 0
level1_mixTweets = 0

#frequencies intializations
posPosCount = 0
posNegCount = 0
negNegCount = 0
negPosCount = 0

ROOT_DIR = "C:/Users/Radhika/Desktop/project_sentiment/"

# positive and negetive dictionaries paths
posPath = os.path.join(ROOT_DIR,"poswords.txt")
negPath = os.path.join(ROOT_DIR,"negwords_test.txt")

#fucation to be called when "upload" button clicks
ftweet = []
def fetch(entries):    
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 
        ftweet.append("%s" %(text))
        #print('next')
        #print(entry[0].get())
        #tweet = entry[0]+": "+entry[1]+"\r\n"
        #file = open(os.path.join(ROOT_DIR,"tweets_final.txt"), "a+") 
        #file.write(tweet) 
        #file.close() 
        #print('end')
    #framing standard tweet format to update in the tweets file
    tweettoupdate = "\r\n"+ftweet[0]+": "+ftweet[1]
    print(tweettoupdate)
    #open whole tweets file to update the current entered tweet with name(tag)
    file = open(os.path.join(ROOT_DIR,"tweets_final.txt"), "a+") 
    file.write(tweettoupdate)
    file.close()
#funtion to be called when "load" buttion clicked        
def loadTweets():
    print('loading tweets')
    file_name= fd.askopenfilename() 
    print(file_name)   
    #note pad with the tweet contents will be opened
    os.system("notepad.exe "+file_name)
    print(file_name)
    #reading all the tweets line by line and appending to tweets list
    with open(file_name, encoding="utf8") as file:        
        for line in file:            
            tweets.append(line.strip())
    #loading of pos and neg words
    #print(tweets[0])
    with open(posPath, encoding="utf8") as file1:        
        for line1 in file1:
            #print('inside')
            posWords.append(line1.strip())    
    #print(posWords[0])
    with open(negPath, encoding="utf8") as file2:
        #print('outside')
        for line2 in file2:
            #print('inside')
            negWords.append(line2.strip())
    print(tweets[0])        
    print(posWords[0])
    print(negWords[0])
    
#the function called when "show tweets" button clicked     
def showTweets():
    #loop to print all the tweets from tweets list
    print(ROOT_DIR)
    path = "python "+ROOT_DIR+"/display_tweets.py 1"
    #path = os.path.join("python ",ROOT_DIR,"/display_tweets.py 1")
    print(path)
    subprocess.call(path, shell=True)
    #subprocess.call("python D:/myproject/sentimental_stress_analisys/display_tweets.py 1", shell=True)
    
def showEmojis():
    print('showing emojis')
    path = os.path.join(ROOT_DIR,"images/main.png")
    img11 = Image.open(path)
    img11.show()


def processTweets():
    global level1_posTweets
    global level1_negTweets
    global level1_mixTweets
    print('process started')
    #dialog box to retrieve the name on which tweets to be processed and filters the relevent tweets
    name = simpledialog.askstring("Input name", "Enter name to process the stress",
                                parent=root)
    print(name)
    #if tweet contains name then tweets will be filtered
    specific_tweets.clear()
    for tweet in tweets:
        if name in tweet:
            specific_tweets.append(tweet)           
    print(specific_tweets)        
    #for pos coount
    for tweet1 in specific_tweets:
        #tokens the tweet with space to avoid duplicate comparisions(ex: good and goodness)
        tokens1 = tweet1.split(" ")
        for posWord in posWords:
            #print(posWord)
            if(posWord in tokens1):
                #print('matched')
                level1_posTweets = level1_posTweets+1
                #print(level1_posTweets)

    #for neg count
    for tweet2 in specific_tweets:
        tokens2 = tweet2.split(" ")
        for negWord in negWords:
            if(negWord in tokens2):
                level1_negTweets = level1_negTweets+1

    print(level1_posTweets)
    print(level1_negTweets)
    #first level plotting
    #y = np.array([level1_posTweets, level1_negTweets])
    #mylabels = ["Positive tweets", "Negetive tweets"]

    #plt.pie(y, labels = mylabels)
    #plt.legend(title = "Sentimental analysis first level:")
    #plt.show() 
    
    Data = {'Types_1': ['Positive tweets','Negetive tweets'],
        'Counts': [level1_posTweets,level1_negTweets]
       }
    df = pd.DataFrame(Data,columns=['Types_1','Counts'])

    New_Colors = ['green','blue']
    plt.bar(df['Types_1'], df['Counts'], color=New_Colors)
    plt.title('Sentimental analysis(level1)', fontsize=14)
    plt.xlabel('Type Of Tweets', fontsize=14)
    plt.ylabel('Counts', fontsize=14)
    plt.grid(True)
    plt.show()
    
    for tweet3 in specific_tweets:
        tokens3 = tweet3.split(" ")
        for posWord in posWords:
            for negWord in negWords:
                if (posWord in tokens3) and (negWord in tokens3):
                    level1_mixTweets = level1_mixTweets+ 1
    print(level1_mixTweets)                
    #y1 = np.array([level1_posTweets, level1_negTweets,level1_mixTweets])
    #mylabels1 = ["Positive tweets", "Negetive tweets","Mixed tweets"]
    #plt.pie(y1, labels = mylabels1)
    #plt.legend(title = "Sentimental analysis second level:")
    #plt.show()
    Data = {'Types_1': ['Positive tweets','Negetive tweets','Mixed tweets'],
        'Counts': [level1_posTweets,level1_negTweets,level1_mixTweets]
       }
    df = pd.DataFrame(Data,columns=['Types_1','Counts'])

    New_Colors = ['green','blue','cyan']
    plt.bar(df['Types_1'], df['Counts'], color=New_Colors)
    plt.title('Sentimental analysis(level2)', fontsize=14)
    plt.xlabel('Type Of Tweets', fontsize=14)
    plt.ylabel('Counts', fontsize=14)
    plt.grid(True)
    plt.show()
    
    
def analytics():
    print("analytics started")
    global posPosCount
    global posNegCount
    global negNegCount
    global negPosCount
    global reltweetcount
    global posaccuracy
    global negaccuracy
    for tweet1 in specific_tweets:
        
        tokens1 = tweet1.split(" ")
        for posWordOuter in posWords:
            for posWordInner in posWords:
                if (posWordOuter in tokens1) and (posWordInner in tokens1):
                    posPosCount = posPosCount + 1
    print(posPosCount)     
    for tweet1 in specific_tweets:
        tokens1 = tweet1.split(" ")
        for posWordOuter in posWords:
            for negWordInner in negWords:
                if (posWordOuter in tokens1) and (negWordInner in tokens1):
                    posNegCount = posNegCount + 1
    print(posNegCount)  
    for tweet1 in specific_tweets:
        tokens1 = tweet1.split(" ")
        for negWordOuter in negWords:
            for negWordInner in negWords:
                if (negWordOuter in tokens1) and (negWordInner in tokens1):
                    negNegCount = negNegCount + 1
    print(negNegCount) 
    for tweet1 in specific_tweets:
        tokens1 = tweet1.split(" ")
        for negWordOuter in negWords:
            for posWordInner in posWords:
                if (negWordOuter in tokens1) and (posWordInner in tokens1):
                    negPosCount = negPosCount + 1
    print(negPosCount) 
    Data = {'Types_1': ['++ tweets','+- tweets','-- tweets','-+ tweets'],
        'Counts': [posPosCount,posNegCount,negNegCount,negPosCount]
       }
    df = pd.DataFrame(Data,columns=['Types_1','Counts'])

    New_Colors = ['green','blue','cyan','magenta']
    plt.bar(df['Types_1'], df['Counts'], color=New_Colors)
    plt.title('Sentimental analysis(level3)', fontsize=14)
    plt.xlabel('Type Of Tweets', fontsize=14)
    plt.ylabel('Counts', fontsize=14)
    plt.grid(True)
    plt.show()
    reltweetcount = len(specific_tweets)
    finalPos = posPosCount + posNegCount
    finalNeg = negNegCount + negPosCount
    posaccuracy = ( finalPos / reltweetcount )*10
    negaccuracy = ( finalNeg / reltweetcount )*10
    print("______");
    print(reltweetcount)
    print(posaccuracy)
    
    print(negaccuracy)
    y = np.array([posaccuracy, negaccuracy])
    mylabels = ["Positive:"+str(posaccuracy), "Negetive:"+str(negaccuracy)]

    plt.pie(y, labels = mylabels)
    plt.legend(title = "accuracies:")
    plt.show() 
    
    if finalPos > finalNeg:
        print("stress based")
        msg = MIMEMultipart()
        message = "You stressed and please call me at help line numener 045128903"
        password = "College@project1"
        msg['From'] = "twitterstresshelpline@gmail.com"
        msg['To'] = "twitterstresshelpline@gmail.com"
        msg['Subject'] = "<<sentimental strees analytics>>" 
        msg.attach(MIMEText(message, 'plain')) 
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls() 
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string()) 
        server.quit() 
        print ("successfully sent email to %s:" % (msg['To']))
        
         
def twitterConn():
    consumer_key = 'UspPzyTqUh8dg8I00ID4v44Hl'
    consumer_secret = '62iz4FpDrjdlDrVimOwY3d3QvffoswYWyCcGvQE4hhJ25YuGs2'
    access_key= '715790506844950528-yAU2kPnakcH1uSQHLVuqHZuqY2gsR9a'
    access_secret = '1Jd25ymaarWIR1j5sdK2nzRMh02Hyo3UkhJgMlXjH47fZ'
 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
 
    api = tweepy.API(auth,wait_on_rate_limit=True)
 
    csvFile = open('file-name', 'a')
    csvWriter = csv.writer(csvFile)
 
    search_words = "#stress"      # enter your words
    new_search = search_words + " -filter:retweets"
 
    for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
         print(tweet.text)
         file = open(os.path.join(ROOT_DIR,"tweets_final.txt"), "a+",encoding="utf-8") 
         file.write(tweet.text)
         file.write("\n")
         file.close()

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


#is used to execute some code only if the file was run directly, and not imported.
if _name_ == '_main_':
    #To initialize tkinter, we have to create a Tk root widget, which is a window with a title bar and other decoration provided by the window manager.
    root = tk.Tk()
    #This means that the string cannot be seen in its entirety
    ents = makeform(root, fields)    
    #The handler for an event binding is called with one parameter, the event itself. The e=ents in both lambdas, while technically a parameter,
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='UPLOAD',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    #This is a common pitfall with declaring a lambda in a loop. The variable i is evaluated when the lambda is called, not when it is defined, ...
    b2 = tk.Button(root, text='LOAD', command=(lambda e=ents: loadTweets()))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    
    b3 = tk.Button(root, text='EMOJIS', command=(lambda e=ents: showEmojis()))
    b3.pack(side=tk.LEFT, padx=6, pady=6)
    
    b4 = tk.Button(root, text='SHOW TWEETS', command=(lambda e=ents: showTweets()))
    b4.pack(side=tk.LEFT, padx=5, pady=5)
    #root.mainloop()
    
    b5 = tk.Button(root, text='PROCESS TWEETS', command=(lambda e=ents: processTweets()))
    b5.pack(side=tk.LEFT, padx=5, pady=5)
    #root.mainloop()
    
    b6 = tk.Button(root, text='FINAL ANALYTICS', command=(lambda e=ents: analytics()))
    b6.pack(side=tk.LEFT, padx=5, pady=5)
    
    b7 = tk.Button(root, text='CONNECT TO TWITTER', command=(lambda e=ents: twitterConn()))
    b7.pack(side=tk.LEFT, padx=5, pady=5)
    
    root.mainloop()
