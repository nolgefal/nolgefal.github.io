import os
import http.client, urllib.parse, json, urllib.request
import random

# check your subscription key from M$
subscriptionKey = "a8023918783642b89970a4820d43ed6d"
# key 2: "ec63751ee8744d7fa28c7cb8fc446833"

host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/images/search"

# keywords
term = ["Ung Hoang Phuc", "My Tam",
        "Khanh Phuong",   "Tam Tit",
        "Phan Dinh Tung", "Cam Ly",
        "Phan Manh Quynh","Le Cat Trong Ly",
        "Minh Thuan",     "Ho Quynh Huong",
        "Sơn Tung MTP",   "Hien Thuc",
        "Ha Anh Tuan",    "Bao Thy",
        "Ngo Kien Huy",   "Le Quyen",
        "Lam Trưong",     "Van Mai Huong",
        "Tuan Hung",      "Hong Nhung",
        "Dan Nguyen",     "Lan Huong",
        "Dam Vinh Hung",  "Thuy Chi",
        "Nguyen Phi Hung","Minh Hang",
        ]

def BingImageSearch(search):
    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(search)
    conn.request("GET", path + "?q=" + query + '&count=30', headers=headers)
    response = conn.getresponse()
    # headers = [k + ": " + v for (k, v) in response.getheaders() if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return response.read().decode("utf8")

def findAll(term, paths):
    print('Searching images for: ', term)
    result = BingImageSearch(term)
    print("\nJSON Response:\n")
    tt = json.loads(result)

    for e in tt['value']:        
        print(e['contentUrl'])
        try:
            urllib.request.urlretrieve(str(e['contentUrl']), paths + str(random.randint(0,10000)) + ".jpg")        
        except:
            print("Error at: ", e['contentUrl'])

if len(subscriptionKey) == 32:
    dir0 = "/media/lhlong/01D309ADC81A8610/lhlong/ML/work/self/object detection/Celeb_Face_VN"

    for e in term:

        # create folder to save images
        directory = dir0 + "/" + e + "/"

        # create forder
        if not os.path.exists(directory):
            os.makedirs(directory)

        findAll(e, directory)

else:
    print("Invalid Bing Search API subscription key!")
    print("Please paste yours into the source code.")