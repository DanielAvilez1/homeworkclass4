import requests

URL = "http://127.0.0.1:5000/users"


def deactivate_user(id):

    url = URL = "/"+id

    response = requests.delete(url)
    if response.status_code == 204:
        print(
            "Successfully removed record ; Got: %d" % id
            % response.json().get("message")
        )
