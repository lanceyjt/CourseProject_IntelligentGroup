# CS410Project Intelligent Browsing via IntelligentGroup

### How to run the application
##### Run the app independently
To run this file independently please download or fork repo and use an Integrated Development Environment (IDE) that can run both JavaScript and Python as we recommend you use visual studio. 

In order to run this file via IDE you must have node 19.2.0 version installed as well as python 3.9.0 which will automatically get downloaded with the node version and you can get the latest node version via this link: https://nodejs.org/en/download/current/ 

Once you have all the proper pre-requisites, you can run this code with the commands below within the IDE. The commands include: set up the Conda environment, download NLTK resources and run Javascript file.

```
conda create --name <env> --file requirements.txt
python3 download_nltk_resources.py
node CS410.js
```

This will run the JavaScript Code which will call the python scripts within the src file. It will be using a test text file called log.txt to and should output every document URL, Word Frequency and Topics for each document. This will ultimately help users fine the key words that would be helpful for there search query so the user can optimize what they are searching for and get ultimately the best results/documents that suites their needs.

#### Run the app via Chronme extension
To run this via a chrome extension, please download our code from the GitHub repo. 

After you have successfully download your code on your local machine, please go to extensions in google chrome and flip the developer mode toggle in the top right corner. Once this is flipped on, then there should be an option now available in the top left corner: “Load Unpacked”. Select that option and import the file as a whole to the chrome extension and insert a query into the search bar. Once a query had been searched, the extension will then return the document URLs with the word frequency and topics used for each URL. Using this information will allow the user to see what topics are most relevant and can use those topics to benefit which documents are most useful for the user or whether the query will need to be optimized to help find the documents the user is looking for. 

For any question’s on how the Project works or questions about the project/code, please contact:
* Alins2@illionis.edu
* yao28@illinois.edu 

### How does it work
1. The app will capture the Url of a google search result page, and parse the query from the Url.

2. Once the query term is captured, the backend script will get the Urls of the first 30 web pages.

3. The app will scrape those web pages/documents, and build a corpus for each web document. Pre-procssing steps including lemmentization and stop words filtering will be applied.

4. During scraping, the frequency for each word in a document is calculated.

5. After sraping, given the corpus of documents, the app will calculate the BM25 scores and rank the documents in the descending order to improve the user's search experience.

6. Top 5 keywords for each document will be provided. 

7. LDA topic modeling will be applied to the corpus of documents. The app will provide 5 topics, each of which is represented as the top 10 words in the topic.

**The information of BM25 scores, word frequencies, and topic modeling results will be used to inspire the user to refine the query terms, and will let the user have an overview of each document, and topics covered in the search result.** 

