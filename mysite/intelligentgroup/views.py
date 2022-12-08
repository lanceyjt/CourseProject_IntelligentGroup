from django.shortcuts import render

# Create your views here.
import json
from . import search_action
from django.contrib.auth.models import User 
from django.http import JsonResponse , HttpResponse 

def index(request):
    return HttpResponse("Hello, world. You're at the intelligentgroup index.")


def search_action_analysis(request):

    query = request.GET.get('query', None)

    sa = search_action.SearchAction(query, 30)
    sa.invoke_url_iterator(num_extra_doc=8)
    sa.create_doc_list()
    sa.build_corpus()

    bm25_scores = sa.get_bm25_scores()

    word_freq_to_return = {} # (url, {word: frequency}) dictionary

    for d in bm25_scores:
        url = d[0]
        word_freq_lst = list(sa.word_freq.get(url).items())
        word_freq_lst.sort(reverse=True, key=lambda x: x[1])
        for i in range(5):
            try:
                word_freq_to_return[url] = word_freq_to_return.get(url, []) + [",".join([str(x) for x in word_freq_lst[i]])]
            except:
                pass

    topics = sa.lda_topic_model(num_topic=5, k=10)

    data = {
        'query_input': query,
        'bm25_scores': bm25_scores,
        'word_freq': word_freq_to_return,
        'topics': topics
    }
    
    print('json-data to be sent: ', data)

    return JsonResponse(data)
