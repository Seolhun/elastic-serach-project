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
        # result = SearchService.search_text(search_text)
        result0 = SearchService.search_text(search_text)
        logger.info("----result0----{}".format(result0))
        result1 = SearchService.search_test1(search_text)
        logger.info("----result1----{}".format(result1))
        result2 = SearchService.search_test2(search_text)
        logger.info("----result2----{}".format(result2))
        result3 = SearchService.search_test3(search_text)
        logger.info("----result3----{}".format(result3))
        result4 = SearchService.search_test4(search_text)
        logger.info("----result4----{}".format(result4))
        return result4, 404
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
