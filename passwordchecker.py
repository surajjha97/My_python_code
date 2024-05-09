import requests
import hashlib

def request_api_data(first5_char):
    url = 'https://api.pwnedpasswords.com/range/' + first5_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return response

def read_res(response):
    print(response.text)

response = pwned_api_check('suraj')
read_res(response)