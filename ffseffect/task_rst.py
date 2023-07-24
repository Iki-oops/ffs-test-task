from flask_fullstack import ResourceController
from flask_restx import Resource
from sqlalchemy import select

from common import db
from ffseffect.task_db import Task

controller = ResourceController('Tasks', path='/tasks/')


@controller.route('/')
class TaskListener(Resource):
    @controller.marshal_with(Task.IndexModel, as_list=True)
    def get(self):
        return db.session.execute(select(Task)).all()
