from flask_fullstack import Identifiable, PydanticModel
from sqlalchemy import Column, ForeignKey, select
from sqlalchemy.sql.sqltypes import Integer, String, Text

from common import Base, db, User
from ffseffect.category_db import Category


class Task(Base, Identifiable):
    __tablename__ = 'tasks'
    not_found_text = 'Task not found'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    BaseModel = PydanticModel.column_model(id)
    CreateModel = PydanticModel.column_model(name, description)
    IndexModel = BaseModel.combine_with(CreateModel)

    @classmethod
    def create(
            cls, category_id: int, user_id: int, name: str, description: str
    ):
        entry: cls = super().create(
            category_id=category_id,
            user_id=user_id,
            name=name,
            description=description
        )
        db.session.flush()
        return entry

    def __repr__(self):
        return f'Task {self.id} {self.name}'

    @classmethod
    def find_by_id(cls, entry_id: int):
        return db.get_first(select(cls).filter_by(id=entry_id))

    @classmethod
    def find_by_category_and_user(cls, category_id: int, user_id: int):
        stmt = select(cls).filter_by(category_id=category_id, user_id=user_id)
        return db.get_all(stmt)
