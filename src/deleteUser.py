from requests import Session
from loginAsUser import signIn
from myurls import MY_URLS
import ansiEscapeCodes

def deleteUser(s:Session):
    r = s.delete(MY_URLS.deleteUser)
    if (r.status_code == 200):
        print(f"{ansiEscapeCodes.GREEN}User is Deleted{ansiEscapeCodes.RESET}")
    else:
        raise Exception("User deletion failed")
    
    
if __name__ == "__main__":
    s= signIn()
    deleteUser(s)