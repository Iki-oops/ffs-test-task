from flask_fullstack import Identifiable, PydanticModel
from sqlalchemy import Column, select
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String

from common import Base, db


class Category(Base, Identifiable):
    __tablename__ = "categories"
    not_found_text = "Category not found"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100), nullable=False)
    hex_color = Column(String(100), nullable=False)

    tasks = relationship('Task', backref='category')

    BaseModel = PydanticModel.column_model(id)
    CreateModel = PydanticModel.column_model(name, hex_color)
    IndexModel = BaseModel.combine_with(CreateModel)

    @classmethod
    def find_by_id(cls, entry_id: int):
        return db.get_first(select(cls).filter_by(id=entry_id))

    @classmethod
    def get_all(cls):
        return db.get_all(select(cls))
