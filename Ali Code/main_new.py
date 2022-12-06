import sys
import json
import ast #abstract syntax tree
import search_action

input = ast.literal_eval(sys.argv[1])
#input = {
#    'query_input': 'bm25',
#    'bm25_scores': None,
#    'word_freq': None,
#    'topics': None
#}

output = input

query = "bm25"

sa = search_action.SearchAction(query, 30)
sa.invoke_url_iterator(num_extra_doc=8)
sa.create_doc_list()
sa.build_corpus()

bm25_scores = sa.get_bm25_scores() # (url, bm25_score) list sorted by score in descending order

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

output['bm25_scores'] = bm25_scores
output['word_freq'] = word_freq_to_return
output['topics'] = topics


#print data sent back, need help sending 3 different arguments with 1 arguemnt being sent for each line.
print(json.dumps(output))

#remove buffer with
sys.stdout.flush()