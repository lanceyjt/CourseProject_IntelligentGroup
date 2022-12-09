# CS410Project Intelligent Browsing via IntelligentGroup

Demo Video Link: https://drive.google.com/file/d/13RUHbyXD1uhBXgWowbY-RiNBWmN_Wf-T/view?usp=sharing

## Overview
The code provides the information below when a user enter a search term in the Chrome extension:
- BM25 scores for first 30 documents in Google search and re-rank in descending order;
- Top 5 most frequently used words and the corresponding word frequency for each document;
- 5 topics covered in the 30 documents, and each topic is represented by the first 10 words.

It can be used for users wanting to modify their search query and wanting to find results that have to do mainly with the topic that satisfies their needs. It can also give a user an overview of each document as well.

For any question’s on how the Project works or questions about the project/code, please contact:
* alins2@illionis.edu
* yao28@illinois.edu 

## How to...?
### How to install dependencies and set up local host

1. Clone the Github Repo:
```
git clone https://github.com/lanceyjt/CourseProject_IntelligentGroup.git 
```
2. Set up & activate Conda environment (Replace <env> by a name of your choice):

If you are using MAC:
```
conda config --add channels conda-forge
conda create -n <env> --file requirements_conda.txt
conda activate <env>
```

If you are using Windows:
```
conda config --add channels conda-forge
conda create -n <env> python=3.9
conda activate <env>
conda install django
conda install html2text
conda install scikit-learn
conda install requests
conda install nltk
conda install bs4
```

3. Install packages only viable through PIP:
```
pip install google
pip install rank_bm25
```
4. Run Django Server:
```
cd mysite      
python manage.py runserver
```

By running the command above, you should be able to see a message like “Starting development server at http://127.0.0.1:8000/”.

To experience the backend functionality, you can input the URL:http://127.0.0.1:8000/intelligentgroup/search_action_analysis/?query=<query>

You can replace the query at the end with a search term query you would like to analyze( ex. http://127.0.0.1:8000/intelligentgroup/search_action_analysis/?query=bm25).

Please give this a few seconds of your time as it is processing your search query in the backend and will output the bm25 score, word frequency, and topics.

### How to install and run application via chrome extension:
After you have successfully done the steps in the last section, please follow the steps below to run the Chrome Extension.

1. Click the three dots token at the top right corner of the Chrome browser. 
2. Go to “More Tools” → “Extensions”
3. Toggle “Developer mode” at the top right corner if it isn’t already activated
4. Click “Load Unpacked” at the top left corner
5. A file explorer window will pop-up
6. Go to the “chrome_extension” subfolder from the code cloned from git, and click “Select”
7. You should be able see an extension named as “Intelligent Search 1.0” now

![image](/images/extension_in_chrome.png)

8. Make sure the extension is turned on by toggling the button at the bottom right

**Important Note: To make sure the Chrome Extension works properly, please make sure the local host created by Django in the previous step is active.**

9. To use the extension, click the extension icon at the right of the address bar, then click the extension “Intelligent Search 1.0”. The UI of the extension should show up.

![image](/images/extension_ui.png)

10. Enter the query you want to analyze, then click analyze. 
11. A new Chrome tab will pop up with the URL http://127.0.0.1:8000/intelligentgroup/search_action_analysis/?query=<query>, wait around 30 seconds while the backend script is running.

## How the application is implemented
 There are 2 components covered in this project: Python backend, and Chrome extension front end. 

In the Python backend, we use [Django](https://www.djangoproject.com/) as the web framework and the tool to create a local host for the Chrome extension to run. In the ```mysite``` subfolder, there are multiple files created by the Django command line following the Django project file structure. There are 3 pivotal files implementing the actual backend functionalities that we should keep an eye on.

**mysite/intelligentgroup/document.py**
This file is used for creating a document object which has several attributes and functions. The attributes include the URL, raw content, list of words, word frequency of a document. The functions include scraping the web document, creating a word list, applying preprocessing steps such as lemmatization and stop word filtering. As well as calculating the word frequency. 

**mysite/intelligentgroup/search_action.py**
The search action file is used for creating a search action object. A search action is defined by a query term and number of documents retrieved. The attributes include the search query term, number of web pages, and corpus. The functions include building the corpus, calculating the bm25 scores for all the documents and performing LDA topic modeling.

**mysite/intelligentgroup/view.py**
This file creates the view of the Web page, it calls objects & functions in ```search_action.py``` and ```document.py``` to perform the backend tasks, including BM25 scores calculation and re-ranking, word frequency calculation and topic modeling, then wrap up the result with HTML language to show in the web page.
As an experimental project, the webpage will be rendered in a local host. The URL of the page follows the format of: http://127.0.0.1:8000/intelligentgroup/search_action_analysis/?query=<query>.

In the Chrome Extension front end, the files are all included in the ```chrome_extension``` subfolder.

**mysite/chrome_extension/manifest.json**

The JSON file describes the important configuration for the extension. 

**mysite/chrome_extension/popup.html**
This file is the front end UI determined by HTML. It includes a text box to input a query term, and a submit button. 

**mysite/chrome_extension/popup.js**
When a click action is processed from the extension UI, it sends the query which the user input to the background to get the full URL, and then opens the URL in a new Chrome tab. To make sure the web page to be successfully rendered, you will need to make sure the local host is active by running the command ```python manage.py runserver```. Detailed instructions will be provided later.

**mysite/chrome_extension/backend.js**
The file is constructed by Chrome API with a listener, it waits for a request to be sent and then sends the full URL as the response back to the popup.

## Output Example

![image](/images/output_example_1.png)

![image](/images/output_example_2.png)
