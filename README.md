<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- ABOUT THE PROJECT -->
## About The Project

An experimental chatbot which can be trained on one's messenger conversation. There are two capabilities of the program so far: train the bot to speak like yourself using your own chat history or train the bot to speak like someone else through your conversation with them. This project is designed to test the features of LangChain with ChatGPT as the LLM framework. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Installation and Usage

1. Get an OpenAI API Key at [https://openai.com/blog/openai-api](https://openai.com/blog/openai-api)
2. Clone the repo
   ```sh
   git clone https://github.com/robert-juang/facebook_chatbot.git
   ```
3. Create folder in the folder "chatWithAnother" or "chatWithSelf" called APIKey.py at the root and set a variable APIKEY to your personal API Key. 
   ```py
   APIKEY = "your-api-key"
   ```
4. Download your messenger conversation in JSON format and store it in a folder called: specialConvo. Drag specialConvo into the folder "chatWithAnother" or "chatWithSelf".
5. go to the root of the directory and run one of the two scripts. To chat with yourself, run:
   ```sh
   ./chatSelf.sh 
   ```
   or to chat to another person, run:
   ```sh
   ./chatAnother.sh 
   ```
6. When you are done chatting, pressing q will store your conversation in a txt file
 
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

The current capabilities of the python program is limited and is more of an experiment and demonstration of what can be built using the OpenAI API and Langchain framework. That being said, more updates will be made to try to improve the chatbot. Enjoy!

<p align="right">(<a href="#readme-top">back to top</a>)</p>
