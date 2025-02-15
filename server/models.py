from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# metadata = MetaData(
#     naming_convention={
#         "ix": "ix_%(column_0_label)s",
#         "uq": "uq_%(table_name)s_%(column_0_name)s",
#         "ck": "ck_%(table_name)s_%(column_0_name)s",
#         "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#         "pk": "pk_%(table_name)s",
#      }
# )



db = SQLAlchemy(metadata=metadata)

# db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    serialize_rules = ('-baked_goods.bakery',)

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    baked_goods = db.relationship('BakedGood', backref='bakery')

    def __repr__(self):
        return f'<Bakery id={self.id} name="{self.name}">'


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    serialize_rules = ('-bakery.baked_goods',)

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    def __rep__(self):
        # return f'<BakedGood id={self.id} name="{self.name}">'
        return f'<BakedGood id={self.id} name="{self.name}">'
    


# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy_serializer import SerializerMixin

# # metadata = MetaData(naming_convention={
# #     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# # })

# metadata = MetaData(
#     naming_convention={
#         "ix": "ix_%(column_0_label)s",
#         "uq": "uq_%(table_name)s_%(column_0_name)s",
#         "ck": "ck_%(table_name)s_%(column_0_name)s",
#         "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#         "pk": "pk_%(table_name)s",
#      }
# )

# db = SQLAlchemy(metadata=metadata)

# class Bakery(db.Model, SerializerMixin):
#     __tablename__ = 'bakeries'

#     serialize_rules = ('-baked_goods.bakery',)

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     created_at = db.Column(db.String)
#     updated_at = db.Column(db.String)

#     baked_goods = db.relationship('BakedGood', backref='bakery')

#     def __repr__(self):
#        return f'<Bakery: {self.name} was created at {self.created_at} and updated at {self.updated_at}>'

# class BakedGood(db.Model, SerializerMixin):
#     __tablename__ = 'baked_goods'

#     serialize_rules = ('-bakery.baked_goods',)

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     price = db.Column(db.Integer)
#     created_at = db.Column(db.String)
#     updated_at = db.Column(db.String)
    
#     bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

#     def __repr__(self):
#        return f'<BakedGood: {self.name} the cost is {self.price} was created at {self.created_at} and updated at {self.updated_at}>'