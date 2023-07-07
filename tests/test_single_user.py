import requests
from jsonschema import validate
from helper import load_json_schema, reqres_session


def test_user_success():
    user_id = 2

    response = reqres_session.get(f'api/users/{user_id}')

    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id


def test_user_json_structure():
    user_id = 1
    response = reqres_session.get(f'api/users/{user_id}')

    schema = load_json_schema('get_single_user.json')

    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


