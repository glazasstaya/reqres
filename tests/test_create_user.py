import allure
import pytest
from helper import load_json_schema, reqres_session, reqres_responce


@pytest.mark.parametrize('name, job',[('John', 'trader'), ('Иван', 'инвестор')])
@allure.feature('API: post user')
@allure.story('API: post user create success')
def test_user_create_success(name, job):
    payload = {"name": name, "job": job}
    response = reqres_session.post('api/users/', json=payload)

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 201)

    if response_json != '':
        with allure.step(f'В ответе есть name = {name}, job = {job}'):
            assert 'name' in response_json
            assert response_json['name'] == name
            assert 'job' in response_json
            assert response_json['job'] == job


@allure.feature('API: post user')
@allure.story('API: post user create success without name')
def test_user_create_success_without_name():
    job = "trader"
    payload = {"job": job}
    response = reqres_session.post('api/users/', json=payload)

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 201)

    if response_json != '':
        with allure.step(f'В ответе нет name, и есть job = {job}'):
            assert 'name' not in response_json
            assert 'job' in response_json
            assert response_json['job'] == job


@allure.feature('API: post user')
@allure.story('API: post user create success without job')
def test_user_create_success_without_job():
    name = "John"
    payload = {"name": name}
    response = reqres_session.post('api/users/', json=payload)

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 201)

    if response_json != '':
        with allure.step(f'В ответе есть name = {name}, и нет job'):
            assert 'name' in response_json
            assert response_json['name'] == name
            assert 'job' not in response_json


@allure.feature('API: post user')
@allure.story('API: post user create success without params')
def test_user_create_success_without_params():
    payload = {}
    response = reqres_session.post('api/users/', json=payload)

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 201)

    if response_json != '':
        with allure.step(f'В ответе нет name и job'):
            assert 'name' not in response_json
            assert 'job' not in response_json


@pytest.mark.parametrize('name, job',[('John', 'trader'), (None, None)])
@allure.feature('API: post user')
@allure.story('API: post user schema validate')
def test_user_create_success_schema_validate(name, job):
    if name == None and job == None:
        payload = {}
    else:
        payload = {"name": name, "job": job}

    response = reqres_session.post('api/users/', json=payload)
    schema = load_json_schema('post_create_user.json')

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 201)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)










