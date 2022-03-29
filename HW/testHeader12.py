import requests

class TestHW12:

    def test_header_method(self):
        response = requests.post(
            "https://playground.learnqa.ru/api/homework_header"
        )
        x_secret_hw_value = response.headers['x-secret-homework-header']
        excepted_result = "Some secret value"

        assert x_secret_hw_value == excepted_result, \
            f"Wrong 'x-secret-homework-header' value in response. Actual value: {x_secret_hw_value}"