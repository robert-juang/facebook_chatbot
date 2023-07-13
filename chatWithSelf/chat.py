import os 
import sys
import APIKey
import readJSON
import random 
from datetime import date
import nltk
import ssl

# will try to install on load, can comment out if installed
# ----------------------------------------------------------
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
# ----------------------------------------------------------

from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = APIKey.APIKEY

ppl = readJSON.people
query = """ You are given a directory of text messages which contains two pieces of information: A Sender and a corresponding Message. 
Please analyze all the conversations and examine the speech, tone, and voice of {0} only. Make sure to study {0}'s response with senders who are not named {0}. 
After you are done analyzing, I want you to become a chatbot and act like {0}. Examine {0}'s speech pattern and adjust your way of speaking to be like {0}. 
I want you to respond to me and answer like {0} using the tone, manner and vocabulary {0} would use. Do not write any explanations. 
Only answer like {0}. Ignore any anomalies in the texts such as unparsable characters. 
Try to limit your responses to 3 sentences maximum. Remember, shorter is better. 
""".format(ppl)


loader = DirectoryLoader("./chatWithSelf/processedData/", glob="*.txt", show_progress=True) 
index = VectorstoreIndexCreator().from_loaders([loader]) 
print("Enter a message to start a conversation:")

recent1 = [] 
recent2 = [] 

while True: 
    response = input("")
    if (response == "q"): 
        break 
    recent2.append(response)
    # r1 = " | ".join(recent1) 
    # r2 = " | ".join(recent2) 
    r2 = recent2[-1] 
    query = """ You are given a directory of text messages which contains two pieces of information: A Sender and a corresponding Message. 
            Please analyze all the conversations and examine the speech, tone, and voice of {0} only. Make sure to study {0}'s response with senders who are not named {0}. 
            After you are done analyzing, I want you to become a chatbot and act like {0}. Examine {0}'s speech pattern and adjust your way of speaking to be like {0}. 
            I want you to respond to me and answer like {0} using the tone, manner and vocabulary {0} would use. Do not write any explanations. 
            Only answer like {0}. Ignore any anomalies in the texts such as unparsable characters. 
            Try to limit your responses to 3 sentences maximum. Remember, shorter is better. 
            The messages that are most recently sent are separated by "|" and is sequential. 
            Take into account my previous responses and reply with a conversational tone matching that of {0}.
            Please do not include "|" in your responses. The messages which are more recent should hold slightly more weight in the way {0} should speak
            whether that be answering questions, giving advice, or being conversational but {0} should still speak and respond 
            with the same conversational tone of {0} in the textfiles. Try to limit your responses to 3 sentences maximum. Remember, shorter is better. 
            Also, try to not repeat the texts with similar ideas. For example, if {0} say "Hey! Not much, " in one response, 
            please try to not use it again. It is okay if you do, but please do it sparingly and under the right responses from me. 

            Here are my recently sent messages in a list format: {1}. 
            """.format(ppl, r2)
    result = index.query(query)
    print(result) 
    recent1.append(result) 

randnum = random.randint(0,100000000000)

file1 = open("./chatWithSelf/conversations/convo{0}.txt".format(randnum),"w+")
file1.write("Bot: {0}. Human: {1}. Conversation date: {2}\n".format(ppl[0], ppl[1], date.today()))
for i in range(len(recent1)) : 
    file1.write("Human: {0}\n".format(recent2[i]))
    file1.write("Bot: {0} \n".format(recent1[i])) 

file1.close() 
print("Conversation Recorded") 

