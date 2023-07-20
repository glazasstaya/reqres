import allure
import pytest
from model.utils.helper import load_json_schema, reqres_session, reqres_responce


@pytest.mark.parametrize('page',[1, 2])
@allure.feature('API: get user list')
@allure.story('API: get user list success')
def test_users_list_page(page):
    payload = {'page': page}
    response = reqres_session.get('api/users/', params=payload)
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        with allure.step(f'В ответе есть page = {page}'):
            assert 'page' in response_json
            assert response_json['page'] == page


@pytest.mark.parametrize('page',[1, 2])
@allure.feature('API: get user list')
@allure.story('API: get user list count')
def test_users_list_data_count(page):
    payload = {'page': page}
    response = reqres_session.get('api/users/', params=payload)
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        with allure.step(f'Количество пользователей в списке <= 6'):
            assert 'data' in response_json
            assert len(response_json['data']) <= 6


@allure.feature('API: get user list')
@allure.story('API: get user list schema validate')
def test_users_list_schema_validate():
    payload = {'page': 1}
    response = reqres_session.get('api/users/', params=payload)
    schema = load_json_schema('get_user_list.json')

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)