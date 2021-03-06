# taken directly from https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/User-Lookup/get_users_with_bearer_token.py
# modified to work for our purposes.
import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url(username):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames="+username
    user_fields = "user.fields=created_at,description,id,name,username"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main1(username):
    bearer_token = auth()
    url = create_url(username)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    return json.dumps(json_response, indent=4, sort_keys=True)


# if __name__ == "__main__":
#     main(username)