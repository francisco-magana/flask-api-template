from flask import jsonify, Response
from settings.database import mongo
from bson import json_util
from flask_cors import cross_origin

def get_all():

    all_tasks = mongo.db.tasks.find()
    
    response = {
        "message": "Data collected",
        "data": all_tasks,
        "success": True
    }

    response = json_util.dumps(response)

    return Response(response=response, status=200, mimetype="application/json")

def getTaskByID(id):
    task = mongo.db.tasks.find({"_id": id})

    response = {
        "message": "Task found",
        "data": task,
        "success": True
    }

    response = json_util.dumps(response)

    return Response(response=response, status=200, mimetype="application/json")


def create(request):
    data = request.get_json()
    print(data)
    task = {
        "_id": data["_id"],
        "task": data["task"],
        "completed": data["completed"]
    }

    print(task)

    mongo.db.tasks.insert_one(task)

    response = {
        "message": "Task created",
        "data": task,
        "success": True
    }

    response = json_util.dumps(response)

    return Response(response=response, status=200, mimetype="application/json")

def setCompleted(id):

    taskID = id
    print(taskID)
    
    mongo.db.tasks.update_one(
        {"_id": taskID},
        {
            "$set": {
                "completed": True
            }
        }
    )

    task = mongo.db.tasks.find({"_id": taskID})

    response = {
        "message": "Task updated",
        "data": task,
        "success": True
    }

    

    response = json_util.dumps(response)
    print(response)

    return Response(response=response, status=200, mimetype="application/json")