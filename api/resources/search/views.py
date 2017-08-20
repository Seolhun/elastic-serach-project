from flask_cors import cross_origin
from flask_restful import Resource, reqparse
from settings.logging import logger
from api.resources.goods.models import GoodsModel
from api.service.search import SearchService


class Search(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sv', type=str, required=True, help="This search value field cannot be left blank!")

    @classmethod
    @cross_origin()
    def get(cls):
        data = Search.parser.parse_args()
        search_text = data['sv']
        logger.info("####### Search Get : {}".format(search_text))
        result = SearchService.search_text(search_text)

        return result, 404
        # return {'message': '{} has no data'.format(data)}, 404

    @classmethod
    @cross_origin()
    def delete(cls, search):
        goods = GoodsModel.find_by_id(search)
        if goods:
            goods.delete_from_db()

        return {'message': 'stack deleted'}

    @classmethod
    @cross_origin()
    def put(cls, pid):
        data = Search.parser.parse_args()
        goods = GoodsModel.find_by_id(pid)
        if goods:
            goods.name = data['name']
        else:
            goods = GoodsModel(pid)

        goods.save_to_db()
        return goods.json()

#
# class SearchList(Resource):
#     parser = reqparse.RequestParser()
#
#     @classmethod
#     @cross_origin()
#     def get(cls):
#         data = Search.parser.parse_args()
#         search_text = data['sv']
#         logger.info("####### Search Get : {}".format(search_text))
#         result = SearchService.search_text(search_text)
#
#         return result, 404
#         # return {'message': '{} has no data'.format(data)}, 404
