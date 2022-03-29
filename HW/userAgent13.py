import json

import pytest
import requests


class TestHW13:
    url = "https://playground.learnqa.ru/api/"
    user_agent_values = {
        "user_agent_1":  "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "user_agent_2":  "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "user_agent_3":   "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "user_agent_4":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "user_agent_5": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }

    expected = {
        "exp_result_1" : {
            "platform": "Mobile",
            "browser": "No",
            "device": "Android"},
        "exp_result_2" : {
            "platform": "Mobile",
            "browser": "Chrome",
            "device": "iOS"},
        "exp_result_3" : {
            "platform": "Googlebot",
            "browser": "Unknown",
            "device": "Unknown"},
        "exp_result_4" : {
            "platform": "Web",
            "browser": "Chrome",
            "device": "No"},
        "exp_result_5" : {
            "platform": "Mobile",
            "browser": "No",
            "device": "iPhone"}
    }
    expected_results = [
        (user_agent_values["user_agent_1"],
         expected["exp_result_1"]["platform"],
         expected["exp_result_1"]["browser"],
         expected["exp_result_1"]["device"]),
        (user_agent_values["user_agent_2"],
         expected["exp_result_2"]["platform"],
         expected["exp_result_2"]["browser"],
         expected["exp_result_2"]["device"]),
        (user_agent_values["user_agent_3"],
         expected["exp_result_3"]["platform"],
         expected["exp_result_3"]["browser"],
         expected["exp_result_3"]["device"]),
        (user_agent_values["user_agent_4"],
         expected["exp_result_4"]["platform"],
         expected["exp_result_4"]["browser"],
         expected["exp_result_4"]["device"]),
        (user_agent_values["user_agent_5"],
         expected["exp_result_5"]["platform"],
         expected["exp_result_5"]["browser"],
         expected["exp_result_5"]["device"])
    ]

    @pytest.mark.parametrize('user_agent,platform,browser,device',expected_results)
    def test_check_user_agent(self,user_agent,platform,browser,device):


        response = requests.get(
            self.url+"user_agent_check",
            headers={"User-Agent": user_agent}
            )
        actual_platform = response.json()["platform"]
        actual_browser = response.json()["browser"]
        actual_device = response.json()["device"]

        assert platform == actual_platform, f"Response parameter 'platform' are NOT correct: {actual_platform}. Expected: {platform}"
        assert browser == actual_browser,f"Response parameter 'browser' are NOT correct: {actual_browser}. Expected: {browser}"
        assert device == actual_device, f"Response parameter 'browser' are NOT correct: {actual_device}. Expected: {device}"