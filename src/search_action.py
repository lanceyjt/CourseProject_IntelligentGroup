from googlesearch import search
from document import WebDocument

class SearchAction(object):
    """
    A search action is defined by a query and number of documents retrieved from Google search.
    """

    def __init__(self, query, num_result=20):
        """
        Initialize a search action.
        """
        self.query = query # Query input in Google search   
        self.num_result = num_result # Number of result/document retrieved
        self.url_iter = None
        self.document_lst = [] # list of WebDocument object
        self.corpus = {} # key: url, value: word list

    def invoke_url_iterator(self, num=10, pause=0.5):
        """
        Invoke url iterator from Google search.
        @num: Number of result per page
        @pause: Lapse to wait between HTTP requests
        """
        iterator = search(query=self.query, num=num, stop=self.num_result, pause=pause)
        self.url_iter = iterator

    def create_doc_list(self):
        """
        Create self.document_lst with a list of WebDocument object.
        """
        assert self.url_iter is not None, 'url iternator is not invoked'
        url_lst = list(self.url_iter)
        self.document_lst = [WebDocument(url) for url in url_lst]

    def build_corpus(self):
        """
        Build corpus of a search action, return a list of tokenized list of words.
        """
        assert len(self.document_lst) > 0, 'Document list is empty' 
        count = 0
        corpus = {}
        for d in self.document_lst:
            d.get_raw_content()
            d.get_word_lst()
            d.pre_processing()
            corpus[d.url] = corpus.get(d.url, d.word_lst)
            count += 1
            print("Number of documents scanned: {x}".format(x=count))

        self.corpus = corpus




