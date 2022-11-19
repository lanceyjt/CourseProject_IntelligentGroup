import search_action

def main():    
    query_list = ["bm25", "illinois", "LDA", "black friday"]

    for query in query_list:
        print("------- Analysis for Query: {} -------".format(query))
        sa = search_action.SearchAction(query, 30)

        print("Invoke url iterator...")
        sa.invoke_url_iterator(num_extra_doc=8)

        print("Create web documents...")
        sa.create_doc_list()
        print("URL list: ", [x.url for x in sa.document_lst])

        print("Build corpus...")
        sa.build_corpus()

        corpus = sa.corpus
        print(len(corpus))

        with open("./output/{q}_corpus.txt".format(q=query), "w") as file:
            file.write(str(corpus))

        res = sa.get_bm25_scores()
        print("Docs with BM25 scores in descending order: ")
        print(res)

        topics = sa.lda_topic_model(num_topic=5, k=10)
        for i in range(len(topics)):
            print("Topic {i} for query '{q}': ".format(i=i+1, q=query))
            print(topics[i])

if __name__ == '__main__':
    main()



        