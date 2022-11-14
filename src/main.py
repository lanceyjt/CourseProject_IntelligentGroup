import search_action

query1 = "bm25"
query2 = "illinois"

for query in [query1, query2]:
    sa = search_action.SearchAction(query, 12)

    print("Invoke url iterator...")
    sa.invoke_url_iterator()


    print("Create web documents...")
    sa.create_doc_list()

    print("Build corpus...")
    sa.build_corpus()

    corpus = sa.corpus
    print(len(corpus))

    with open("./output/{q}_corpus.txt".format(q=query), "w") as file:
        file.write(str(corpus))

        