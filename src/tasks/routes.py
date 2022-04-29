from flask import Blueprint, request
import tasks.tasks_controller as tasks_controller

# Configuracion de Blueprint
tasks_bp = Blueprint('tasks_bp', __name__)


@tasks_bp.route('/', methods=['GET'])
def index():
    return tasks_controller.get_all()


@tasks_bp.route('/', methods=['POST'])
def createOne():
    return tasks_controller.create(request)

@tasks_bp.route('/<id>/', methods=['PUT'])
def updateTask(id):
    id = int(id)
    return tasks_controller.setCompleted(id)

@tasks_bp.route('/<id>/', methods=['GET'])
def getTaskByID(id):
    id = int(id)
    return tasks_controller.getTaskByID(id)