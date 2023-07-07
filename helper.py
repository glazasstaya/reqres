import json
import logging
import os.path

import allure
from allure_commons.types import AttachmentType
from requests import Session, Response
from curlify import to_curl


def load_json_schema(file_name):
    schema_path = os.path.join(os.path.dirname(__file__), 'schemas', file_name)
    with open(schema_path) as schema:
        return json.loads(schema.read())


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method = method, url = self.base_url + url, *args, **kwargs)
        curl = to_curl(response.request)
        logging.info(curl)
        with allure.step(f'{method} {url}'):
            allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
            return response

reqres_session = CustomSession('https://reqres.in/')
