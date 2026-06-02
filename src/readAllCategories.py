import requests
import json
from myurls import MY_URLS

ALL_CATEGORIES_URL = MY_URLS["allCategories"]
OUT_FILENAME = "out/allCategories.json"


def handleResponse(res):
    with open(OUT_FILENAME, "w") as out:
        out.write(json.dumps(res["data"], indent=2))
    print(f"Output of {ALL_CATEGORIES_URL} written on {OUT_FILENAME}")



def main():
    req = requests.get(ALL_CATEGORIES_URL)
    if (req.ok):
        handleResponse(req.json())
    

if __name__ == "__main__":
    main()