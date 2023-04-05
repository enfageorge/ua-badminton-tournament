import pytest
from app import app, db
from models.tables.user import User
from models.tables.login import Login
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

@pytest.fixture(scope='module')
def new_login():
    login = Login(login_id = "login_id", password = "a_complicated_password")
    return login
@pytest.fixture(scope='module')
def new_user():
    user = User(first_name='John', last_name='Doe', email='johndoe@example.com')
    return user

def test_new_user(new_user):
    assert new_user.first_name == 'John'
    assert new_user.last_name == 'Doe'
    assert new_user.email == 'johndoe@example.com'

def test_add_user_to_database(new_user):
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()
        assert new_login in db.session
        assert new_user in db.session

def test_update_user(new_user):
    with app.app_context():
        new_user.first_name = 'Jane'
        db.session.commit()
        updated_user = User.query.filter_by(email='johndoe@example.com').first()
        assert updated_user.first_name == 'Jane'

def test_delete_user(new_user):
    with app.app_context():
        db.session.delete(new_user)
        db.session.commit()
        deleted_user = User.query.filter_by(email='johndoe@example.com').first()
        assert deleted_user is None