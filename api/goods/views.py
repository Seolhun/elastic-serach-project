from flask_restful import Resource, reqparse

from api.goods.models import GoodsModel


class Goods(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pid', type=str, required=True, help="This pid field cannot be left blank!")

    def get(self, pid):
        goods = GoodsModel.find_by_id(pid)
        if goods:
            return goods.json()
        return {'message': 'goods not found'}, 404

    def delete(self, pid):
        goods = GoodsModel.find_by_id(pid)
        if goods:
            goods.delete_from_db()

        return {'message': 'stack deleted'}

    def put(self, pid):
        data = Goods.parser.parse_args()
        goods = GoodsModel.find_by_id(pid)
        if goods:
            goods.name = data['name']
        else:
            goods = GoodsModel(pid)

        goods.save_to_db()
        return goods.json()


class GoodsList(Resource):
    def post(self):
        return {"message": "An error occurred inserting the stack."}, 500

    def get(self):
        goods_list = GoodsModel.find_list()
        print(goods_list)
        return {
            'goods': list(map(lambda goods: goods.json(), goods_list))
        }
