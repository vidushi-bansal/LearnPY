
import json

with open("values.json", "r") as f:     # open it in read mode
  data = json.load(f)

print(data)
