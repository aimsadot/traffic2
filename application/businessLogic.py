from . import db
from flask_login import current_user
from .dataAccess import *


def format_area(sl, area):
    return {
        'sl': sl,
        'id': area.id,
        'name': area.name,
        "lat": area.lat,
        "lng": area.lng,
        "description": area.description,
        "created_by": area.user.email,
        "created_at": area.time_created
    }


def format_area_like(area):
    return {
        "text": area.name,
        "value": area.id
    }


def list_area():
    areas = get_all_area();
    lst = [format_area(idx + 1, area) for idx, area in enumerate(areas)]
    return lst


def list_area_by_like(like):
    areas = get_area_with_like(like)
    return [format_area_like(area) for area in areas]


def add_area(data):
    msg = []
    name = data['area_name']
    lat = data['area_lat']
    lng = data['area_lng']
    description = data['description']

    error = False
    if len(name) == 0:
        msg.append('No area name was given')
        error = True
    if get_area_by_name(name):
        msg.append('Area already exists')
        error = True
    if len(lat) == 0 or len(lng) == 0:
        msg.append('No geographical area was selected')
        error = True

    if not error:
        result = add_area_model(name, description, lat=lat, lng=lng)
        if result:
            msg.append("successfully added area to database!")
        else:
            msg.append("Unable to add area to database")
            error = True
    return error, msg


def add_rtsp(data):
    msg = []
    name = data['name']
    lat = data['rtsp_lat']
    lng = data['rtsp_lng']
    area_id = int(data['area_id'])
    rtsp_link = data['rtsp_link']

    error = False

    if len(name) == 0:
        msg.append('No link name was given')
        error = True
    if get_media_by_rtsp_link(rtsp_link):
        msg.append('RTSP Link already exists!')
        error = True
    if not get_area_by_id(area_id):
        msg.append('Area does not exist')
        error = True
    if len(lat) == 0 or len(lng) == 0:
        msg.append('No link location was selected in map')
        error = True

    if not error:
        result = add_rtsp_model(name=name, rtsp_link=rtsp_link, lat=lat, lng=lng, area_id=area_id)
        if result:
            msg.append("successfully added RTSP Link!")
        else:
            msg.append("Unable to add rtsp!")
            error = True
    return error, msg


def add_operations(mod, data):
    if mod == 'add_area':
        return add_area(data)
    elif mod == 'add_rtsp':
        return add_rtsp(data)
