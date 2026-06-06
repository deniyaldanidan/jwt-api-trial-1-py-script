import requests
from myurls import MY_URLS
from custHeaders import CONTENT_TYPE_JSON_HEADER

# These are just localhost demo passwords so no problemzzz
UNAME = "mr_admin"
PASSWORD = "password"


def loginAsAdmin():
    s = requests.Session();
    r = s.post(MY_URLS.logIn, json={"unameOrEmail": UNAME, "pwd": PASSWORD}, headers=CONTENT_TYPE_JSON_HEADER)
    if (r.ok):
        s.headers.update({"Authorization": f"Bearer {r.json()["auth"]}"})
        return s
    else: 
        # print("login as admin failed")
        print(r.json())
        raise Exception("Login as admin failed")
        
