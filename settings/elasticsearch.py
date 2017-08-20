from elasticsearch import Elasticsearch
from settings import config

es = Elasticsearch(hosts=[config.ELASTIC_SEARCH_HOST])
