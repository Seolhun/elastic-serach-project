from api.goods.models import GoodsModel
from sklearn.externals import joblib


def generate_data():
    goods_list = joblib.load("goods_dump.dat")
    for goods in goods_list:
        if GoodsModel.find_by_id(goods['pid']):
            return;

        item = GoodsModel(goods['pid'])
        item.name = goods['name']
        item.site_name = goods['site_name']
        item.img = goods['img']
        item.query_click = goods['query_click']
        item.cate1 = goods['cate1']
        item.cate2 = goods['cate2']
        item.cate3 = goods['cate3']

        item.clickct = int(goods['clickct'])
        item.review_num = int(goods['review_num'])
        item.review_rate = int(goods['review_rate'])

        item.save_to_db()
    return 'ok'



