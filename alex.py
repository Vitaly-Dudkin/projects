import requests


def boo(answer, question, difficult):
    print(answer, question, difficult)

# def foo(kwargs):
#     print(**kwargs)

URL_TO_JSON_BIN = 'https://api.npoint.io/384b56bc7ab906f053b6'

response = requests.get(URL_TO_JSON_BIN).json()

# for obj in response:
#     print(obj)
#     boo(**obj)

boo(difficult=4, answer=6, question="hi")
