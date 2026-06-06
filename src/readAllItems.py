import requests
from myurls import MY_URLS
from writeResponseIntoJsonFile import handleResponse

OUT_FILENAME = "out/allItems.json"


def readAllItems():
    req = requests.get(MY_URLS.allItems)
    isSuccess = req.ok
    if (isSuccess):
        handleResponse(data=req.json()["data"], filename=OUT_FILENAME, req_url=MY_URLS.allItems)
        
        
if __name__ == "__main__":
    readAllItems()

