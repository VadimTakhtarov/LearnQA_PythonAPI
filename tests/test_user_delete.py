import pytest

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):

    def test_delete_admin_user(self):
        # LOGIN BY USER
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = MyRequests.post(
            "/user/login",
            data=login_data
        )

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE
        response2 = MyRequests.delete(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_text(
            response2,
            "Please, do not delete test users with ID 1, 2, 3, 4 or 5.")

        # GET . CHECK THAT ADMIN USER NOT DELETED
        response4 = MyRequests.get(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response4, 200)


    def test_delete_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(
            "/user/",
            data=register_data
        )

        Assertions.assert_code_status(response1,200)
        Assertions.assert_json_has_key(response1,"id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1,"id")


        # LOGIN
        login_data = {
            "email" : email,
            "password" : password
        }

        response2 = MyRequests.post(
            "/user/login",
            data=login_data
        )

        auth_sid = self.get_cookie(response2,"auth_sid")
        token = self.get_header(response2,"x-csrf-token")

        # DELETE
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid":auth_sid},
        )
        Assertions.assert_code_status(response3,200)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response4,404)
        Assertions.assert_response_text(response4,"User not found")

    def test_edit_just_created_user_without_authorization(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(
            "/user/",
            data=register_data
        )

        Assertions.assert_code_status(response1,200)
        Assertions.assert_json_has_key(response1,"id")

        user_id = self.get_json_value(response1,"id")

        # EDIT
        new_name = "Changed Name"

        response2 = MyRequests.put(
            f"/user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response2,400)
        Assertions.assert_response_text(response2,"Auth token not supplied")

    def test_delete_user_by_other_authorizated_user(self):
        # REGISTER FOR USER1
        user1_register_data = self.prepare_registration_data()
        response1 = MyRequests.post(
            "/user/",
            data=user1_register_data
        )

        Assertions.assert_code_status(response1,200)
        Assertions.assert_json_has_key(response1,"id")

        user1_email = user1_register_data["email"]
        user1_first_name = user1_register_data["firstName"]
        user1_password = user1_register_data["password"]
        user1_user_id = self.get_json_value(response1,"id")

        # REGISTER FOR USER2
        user2_register_data = self.prepare_registration_data()
        response2 = MyRequests.post(
            "/user/",
            data=user2_register_data
        )

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        user2_email = user2_register_data["email"]
        user2_first_name = user2_register_data["firstName"]
        user2_password = user2_register_data["password"]
        user2_user_id = self.get_json_value(response2, "id")

        # LOGIN BY USER2
        login_data = {
            "email" : user2_email,
            "password" : user2_password
        }

        response3 = MyRequests.post(
            "/user/login",
            data=login_data
        )

        user2_auth_sid = self.get_cookie(response3,"auth_sid")
        user2_token = self.get_header(response3,"x-csrf-token")

        # DELETE USER1 WITH USER2 AUTHORIZATION . CHECK THAT USER1 CAN'T BE DELETED WITH USER2 AUTH DATA
        new_name = "Changed Name"

        response4 = MyRequests.delete(
            f"/user/{user1_user_id}",
            headers={"x-csrf-token":user2_auth_sid},
            cookies={"auth_sid":user2_token}
        )
        Assertions.assert_code_status(response4,400)
        Assertions.assert_response_text(response4,"Auth token not supplied")

        # LOGIN BY USER1. CHECK THAT USER1 NOT DELETED
        login_data = {
            "email": user2_email,
            "password": user2_password
        }

        response5 = MyRequests.post(
            "/user/login",
            data=login_data
        )
        Assertions.assert_code_status(response5,200)
        Assertions.assert_json_has_key(response5,"user_id")
