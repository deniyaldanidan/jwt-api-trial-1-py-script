import requests
import json
from myurls import MY_URLS

OUT_FILENAME = "out/allItems.json"
ALL_ITEMS_URL = MY_URLS['allItems']

def handleResponse(res):
    with open(OUT_FILENAME, "w") as out:
        out.write(json.dumps(res["data"], indent=2))
        
    print(f"Output for {ALL_ITEMS_URL} written in {OUT_FILENAME}")

def main():
    req = requests.get(ALL_ITEMS_URL)
    isSuccess = req.ok
    if (isSuccess):
        handleResponse(req.json())
        
        
if __name__ == "__main__":
    main()

