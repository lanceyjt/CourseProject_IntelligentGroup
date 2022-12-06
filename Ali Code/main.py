#Uncomment This code to test if JS and PY script is communicating to one another

import sys
import json
import ast #abstract syntax tree
import search_action

# Create output to pass back
query = "bm25"

sa = search_action.SearchAction(query, 30)
sa.invoke_url_iterator(num_extra_doc=8)
sa.create_doc_list()
sa.build_corpus()

bm25_scores = sa.get_bm25_scores() # (url, bm25_score) list sorted by score in descending order

word_freq_to_return = [] # (url, {word: frequency}) list

for d in bm25_scores:
    url = d[0]
    word_freq_lst = list(sa.word_freq.get(url).items())
    word_freq_lst.sort(reverse=True, key=lambda x: x[1])
    for i in range(5):
        try:
            word_freq_to_return.append([url, word_freq_lst[i]])
        except:
            pass

topics = sa.lda_topic_model(num_topic=5, k=10)

print(bm25_scores)
print("------")
print(word_freq_to_return)
print("------")
print(topics)


# #This was the script called to communicate to the js script 
# #When Called by JS script, data_to_pass_back is data sent back to JSON
# data_to_pass_back = 'Document URL'
# data_to_pass_back_1 = 'Word Frequency'
# data_to_pass_back_2 = 'Topics'

# input = ast.literal_eval(sys.argv[1])
# input_1 = ast.literal_eval(sys.argv[1])
# input_2 = ast.literal_eval(sys.argv[1])
# output = input 
# output_1 = input_1 
# output_2 = input_2


# #output sent back to the script, please update this paramater below where your code is the output
# output['data_returned'] = data_to_pass_back
# output_1['data_returned_1'] = data_to_pass_back_1
# output_2['data_returned_2'] = data_to_pass_back_2

# #print data sent back, need help sending 3 different arguments with 1 arguemnt being sent for each line.
# print(json.dumps(output))

# #remove buffer with
# sys.stdout.flush()