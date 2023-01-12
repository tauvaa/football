import json
from functools import reduce
import os
import requests as req
def get_data():

    file_name = "data.json"
    if file_name not in os.listdir():
        with open("season2022") as f:
            data = f.readlines()
        data = map(lambda x: x.strip(), data)
        data = list(data)
        all_data = []
        counter = 0
        for url in data:
            res = req.get(url)
            all_data.append(res.json())
            counter += 1
            print(f"counter: {counter}")

        with open(file_name, "w+") as f:
            f.write(json.dumps(all_data))

    with open(file_name) as f:
        data = json.load(f)
    data = reduce(lambda x, y: x+y, data)

    return data
