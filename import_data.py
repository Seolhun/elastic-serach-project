# import requests
import threading

from settings.thirdparty import es
from elasticsearch.helpers import bulk
from sklearn.externals import joblib


class IndexDataThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        create_index("goods")
        generate_data_batch("goods")
        print("Exiting " + self.name)


# from api.goods.models import GoodsModel
def create_index(index_name):
    mapping = '''
        {
          "mappings": {
            "goods": { 
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
    es.indices.create(index=index_name, ignore=400, body=mapping)
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
            "_type": "item",
            "_source": {
                "goods": goods,
            }
        }
        i += 1
        actions.append(action)
        if i >= 50000:
            print("success", i)
            success, _ = bulk(es, actions, index=index_name, raise_on_error=True)
            count += success
            i = 0
            actions = []

    success, _ = bulk(es, actions, index=index_name, raise_on_error=True)
    count += success
    print("insert %s lines" % count)


thread1 = IndexDataThread(1, "Thread-1", 1)
thread1.start()
