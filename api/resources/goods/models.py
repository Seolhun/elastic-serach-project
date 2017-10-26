from settings.database import db
from sqlalchemy.orm import Session

'''
    "pid": "1194012460",
    "site_name": "lotteimall",
    "name": "'['인케이스']'아이폰7 아이콘 케이스_네이비",
    "img": "http://image2.lotteimall.com/goods/60/24/01/1194012460_1.jpg",

    "query_click": "인케이스아이콘케이스=96",

    "cate1": "휴대폰/음향/차량용기기",    
    "cate2": "휴대폰/태블릿액세서리",
    "cate3": "케이스/파우치",
    
    "review_num": 0
    "review_rate": 0,
    "clickct": 0,
'''


class GoodsModel(db.Model):
    __tablename__ = 'TB_GOODS'
    pid = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    site_name = db.Column(db.String(200))
    img = db.Column(db.String(200))

    query_click = db.Column(db.String(120))

    cate1 = db.Column(db.String(30))
    cate2 = db.Column(db.String(30))
    cate3 = db.Column(db.String(30))

    clickct = db.Column(db.Integer, default=0, server_default=db.text('0'))
    review_num = db.Column(db.Integer, default=0, server_default=db.text('0'))
    review_rate = db.Column(db.Integer, default=0, server_default=db.text('0'))

    def __init__(self, pid):
        self.pid = pid

    def json(self):
        return {
            'pid': self.pid,
            'name': self.name,
            'site_name': self.site_name,
            'img': self.img,
            'query_click': self.query_click,
            'cate1': self.cate1,
            'cate2': self.cate2,
            'cate3': self.cate3,
            'clickct': self.clickct,
            'review_num': self.review_num,
            'review_rate': self.review_rate
        }

    @classmethod
    def find_by_id(cls, pid):
        # stack = SimilarStackModel.query.filter(SimilarStackModel.stacks.any(stack_name=stack_name)).all()
        stack = cls.query.filter_by(pid=pid).first()
        return stack

    @classmethod
    def find_by_name(cls, name):
        # stack = SimilarStackModel.query.filter(SimilarStackModel.stacks.any(stack_name=stack_name)).all()
        stack = cls.query.filter_by(name=name).first()
        return stack

    @classmethod
    def find_list(cls):
        return cls.query.order_by(cls.pid)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def save_to_db_batch(self):
        session = Session(bind=None)
        session.bulk_insert_mappings(GoodsModel, [
            dict(
                
            )
        ])
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
