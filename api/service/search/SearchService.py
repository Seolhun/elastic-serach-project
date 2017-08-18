from settings.thirdparty import es


def search_text(search_value):
    # query = {
    #     "query": {
    #         "match_all": {
    #
    #         }
    #     }
    # }
    # query = {
    #     "query": {
    #         "term": {"name": search_value}
    #     }
    # }
    query = {
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "name": search_value
                    }
                }
            }
        }
    }
    # query = {
    #     "query": {
    #         "match": {
    #             "name" : search_value
    #         }
    #     }
    # }

    # res = es.search(index="goods", body=query, from_=20, size=100, _source=False)
    res = es.search(index="goods", body=query, from_=20, size=100)
    good_list = []
    for hit in res['hits']['hits']:
        # good_list.append(hit["_source"]['goods'])
        good_list.append(hit)
    return {'goods_list': good_list}
