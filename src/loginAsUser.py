import requests
from myurls import MY_URLS
from custHeaders import CONTENT_TYPE_JSON_HEADER
import ansiEscapeCodes

SIGNUP_CREDENTIALS = {
    "username": "anna",
    "email": "anna0z@gmail.com",
    "password": "password"
}
LOGIN_CREDENTIALS = {
    "unameOrEmail": "anna0z@gmail.com",
    "pwd": "password"
}

def signUp():
    s = requests.Session()
    r = s.post(MY_URLS.signUp, json=SIGNUP_CREDENTIALS, headers=CONTENT_TYPE_JSON_HEADER)
    if (r.ok):
        print(f"{ansiEscapeCodes.GREEN}Signed Up as User{ansiEscapeCodes.RESET}")
        s.headers.update({"Authorization": f"Bearer {r.json()["auth"]}"})
        return s
    else:
        print(f"{ansiEscapeCodes.RED}SigingUp failed{ansiEscapeCodes.RESET}")
        raise Exception("SignUp Failed")

def signIn():
    s = requests.Session();
    r = s.post(MY_URLS.logIn, json=LOGIN_CREDENTIALS, headers=CONTENT_TYPE_JSON_HEADER)
    if (r.status_code == 404):
        print (f"{ansiEscapeCodes.YELLOW}Login Failed Trying Signing Up{ansiEscapeCodes.RESET}")
        return signUp()
    elif (r.ok):
        print(f"{ansiEscapeCodes.GREEN}Logged in as User{ansiEscapeCodes.RESET}")
        s.headers.update({"Authorization": f"Bearer {r.json()["auth"]}"})
        # print(s.cookies.get("refresh"))
        return s
    else:
        print(f"{ansiEscapeCodes.RED}Log In failed{ansiEscapeCodes.RESET}")
        raise Exception("Sign In Failed")
    