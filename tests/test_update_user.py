import allure
import pytest
from model.utils.helper import load_json_schema, reqres_session, reqres_responce

@pytest.mark.parametrize('name, job',[('John', 'trader'), ('Иван', 'инвестор')])
@allure.feature('API: update user')
@allure.story('API: update user success')
def test_user_update_success(name, job):
    user_id = 2
    payload = {"name": name, "job": job}
    response = reqres_session.put(f'api/users/{user_id}', json=payload)

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)

    if response_json != '':
        with allure.step(f'В ответе есть name = {name}, job = {job}'):
            assert 'name' in response_json
            assert response_json['name'] == name
            assert 'job' in response_json
            assert response_json['job'] == job



@allure.feature('API: update user')
@allure.story('API: update user schema validate')
def test_user_update_json_schema_validate():
    id = 2
    payload = {"name": "morpheus", "job": "zion resident"}
    response = reqres_session.put(f'api/unknown/{id}', json=payload)

    schema = load_json_schema('put_user.json')
    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 200)
    if response_json != '':
        reqres_responce.responce_schema_validate(response_json, schema)