import requests
from writeResponseIntoJsonFile import handleResponse
from myurls import MY_URLS
import ansiEscapeCodes

ITEM_ID = 1

def readItem(id:int):
    OUT_FILENAME = f"out/Item{id}.json"
    r = requests.get(MY_URLS.viewItem(id))
    if (r.status_code == 404):
        print(f"{ansiEscapeCodes.RED} Requested Item id:{id} not found")
        raise Exception("Requested resource not found")
    elif (r.status_code == 200):
        handleResponse(data=r.json()["data"], filename=OUT_FILENAME, req_url=MY_URLS.viewItem(id))
        return
    else:
        raise Exception("Unknown error happened")
    
if __name__ == "__main__":
    readItem(ITEM_ID)