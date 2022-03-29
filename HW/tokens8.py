import requests
import time


status_response = "Job is NOT ready"
result_response = "Job is ready"
error_response = "No job linked to this token"
incorrect_token = "dfaf5f5sefs5f5effesf558"

response1 = requests.get("https://playground.learnqa.ru/api/longtime_job")
job_time = response1.json()['seconds']
job_token = response1.json()['token']

data = {
    'token': job_token
}
response2 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
     params=data
    )
if response2.json()['status'] == status_response:
    print(f"PASSED! Correct server answer, "
          f"when job is not ready: {response2.json()['status']}")
else:
    print(f"FAILED! Incorrect server answer "
          f"when jon is not ready: {response2.json()['status']}")
print(f"Response text: {response2.text}")

print("------------")
time.sleep(job_time)
response3 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
     params=data
    )

if response3.json()['status'] == result_response:
    print(f"PASSED! Correct server answer, "
          f"when job is ready: {response3.json()['status']}. Job time: {job_time}")
else:
    print(f"FAILED! Incorrect server answer "
          f"when jon is ready: {response3.json()['status']}. Job time: {job_time}")
print(f"Response text: {response3.text}")

print("------------")

response4 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
     params={'token': incorrect_token}
    )

if response4.json()['error'] == error_response:
    print(f"PASSED! Correct server answer about job, "
          f"when incorrect token in request: {response4.json()['error']}")
else:
    print(f"FAILED! Incorrect server answer about job, "
          f"when incorrect token in request: {response4.json()['error']}")
print(f"Response text: {response4.text}")