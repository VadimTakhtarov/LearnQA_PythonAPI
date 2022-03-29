import requests


class TestHW11:

    def test_cookie(self):
        response = requests.post(
            "https://playground.learnqa.ru/api/homework_cookie"
        )

        assert response.cookies['HomeWork'] == 'hw_value', \
            f"Incorrect response cookie: {response.cookies['HomeWork']}"