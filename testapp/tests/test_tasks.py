import pytest
from sample_app.views.tasks import Tasks
from sample_app.models.taskmodel import task_obj
from conftest import client

def test_get_task(client):
    get_tasks_response =client.get("/tasks/")
    assert get_tasks_response.status_code == 200

def test_create_task(client):
    data_for_create = {'task': "create_task_test_case"}
    create_task_response = client.post("/tasks/", data=data_for_create)
    assert create_task_response.status_code == 201

def test_put_task(client):
    data_for_update = {'task': "update_task_test_case"}
    _id = task_obj.tasks[0]['task_Id']
    create_task_response = client.put("/tasks/" + str(_id), data=data_for_update)
    assert create_task_response.status_code == 201

def test_delete_task(client):
    _id = task_obj.tasks[0]['task_Id']
    delete_task_response = client.delete("/tasks/" + str(_id))
    assert delete_task_response.status_code == 204
