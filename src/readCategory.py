import requests
from writeResponseIntoJsonFile import handleResponse
from myurls import MY_URLS
import ansiEscapeCodes

CATEGORY_ID = 3

def readCategory(id:int):
    OUT_FILENAME = f"out/category{id}.json"
    r = requests.get(MY_URLS.viewCategory(id))
    if (r.status_code == 404):
        print(f"{ansiEscapeCodes.RED} Requested Category id:{id} not found")
        raise Exception("Requested resource not found")
    elif (r.status_code == 200):
        handleResponse(data=r.json()["data"], filename=OUT_FILENAME, req_url=MY_URLS.viewCategory(id))
        return
    else:
        raise Exception("Unknown error happened")
    
if __name__ == "__main__":
    readCategory(CATEGORY_ID)