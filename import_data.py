import json
# import requests
from sklearn.externals import joblib
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])


# from api.goods.models import GoodsModel
def create_index():
    mapping = '''
        {
          "mappings": {
            "goods2": { 
              "_all":       { "enabled": false  }, 
              "properties": { 
                "pid":    { "type": "text"  }, 
                "site_name":     { "type": "text"  }, 
                "name":     { "type": "text"  }, 
                "img":     { "type": "text"  }, 
                "query_click":     { "type": "text"  }, 
                "cate1":     { "type": "text"  }, 
                "cate2":     { "type": "text"  }, 
                "cate3":     { "type": "text"  }, 
                "review_num":     { "type": "integer"  }, 
                "review_rate":     { "type": "integer"  }, 
                "clickct":     { "type": "integer"  }
              }
            }
          }
        }
        '''
    es.indices.create(index="goods", ignore=400, body=mapping)
    # es.search(index='test-index', filter_path=['hits.hits._id', 'hits.hits._type'])


def generate_data_batch(index_name):
    goods_list = joblib.load("goods_dump.dat")
    # es.indices.put_mapping(index="goods", body=goods_list, doc_type="application/json")
    i = 0
    count = 0
    actions = []
    for goods in goods_list:
        action = {
            "_index": index_name,
            "_type": "ko",
            "_source": {
                "goods": goods,
            }
        }
        i += 1
        actions.append(action)
        print("loop", i)
        if i >= 50000:
            success, _ = bulk(es, actions, index=index_name, raise_on_error=True)
            count += success
            i = 0
            actions = []

    success, _ = bulk(es, actions, index=index_name, raise_on_error=True)
    count += success
    print("insert %s lines" % count)


create_index()
generate_data_batch()
