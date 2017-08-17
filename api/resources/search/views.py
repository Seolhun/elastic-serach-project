from flask_restful import Resource, reqparse

from api.resources.goods.models import GoodsModel
from settings.logging import logger
from api.service.search import SearchService


class Search(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sv', type=str, required=True, help="This search value field cannot be left blank!")

    def get(self):
        data = Search.parser.parse_args()
        logger.debug("--------{}-------".format(data))
        result = SearchService.search_text(data['sv'])

        return {'message': '{} has no data'.format(result)}, 404

    def delete(self, search):
        goods = GoodsModel.find_by_id(search)
        if goods:
            goods.delete_from_db()

        return {'message': 'stack deleted'}

    def put(self, pid):
        data = Search.parser.parse_args()
        goods = GoodsModel.find_by_id(pid)
        if goods:
            goods.name = data['name']
        else:
            goods = GoodsModel(pid)

        goods.save_to_db()
        return goods.json()
