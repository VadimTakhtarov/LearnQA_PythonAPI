import json.decoder
from _datetime import datetime

from requests import Response

class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header with name {header_name} in the last response"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is \"{response.text}\""

        assert name in response_as_dict, f"Response JSON doesn't have key \"{name}\""

        return response_as_dict[name]

    def prepare_registration_data(
            self,
            email=None,
            password=None,
            username=None,
            firstname=None,
            lastname=None):
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        if password is None:
            password = '123'
        if username is None:
            username = f"LearnQA_Username{random_part}"
        if firstname is None:
            firstname = f"LearnQA_FirstName{random_part}"
        if lastname is None:
            lastname = f"LearnQA_LastName{random_part}"
        if email is None:
            base_part = "LearnQA"
            domain = "example.com"
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': password,
            'username': username,
            'firstName': firstname,
            'lastName': lastname,
            'email': email
        }