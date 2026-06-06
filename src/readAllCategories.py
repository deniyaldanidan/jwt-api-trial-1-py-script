import requests
from writeResponseIntoJsonFile import handleResponse
from myurls import MY_URLS

OUT_FILENAME = "out/allCategories.json"


# def handleResponse(res):
#     with open(OUT_FILENAME, "w") as out:
#         out.write(json.dumps(res["data"], indent=2))
#     print(f"Output of {ALL_CATEGORIES_URL} written on {OUT_FILENAME}")



def readAllCategories():
    req = requests.get(MY_URLS.allCategories)
    if (req.ok):
        handleResponse(data=req.json()["data"], filename=OUT_FILENAME, req_url=MY_URLS.allCategories)
    

if __name__ == "__main__":
    readAllCategories()