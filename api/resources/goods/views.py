from flask_restful import Resource, reqparse

from api.resources.goods.models import GoodsModel
from settings.logging import logger


class Goods(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pid', type=str, required=True, help="This pid field cannot be left blank!")

    @classmethod
    def get(cls, pid):
        goods = GoodsModel.find_by_id(pid)
        if goods:
            return goods.json()
        return {'message': 'goods not found'}, 404

    @classmethod
    def delete(cls, pid):
        goods = GoodsModel.find_by_id(pid)
        if goods:
            goods.delete_from_db()

        return {'message': 'stack deleted'}

    @classmethod
    def put(cls, pid):
        data = Goods.parser.parse_args()
        goods = GoodsModel.find_by_id(pid)
        if goods:
            goods.name = data['name']
        else:
            goods = GoodsModel(pid)

        goods.save_to_db()
        return goods.json()


class GoodsList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('search', type=str, required=True, help="This search field cannot be left blank!")

    def post(self):
        data = GoodsList.parser.parse_args()
        logger.debug("--------{}-------".format(data))
        return {"message": "An error occurred inserting the stack."}, 404

    def get(self):
        goods_list = GoodsModel.find_list()
        logger.debug("--------{}-------".format(goods_list))
        return {
            'goods': list(map(lambda goods: goods.json(), goods_list))
        }
