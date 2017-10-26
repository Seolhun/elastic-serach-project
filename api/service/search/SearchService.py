from settings.logging import logger
from settings.elasticsearch import es


def search_text(search_value):
    # Searching All
    query = {
        'query': {
            'match_all': {

            }
        }
    }
    # # Search By site_name
    # query = {
    #     'query': {
    #         'match': {
    #             'site_name': search_value,
    #         }
    #     }
    # }

    # query = {
    #     "query": {
    #         "constant_score": {
    #             "filter": {
    #                 "term": {
    #                     "site_name": search_value
    #                 }
    #             }
    #         }
    #     }
    # }
    # query = {
    #     "query": {
    #         "multi_match": {
    #             "query": search_value,
    #             "type": "cross_fields",
    #             "fields": ["site_name", "name", 'cate1', 'cate2', 'cate3']
    #         }
    #     }
    # }

    # "type": "cross_fields",
    # "type": "phrase_prefix",
    res = es.search(index="goods", doc_type="item", body=query)

    # responses = es.search(index="goods", body=query)
    logger.info("------------------------------------------------------------------------")
    logger.info("search_text {}".format(res))
    logger.info("------------------------------------------------------------------------")
    good_list = []
    for hit in res['hits']['hits']:
        good_list.append(hit)
    return {'goods_list': good_list}
