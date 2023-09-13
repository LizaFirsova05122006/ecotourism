import sqlalchemy
from sqlalchemy.util.preloaded import orm

from .db_session import SqlAlchemyBase


class Region(SqlAlchemyBase):
    __tablename__ = 'regions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_fd = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("federal_districts.id"))
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    federal = orm.relationship('Federal')
    nature = orm.relationship("Nature", back_populates='nature')