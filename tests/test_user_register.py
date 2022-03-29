import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response,"id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post( "/user", data=data )

        Assertions.assert_code_status(response,400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",\
            f"Unexpected response content: {response.content}"

    def test_create_user_with_email_without_dog_symbol(self):
        email = "vinkotovexample.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content: {response.content}"

    # Homework Ex15
    missing_parameters = {
    'username',
    'firstName',
    'lastName',
    'email',
    'password',
    }

    @pytest.mark.parametrize("missing_param",missing_parameters)
    def test_create_user_with_missing_parameters(self,missing_param):
        data = self.prepare_registration_data()
        data.pop(missing_param,None)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {missing_param}", \
            f"Unexpected response content: {response.content}"

    names = {
        # username with one symbol:
        "1",
        # username with 250 symbols:
        "teststringfornameteststringfornameteststringfornameteststringfornameteststringfornameteststringf"
        "ornameteststringfornameteststringfornameteststringfornameteststringfornameteststringfornameteststr"
        "ingfornameteststringfornameteststringfornameteststringfornametest"
    }
    @pytest.mark.parametrize("name", names )
    def test_create_user_with_different_username_str_length(self, name):
        data = self.prepare_registration_data(username=name)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)

        assert_text = "long" if len(name) > 250 else "short"

        assert response.content.decode("utf-8") == f"The value of 'username' field is too {assert_text}", \
                f"Unexpected response content: {response.content}"
