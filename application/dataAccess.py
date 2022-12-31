from flask_login import current_user
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from .models import *


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def check_user_password(user, password):
    return user and check_password_hash(user.password, password)


def add_user(email: str, password: str) -> bool:
    user = get_user_by_email(email)
    result = False
    if not user:
        user_id = None
        if current_user:
            user_id = current_user.id
        try:
            db.session.add(
                User(
                    email=email,
                    password=generate_password_hash(password, method='sha256'),
                    user_id=user_id
                )
            )
            db.session.commit()
            result = True
        except exc.SQLAlchemyError:
            db.session.rollback()
    return result


def get_area_by_name(name):
    return Area.query.filter_by(name=name).first()


def add_area_model(name, description, lat, lng):
    result = False
    try:
        area = Area(
            name=name,
            description=description,
            lat=lat,
            lng=lng,
            user_id=current_user.id)
        db.session.add(area)
        db.session.commit()
        result = True
    except exc.SQLAlchemyError:
        db.session.rollback()
    return result


def get_all_area():
    return Area.query.all()


def get_media_by_rtsp_link(rtsp_link):
    return Media.query.filter_by(path=rtsp_link).first()


def get_area_by_id(area_id):
    return Area.query.filter_by(id=area_id).first()


def add_rtsp_model(name, rtsp_link, lat, lng, area_id):
    result = False
    try:
        model = Media(
            name=name,
            path=rtsp_link,
            lat=lat,
            lng=lng,
            area_id=area_id,
            user_id=current_user.id)
        db.session.add(model)
        db.session.commit()
        result = True
    except exc.SQLAlchemyError:
        db.session.rollback()
    return result
