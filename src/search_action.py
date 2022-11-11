from googlesearch import search

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
        self.url_lst = []

    def invoke_url_iterator(self, num=10, pause=0.5):
        """
        Invoke url iterator from Google search.
        @num: Number of result per page
        @stop: Last result to retrieve
        @pause: Lapse to wait between HTTP requests
        """
        iterator = search(query=self.query, num=num, stop=self.num_result, pause=pause)
        self.url_iter = iterator

    def get_url_list(self):
        """
        Get url list of a search action.
        """
        assert self.url_iter is not None, 'url iternator is not invoked'
        url_lst = list(self.url_iter)
        self.url_lst = url_lst
        return url_lst

    

