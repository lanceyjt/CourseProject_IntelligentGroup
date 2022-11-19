from googlesearch import search
from document import WebDocument
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

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

    def invoke_url_iterator(self, num=10, pause=0.5, num_extra_doc=0):
        """
        Invoke url iterator from Google search.
        @num: Number of result per page
        @pause: Lapse to wait between HTTP requests
        @num_extra_doc: Extra number of documents to offset for web documents not readable or parsable.
        """
        iterator = search(query=self.query, num=num, stop=self.num_result+num_extra_doc, pause=pause)
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
            if d.url.endswith('.pdf') or d.url.endswith('.pdf/'):
                continue # not able to parse pdf file appropriately

            if len(corpus) >= self.num_result:
                break

            d.get_raw_content()

            if d.readable:
                d.get_word_lst()
                d.pre_processing()
                corpus[d.url] = corpus.get(d.url, d.word_lst)
                count += 1
                print("Number of documents scanned: {x}".format(x=count))

        self.corpus = corpus

    def get_bm25_scores(self, query=""):
        """
        Rank documents with Okapi BM25, and return a list of [doc, score].
        """
        assert len(self.corpus) > 0, 'Corpus is empty'
        tokenized_corpus = list(self.corpus.values())
        bm25 = BM25Okapi(tokenized_corpus)
        query = self.query.lower() if query == "" else query.lower()
        tokenized_query = query.split()
        doc_scores = list(bm25.get_scores(tokenized_query))
        url_lst = [x.url for x in self.document_lst if x.readable]
        doc_scores_map = list(zip(url_lst, doc_scores))
        doc_scores_map.sort(reverse=True, key=lambda x: x[1])
        return doc_scores_map

    def lda_topic_model(self, num_topic=3, k=5):
        """
        Perform LDA topic modeling.
        @num_topic: number of topic with LDA
        @k: Top k words will be used to represent a topic
        """
        assert len(self.corpus) > 0, "Corpus is empty"
        corpus_text = [" ".join(x) for x in self.corpus.values()]

        # Create doc term matrix
        print("Create doc term matrix...")
        count_vect = CountVectorizer(stop_words='english')
        doc_term_matrix = count_vect.fit_transform(corpus_text)

        # Fit LDA model
        print("Fit LDA model...")
        LDA = LatentDirichletAllocation(n_components=num_topic, random_state=111)
        LDA.fit(doc_term_matrix)

        topics = []
        for _, topic in enumerate(LDA.components_):
            top_words = [count_vect.get_feature_names_out()[i] for i in topic.argsort()[-k:]]
            topics.append(top_words)

        return topics



        
    




