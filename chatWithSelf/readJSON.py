import json 
import os 
from datetime import datetime

#contain participaant + messages
#TODO: Change to accept user input 
name = input("Enter your name: (Make sure it's the name on your FB/Instagram account) ")
people = name

fileloc = "./chatWithSelf/chatData"

for index, folders in enumerate(os.listdir(fileloc)):
    f = os.path.join(fileloc, folders)
    if os.path.isdir(f): 
        #check appropriate directory
        for file in os.listdir(f): 
            #read
            if (file == "message_1.json"):
                f = open('{0}/message_1.json'.format(f),"r")
                data = json.load(f)
                message = data["messages"] 
                f.close()

                #write messages to file
                file1 = open("./chatWithSelf/processedData/testfile{0}.txt".format(index),"w+")
                for num in range(len(message)) : 
                    msg = message[num] 
                    if "content" in msg and "Reacted" not in msg["content"]: 
                        file1.write("Sender: {0}. Message: {1} \n".format(msg["sender_name"], msg["content"])) 
                file1.close() 

print("Data processed") 


