# Implementing a JSON data in Python  
Javascript Object Notation      
JSON data is commonly used for configuration files, storing some type of data or commonly for API  
Syntax of a Json is very similar to a python dictionary.  
For example,   
```python  
import json  
json_string = '''  
  {  
    "students": [  
      {
        "id": 1,
        "name": "Tim",
        "age": 21
      },
      {
        "id": 2,
        "name": "Jim",
        "age": 20 
      }
    ]
  }
'''

data = json.loads(json_string)                         # load(s) because we are loading string
print(data)
print(data['students'])
print(data['students'][0])

```   
Output:    
{'students': [{'id': 1, 'name': 'Tim', 'age': 21}, {'id': 2, 'name': 'Jim', 'age': 20}]}    
[{'id': 1, 'name': 'Tim', 'age': 21}, {'id': 2, 'name': 'Jim', 'age': 20}]  
{'id': 1, 'name': 'Tim', 'age': 21}  

The output is printed as a python dictionary.  
=================================================================================================================  
### Printing specifics:  
**Example**     
for student in data['students']:    
  print (student)    
    
Output:    
{'id': 1, 'name': 'Tim', 'age': 21}    
{'id': 2, 'name': 'Jim', 'age': 20}  


**Example**  
for student in data['students']:    
  print (student['name'])  
  
Output:  
Tim  
Jim    
  
=================================================================================================================  
### Dump a Python Dictionary into Json Format  
  
data['test'] = True  
  
new_json = json.dumps(data, indent=2, sort_keys=True)  
print(new_json)  
  
Output:  
```json  
{
  "students": [
    {
      "age": 21,
      "id": 1,
      "name": "Tim"
    },
    {
      "age": 20,
      "id": 2,
      "name": "Jim"
    }
  ],
  "test": true
}
```  
  
indent gives an indentation of 2    
sort_keys sorts keys in alphabetical order    
  
==================================================================================================  
### Working with JSON File  
#### Load Json data from a file  
  
We will import json, and then open the file values.json in a read only mode  
```python  
import json  
 
with open("values.json", "r") as f:     # open it in read mode
  data = json.load(f)

print(data)
```
  
#### Dump Json to a file  
  
import json  
  
with open("values2.json", "w") as f:     # open it in write mode as we are creating a new file  
  json.dump(data, f)  
  
  
==================================================================================================

### Getting a JSON from a url
```python

import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

print(response.text)

```

=============================================================================
