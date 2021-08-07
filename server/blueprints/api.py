import datetime

from sanic import Blueprint
from sanic.response import json
from db.queries import resident_is_home, update_home_status


api_views = Blueprint('api_views', url_prefix='/api')


@api_views.route('/', methods=['GET', 'POST'])
async def sup_dude(request):
    return json(
        {
            'message': 'Sup dude?'
        }
    )


@api_views.route('/ping', methods=['GET', 'POST'])
async def ping(request):
    print('/ping()')
    return json(
        {
            'message': 'pong'
        }
    )


@api_views.route('/status', methods=['GET'])
async def get_status(request):
    status = resident_is_home()
    print('is_home ?', status)
    return json(
        {
            'is_home': status
        }
    )


@api_views.route('/home', methods=['POST'])
async def welcome_home(request):
    update_home_status(True)
    return json(
        {
            'is_home': True
        }
    )


@api_views.route('/away', methods=['POST'])
async def bye(request):
    update_home_status(False)
    return json(
        {
            'is_home': False
        }
    )
