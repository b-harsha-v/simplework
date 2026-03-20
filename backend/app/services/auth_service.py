import requests

GOOGLE_TOKEN_INFO_URL = "https://oauth2.googleapis.com/tokeninfo"


def verify_google_token(id_token):

    response = requests.get(
        GOOGLE_TOKEN_INFO_URL,
        params={"id_token": id_token}
    )

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "email": data.get("email"),
        "name": data.get("name")
    }