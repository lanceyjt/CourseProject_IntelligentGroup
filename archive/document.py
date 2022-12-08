import re
import html2text
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

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
        self.word_counter = {}
        self.readable = True

    def get_raw_content(self):
        """
        Get raw content of the web document.
        Update self.raw_content.
        """
        try:
            response = requests.get(self.url, timeout=2.50)
        except Exception as err:
            # print(err)
            self.readable = False
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        raw_content = web_transformer.handle(str(soup))

        self.raw_content = raw_content
        return raw_content
    
    def get_word_lst(self, all_lowercase=True):
        """
        Get word list of the web document, only keep alphabetical characters.
        Update self.word_lst.
        """
        pat = re.compile(r'[^a-zA-Z0-9\s\-]+')
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
    
    def get_word_frequency(self):
        """
        Calculate frenquency of existing words in a document, update self.word_counter.
        """
        assert self.word_lst != [], 'Attribute word_lst is empty'
        word_counter = {}
        for w in self.word_lst:
            word_counter[w] = word_counter.get(w,0) + 1
        self.word_counter = word_counter

        return word_counter
