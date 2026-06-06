from requests import Session
from myurls import MY_URLS
from loginAsUser import signIn
import ansiEscapeCodes


def refresh(s:Session):
    # print(s.cookies.get("refresh"))
    r = s.put(MY_URLS.refresh)
    if (r.status_code == 200):
        print (f"{ansiEscapeCodes.GREEN}New auth-token: {ansiEscapeCodes.BOLD}{r.json()["auth"]}{ansiEscapeCodes.RESET}")
        s.headers.update({"Authorization": f"Bearer {r.json()["auth"]}"})
        return s
    else:
        print(r.json())
        raise Exception("Refresh failed")
    
    
if __name__ == "__main__":
    s = signIn()
    refresh(s)