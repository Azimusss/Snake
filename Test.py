import json, os
import settings
from Classes.TextBox import *

top = [
    {
        "name": "Vasya",
        "score": 1000
    },
    {
        "name": "Petya",
        "score": 450
    },
    {
        "name": "Kolya",
        "score": 100
    }]

name = main()
print(name)

top.append({"name": str(name), "score": 900})

print(top)

print(sorted(top, key=lambda x: x["score"], reverse=True)[:9])

#####################################################################

# lst = ['v', 'a', 's', 'y', 'a']
# str = str.join(" ", lst)
# print(str)

#####################################################################

# with open(os.path.join(settings.DATA_DIR, 'Top_Records.json')) as f:
#             top = json.load(f)

