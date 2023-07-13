import os 
import sys
import APIKey
import readJSON
import random 
from datetime import date

from langchain.document_loaders import TextLoader 
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = APIKey.APIKEY

ppl = readJSON.people
query = """ The textfile contains two pieces of information: Sender and Message. 
Pretend you are {0}. I will be person {1}. I want you to act like {0}.
Analyze {0}'s speech pattern and adjust your way of speaking to be like {0}. 
I want you to respond and answer like {0} using the tone, manner and vocabulary {0} would use. Do not write any explanations. 
Only answer like {0}. Ignore any anomalies in the text such as unparsable characters. 
Take into account {1}'s answer and respond with a conversational tone matching that of {0}.
Try to limit your responses to 3 sentences maximum. Remember, shorter is better. 
""".format(ppl[0], ppl[1])


loader = TextLoader('./chatWithAnother/testText/testfile.txt')
# loader = DirectoryLoader(".", glob="*.txt") 
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
    query = """ The textfile contains two pieces of information: Sender and Message. 
            Pretend you are {0}. I will be person {1}. I want you to act like {0}.
            Analyze {0}'s speech pattern and adjust your way of speaking to be like {0}. 
            I want you to respond and answer like {0} using the tone, manner and vocabulary {0} would use. Do not write any explanations. 
            Only answer like {0}. Ignore any anomalies in the text such as unparsable characters. 
            The messages that are most recently sent are separated by "|" and is sequential. 
            Take into account {1}'s answer and respond with a conversational tone matching that of {0}.
            Please do not include "|" in your responses. Remember the previous chat messages which is sent by both
            {0} and {1}. The messages which are more recent should hold slightly more weight in the way {0} should speak
            whether that be answering questions, giving advice, or being conversational but {0} should still speak and respond 
            with the same conversational tone of {0} in the textfile. Try to limit your responses to 3 sentences maximum. Remember, shorter is better. 
            Also, try to not repeat the texts with similar ideas. For example, if {0} say "Hey! Not much, " in one response, 
            please try to not use it again. It is okay if you do, but please do it sparingly and under the right response from {1}.

            Here are {1}'s recently sent messages in a list format: {2}. 
            """.format(ppl[0], ppl[1], r2)
    result = index.query(query, llm=ChatOpenAI())
    print(result) 
    recent1.append(result) 
randnum = random.randint(0,100000000000)

file1 = open("./chatWithAnother/conversations/convo{0}.txt".format(randnum),"w")
file1.write("Bot: {0}. Human: {1}. Conversation date: {2}\n".format(ppl[0], ppl[1], date.today()))
for i in range(len(recent1)) : 
    file1.write("Human: {0}\n".format(recent2[i]))
    file1.write("Bot: {0} \n".format(recent1[i])) 

file1.close() 
print("Conversation Recorded") 

