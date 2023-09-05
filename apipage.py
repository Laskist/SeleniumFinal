import logging
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def post_presence(get_token_auth):
    logging.debug('Open posts page')
    header = {
        "X-Auth-Token": get_token_auth
    }
    body = {
        "owner": "notMe"
    }
    r = requests.get(data["url_api"], params=body, headers=header).json()["data"]
    if r:
        name = [i["title"] for i in r]
        return name
    else:
        logging.error('Страница с постами не открылась')


def create_check_new_post(get_token_auth):
    logging.debug('Open posts page')
    header = {
        "X-Auth-Token": get_token_auth
    }
    body = {
        "title": data["title2"],
        "description": data["description2"],
        "content": data["content2"]
    }
    r = requests.post(data["url_api"], data=body, headers=header)
    con = requests.get(data["url_api"], data=body, headers=header).json()["data"]
    if con:
        description = [i['description'] for i in con]
        return description
    else:
        logging.error('Пост не найден')