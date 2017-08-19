from flask_restful import Resource, reqparse

from api.resources.goods.models import GoodsModel
from settings.logging import logger
from api.service.search import SearchService


class Search(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sv', type=str, required=True, help="This search value field cannot be left blank!")

    @classmethod
    def get(cls):
        data = Search.parser.parse_args()
        search_text = data['sv']
        result = SearchService.search_text(search_text)
        return result, 404
        # return {'message': '{} has no data'.format(data)}, 404

    @classmethod
    def delete(cls, search):
        goods = GoodsModel.find_by_id(search)
        if goods:
            goods.delete_from_db()

        return {'message': 'stack deleted'}

    @classmethod
    def put(cls, pid):
        data = Search.parser.parse_args()
        goods = GoodsModel.find_by_id(pid)
        if goods:
            goods.name = data['name']
        else:
            goods = GoodsModel(pid)

        goods.save_to_db()
        return goods.json()
