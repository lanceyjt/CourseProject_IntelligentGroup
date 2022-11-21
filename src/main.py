import search_action

def main():    
    query_list = ["bm25", "illinois", "LDA", "black friday"]

    for query in query_list:
        print("------- Analysis for Query: {} -------".format(query))
        sa = search_action.SearchAction(query, 30)

        print("==== Web Scraper ====")
        print("Invoke url iterator...")
        sa.invoke_url_iterator(num_extra_doc=8)

        print("Create web documents...")
        sa.create_doc_list()
        print("URL list: ", [x.url for x in sa.document_lst])

        print("Build corpus...")
        sa.build_corpus()

        corpus = sa.corpus
        print("Length of corpus: ", len(corpus))
        print("====================")
        print("")

        #with open("./output/{q}_corpus.txt".format(q=query), "w") as file:
        #    file.write(str(corpus))

        print("==== BM25 Ranking ====")
        res = sa.get_bm25_scores()
        print("Docs with BM25 scores in descending order: ")
        for d in res:
            print(d)
        print("======================")
        print("")

        print("==== Word frequency ====")
        word_freq = sa.word_freq
        
        print("Most frequently used 5 words & frequency for each document:")
        for d in res:
            url = d[0]
            print("Document url:", url)
            word_freq_lst = list(word_freq.get(url).items())
            word_freq_lst.sort(reverse=True, key=lambda x: x[1])
            for i in range(5):
                try:
                    print(word_freq_lst[i])
                except:
                    pass
            print("----")

        print("========================")
        print("")

        print("==== LDA Topic Modeling ====")
        topics = sa.lda_topic_model(num_topic=5, k=10)
        for i in range(len(topics)):
            print("Topic {i} for query '{q}': ".format(i=i+1, q=query))
            print(topics[i])
        print("============================")
        print("")

if __name__ == '__main__':
    main()



        