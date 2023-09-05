from apipage import post_presence, create_check_new_post
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_post_presence(get_token_auth):
    assert data["owner_title_name"] in post_presence(get_token_auth)

def test_create_check_new_post2(get_token_auth):
    assert data["description2"] in create_check_new_post(get_token_auth)