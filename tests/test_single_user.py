import allure
import pytest
from helper import load_json_schema, reqres_session, reqres_responce


@pytest.mark.parametrize('user_id',[1, 2])
@allure.feature('API: get user')
@allure.story('API: get user success')
def test_get_user_success(user_id):
    response = reqres_session.get(f'api/users/{user_id}')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)

    if response_json != '':
        with allure.step(f'В ответе есть user_id = {user_id}'):
            assert 'data' in response_json, 'В ответе нет поля "data"'
            assert 'id' in response_json['data'], 'В ответе нет поля "id'
            assert response_json['data']['id'] == user_id, 'В ответе нет поля "user_id'


@allure.feature('API: get user')
@allure.story('API: get user not found')
def test_user_not_found():
    user_id = 23
    response = reqres_session.get(f'api/users/{user_id}')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 404)

    if response_json != '':
        with allure.step(f'В ответе пустой json'):
            assert response_json == {}



@allure.feature('API: get user')
@allure.story('API: get user schema validate')
def test_user_json_schema_validate():
    user_id = 1
    response = reqres_session.get(f'api/users/{user_id}')

    schema = load_json_schema('get_single_user.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)




