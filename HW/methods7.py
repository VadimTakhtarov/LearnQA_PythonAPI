import requests

methods = ["POST","GET","PUT","DELETE","Wrong method",""]
api_url = "https://playground.learnqa.ru/api/compare_query_type"

for method in methods:
    get_response = requests.get(
        api_url,
        params={'method': f"{method}"})
    print(f"GET request with parameter 'method' : {method}")
    print(f"Response code: {get_response.status_code}")
    print(f"Response text: {get_response.text}")
    print("-----------------")

    post_response = requests.post(
        api_url,
        data={'method': f"{method}"})
    print(f"POST request with parameter 'method' : {method}")
    print(f"Response code: {post_response.status_code}")
    print(f"Response text: {post_response.text}")
    print("-----------------")

    put_response = requests.put(
        api_url,
        data={'method': f"{method}"})
    print(f"PUT request with parameter 'method' : {method}")
    print(f"Response code: {put_response.status_code}")
    print(f"Response text: {put_response.text}")
    print("-----------------")


    delete_response = requests.delete(
        api_url,
        data={'method': f"{method}"})
    print(f"DELETE request with parameter 'method' : {method}")
    print(f"Response code: {delete_response.status_code}")
    print(f"Response text: {delete_response.text}")
    print("-----------------")