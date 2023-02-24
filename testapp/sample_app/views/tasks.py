from flask import Flask, render_template, request
from flask.views import View, MethodView
import marshmallow as ma
from flask_smorest import Blueprint, abort
from ..models.taskmodel import task_obj

blp = Blueprint("Tasks", "tasks", url_prefix="/tasks", template_folder='templates', description="Operations on tasks")


class TaskQueryArgsSchema(ma.Schema):
    task = ma.fields.String()
    # task_id = ma.fields.Int()


class TaskDataQueryArgsSchema(ma.Schema):
    task = ma.fields.String()


@blp.route("/")
class Tasks(MethodView):
    @blp.response(200)
    def get(self):
        """List all Tasks"""
        return task_obj.tasks

    @blp.arguments(TaskQueryArgsSchema, location="query")
    @blp.response(201)
    def post(self, task):
        """Adds a new task"""
        item = task_obj.createtask(task)
        return item


@blp.route("<int:task_id>")
class TasksActions(MethodView):
    @blp.response(200)
    def get(self, task_id):
        """Get a task by it's id"""
        try:
            item = task_obj.gettask(task_id)
            print(item)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        else:
            return item if item else abort(404, message=f"task_id - {task_id} - Item not found.")

    @blp.arguments(TaskDataQueryArgsSchema, location="query")
    @blp.response(201)
    def put(self, args, task_id: int):
        """ Update a task by it's id"""
        print(args, task_id)
        try:
            item = task_obj.gettask(task_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        else:
            return item.update(args) if item else abort(404, message=f"task_id - {task_id} - Item not found.")

    @blp.response(204)
    def delete(self, task_id):
        """Delete a task"""
        try:
            #task_obj.deletetask(task_id)
            deletion_status = task_obj.deletetask(task_id)
            if not deletion_status:
                abort(404, message=f"task_id - {task_id} - Item not found.")
        except ItemNotFoundError:
            abort(404, message="Item not found.")


class ItemNotFoundError(Exception):
    pass
