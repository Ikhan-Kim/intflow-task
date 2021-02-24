from flask import Blueprint, request, Response
from . import data
import json

bp = Blueprint('main', __name__, url_prefix='/')


# test_data = [
# {
#     "current_dt": "02/17/2021 11:00:00",
#     "camera_id": "1",
#     "object_id": "1",
#     "activity": "72",
#     "feed": "36",
#     "drinking": "56"
#   },
# {
#     "current_dt": "02/17/2021 11:00:00",
#     "camera_id": "1",
#     "object_id": "2",
#     "activity": "85",
#     "feed": "77",
#     "drinking": "62"
#   },
# ]

object_num = {
  1: 4,
  2: 4,
  3: 5,
}

@bp.route('/<int:camera_id>', methods=['GET'])
def camera_info(camera_id):
  if request.method == 'GET':
    res = Response(json.dumps(object_num))
    # list2dict = dict(zip(range(1, len(data.db)+1), data.db))
    # res = Response(json.dumps(list2dict))
    res.headers["Access-Control-Allow-Origin"] = "*"  
    return res

@bp.route('/<int:camera_id>/<int:object_id>', methods=['GET'])
def object_info(camera_id, object_id):
  if request.method == 'GET':
    object_time = []
    object_activity = []
    object_feed = []
    object_drinking = []

    for d in data.db:
      if d['camera_id'] == str(camera_id) and d['object_id'] == str(object_id):
        object_time.append(d['current_dt'])
        object_activity.append(d['activity'])
        object_feed.append(d['feed'])
        object_drinking.append(d['drinking'])
    object_data = dict( times = object_time, activity = object_activity, feed = object_feed, drinking = object_drinking)
    print("************************************")
    print(type(object_data))
    print(object_data)
    res = Response(json.dumps(object_data))
    res.headers["Access-Control-Allow-Origin"] = "*"  
    return res