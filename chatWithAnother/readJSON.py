import json 
from datetime import datetime

#contain participaant + messages
people = [] 

f = open('./chatWithAnother/specialConvo/message_1.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

#get data
for ppl in data["participants"]: 
    people.append(ppl["name"])
message = data["messages"] 
print("File Read Finished") 
f.close()

#write to file
file1 = open("./chatWithAnother/testText/testfile.txt","w")
for num in range(len(message)-1, -1,-1) : 
    msg = message[num] 
    if "content" in msg and "Reacted" not in msg["content"]: 
        # file1.write("Date:{0}. Sender: {1}. Message: {2} \n".format(datetime.fromtimestamp(msg["timestamp_ms"]/1000.00), msg["sender_name"], msg["content"])) 
        file1.write("Sender: {0}. Message: {1} \n".format(msg["sender_name"], msg["content"])) 
file1.close() 
print("Text File Written") 


