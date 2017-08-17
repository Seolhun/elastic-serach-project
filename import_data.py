import json
import requests
from sklearn.externals import joblib
from elasticsearch import Elasticsearch


# from api.goods.models import GoodsModel


def generate_data():
    es = Elasticsearch(hosts=["http://127.0.0.1:9200"])
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
    es.indices.create(index="goods", ignore=400, body=mapping)
    # es.search(index='test-index', filter_path=['hits.hits._id', 'hits.hits._type'])

    goods_list = joblib.load("goods_dump.dat")
    # es.indices.put_mapping(index="goods", body=goods_list, doc_type="application/json")
    for goods in goods_list:
        pid = goods["pid"]
        es.index(index="goods", doc_type="generated", id=pid, body=goods)
        # print(goods_list)
        # print("-----", goods_list[:5])
        # headers = {'Content-type': 'application/json'}
        # response = requests.post("http://127.0.0.1:9200/goods/external/_bulk?pretty", headers=headers, data=goods_list[:5])
        # for goods in goods_list:
        #     if GoodsModel.find_by_id(goods['pid']):
        #         return;
        #
        #     item = GoodsModel(goods['pid'])
        #     item.name = goods['name']
        #     item.site_name = goods['site_name']
        #     item.img = goods['img']
        #     item.query_click = goods['query_click']
        #     item.cate1 = goods['cate1']
        #     item.cate2 = goods['cate2']
        #     item.cate3 = goods['cate3']
        #
        #     item.clickct = int(goods['clickct'])
        #     item.review_num = int(goods['review_num'])
        #     item.review_rate = int(goods['review_rate'])
        #
        #     item.save_to_db()
        # return response.json()


generate_data()
