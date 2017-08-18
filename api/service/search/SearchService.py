import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import MultiSearch, Search, Q

from settings.logging import logger

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])


def search_test1(search_value):
    ms = MultiSearch(using=es, index='goods')
    ms = ms.add(Search(doc_type="item").filter('term', category='gsshop'))
    ms = ms.add(Search(doc_type="item"))
    responses = ms.execute()
    logger.info("------------------------------------------------------------------------")
    logger.info("responses {}".format(responses))
    logger.info("------------------------------------------------------------------------")
    good_list = []
    for response in responses:
        logger.info("------------------------------------------------------------------------")
        logger.info("response {}".format(response))
        logger.info("------------------------------------------------------------------------")
        for hit in response:
            logger.info("------------------------------------------------------------------------")
            logger.info("hit {}".format(hit))
            logger.info("------------------------------------------------------------------------")
            good_list.append(hit)


def search_test2(search_value):
    s = Search(using=es, index="goods", doc_type="item")
    s = s.query('bool', filter=[Q('terms', tags=['search', 'gsshop'])])
    responses = s.execute()
    # logger.info("-----search_test2{}".format(responses))

    good_list = []
    for response in responses:
        for hit in response:
            good_list.append(hit)
            print(hit.title)

    return {'goods_list': good_list}


def search_test3(search_value):
    s = Search(using=es, index="goods", doc_type="item").filter("term", category="site_name").query("match", title="lotteimall")

    responses = s.execute()
    good_list = []
    for hit in responses:
        print(hit.meta.score, hit.title)

    for tag in responses:
        good_list.append(tag)
        print(tag.key, tag.max_lines.value)

    return {'goods_list': good_list}


def search_test4(search_value):
    responses = es.get(index="goods", doc_type="item", id='AV313dFnjPA3zYh4asSV')['_source']
    # logger.info("------search_test4{}".format(responses))
    if not responses:
        return None
    return {'goods_list': responses}


def search_text(search_value):
    query = {
        "query": {
            "match_all": {

            }
        }
    }
    # query = {
    #     "query": {
    #         "match": {
    #             "site_name": "gsshop",
    #         }
    #     }
    # }
    # query = {
    #     "query": {
    #         "multi_match": {
    #             "query": "gsshop",
    #             "fields": ["site_name", "name"]
    #         }
    #     }
    # }

    responses = es.search(index="goods", doc_type="item", body=query)
    good_list = []
    for hit in responses['hits']['hits']:
        # good_list.append(hit["_source"]['goods'])
        good_list.append(hit)
    return {'goods_list': good_list}
