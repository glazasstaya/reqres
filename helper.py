import json
import logging
import os.path

import allure
from allure_commons.types import AttachmentType
from requests import Session, Response
from curlify import to_curl
from jsonschema import validate


def load_json_schema(file_name):
    schema_path = os.path.join(os.path.dirname(__file__), 'schemas', file_name)
    with open(schema_path) as schema:
        return json.loads(schema.read())


class ReqresResponce():

    def responce_status_chek(self, status_code, expected_status):
        with allure.step(f'Статус ответа: {status_code}'):
            assert status_code == expected_status, f'Статус ответа {status_code}'


    def responce_schema_validate(self, response_json, schema):
        with allure.step('Валидация схемы ответа'):
            validate(instance=response_json, schema=schema)

    def responce_json_get(self, responce_content):
        response_json = ''
        try:
            response_json = responce_content.json()
        except json.JSONDecodeError:
            print('Ответ не в json формате')
        return response_json


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method = method, url = self.base_url + url, *args, **kwargs)
        print(args, kwargs)
        curl = to_curl(response.request)
        status = response.status_code
        status_curl = f'Код ответа: {status}, {curl}'
        logging.info(status_curl)

        with allure.step(f'{method} {url}'):
            params_attach_body = f' *args, **kwargs parametrs: {args} {kwargs}'
            allure.attach(body=params_attach_body, name='params', attachment_type=AttachmentType.TEXT, extension='txt')
            allure.attach(body=status_curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
            try:
                allure.attach(
                    body=json.dumps(response.json(), ensure_ascii=False, indent=2),
                    name='json',
                    attachment_type=AttachmentType.JSON,
                    extension='json'
                )
            except json.JSONDecodeError:
                allure.attach(body=response.text, name='text', attachment_type=AttachmentType.TEXT, extension='txt')

            return response

reqres_session = CustomSession('https://reqres.in/')
reqres_responce = ReqresResponce()

