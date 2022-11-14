from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import requests
import html2text
import re

web_transformer = html2text.HTML2Text()
web_transformer.ignore_links = True

class WebDocument(object):
    """
    A document with a website url.
    """

    def __init__(self, url):
        """
        Initialize web document.
        """
        self.url = url
        self.raw_content = ""
        self.word_lst = []

    def get_raw_content(self):
        """
        Get raw content of the web document.
        Update self.raw_content.
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        raw_content = web_transformer.handle(str(soup))

        self.raw_content = raw_content
        return raw_content
    
    def get_word_lst(self, all_lowercase=True):
        """
        Get word list of the web document, only keep alphabetical characters.
        Update self.word_lst.
        """
        pat = re.compile(r'[^a-zA-Z\s]+')
        raw_content = self.raw_content.lower() if all_lowercase else self.raw_content
        word_content = re.sub(pat, '', raw_content)
        word_lst = word_content.split()

        self.word_lst = word_lst
        return word_lst

    def pre_processing(self, lemmentize=True,remove_stop_words=True):
        """
        Apply preprocessing steps to self.word_lst.
        """
        assert self.word_lst != [], 'Attribute word_lst is empty'
        if lemmentize:
            wnl = WordNetLemmatizer()
            lemmentized_word_lst = [wnl.lemmatize(w) for w in self.word_lst]
            self.word_lst = lemmentized_word_lst
        if remove_stop_words:
            stop_words = set(stopwords.words('english'))
            filtered_word_lst = [w for w in self.word_lst if not (w.lower() in stop_words or len(w) < 2 or len(w) > 45)]
            self.word_lst = filtered_word_lst




