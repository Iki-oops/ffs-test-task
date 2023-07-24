from flask_fullstack import ResourceController, counter_parser
from flask_restx import Resource
from flask_restx.reqparse import RequestParser
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, PendingRollbackError

from common import User, db
from ffseffect.category_db import Category
from ffseffect.task_db import Task

controller = ResourceController('Category', path='/category/')

task_add_parser: RequestParser = RequestParser()
task_add_parser.add_argument("name", type=str, required=True)
task_add_parser.add_argument("description", type=str, required=True)


@controller.route('/')
class CategoryListener(Resource):
    @controller.marshal_with(Category.IndexModel, as_list=True)
    def get(self):
        return Category.get_all()


@controller.route('/<int:category_id>/tasks/')
class CategoryTasksListener(Resource):
    @controller.jwt_authorizer(User)
    @controller.marshal_with(Task.IndexModel, as_list=True)
    def get(self, user: User, category_id: int):
        return Task.find_by_category_and_user(category_id, user.id)

    @controller.doc_abort(400, "Object is not exist")
    @controller.jwt_authorizer(User)
    @controller.argument_parser(task_add_parser)
    @controller.marshal_with(Task.CreateModel)
    def post(self, user: User, category_id: int, name: str, description: str):
        category: Category = Category.find_by_id(category_id)

        if category is None:
            controller.abort(400, f'Category is not exist with this id - {category_id}')

        task: Task = Task.create(category_id, user.id, name, description)
        return task
