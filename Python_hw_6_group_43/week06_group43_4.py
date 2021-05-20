#  import necessary modules
import json

# open json file
with open("06_bonus_random_user.json", "r") as random_user:
    # 1. json.loads() parses from json string to python dictionary (deserialization)
    # 2. use json.load() to encode from json file to python dictionary
    py_dict = json.load(random_user)
    print("The output type is", type(py_dict))

    # 3. change first and last name
    py_dict["results"][0]["name"]["first"] = "Max"
    py_dict["results"][0]["name"]["last"] = "Mustermann"
    # name changed
    print(py_dict["results"][0]["name"])

    # 4. json.dumps() converts a python object into a json string
    json_string = json.dumps(py_dict, indent=2)
    print("The output type is", type(json_string))

    # 5. saving random Max Mustermann to json file
    with open("max_mustermann.json", "w") as mm:
        json_string = json.dump(py_dict, mm, indent=2)

    # 6. Probably using the ultra json (usjon) module instead of json,
    # as it is an ultra fast json encoder/decoder written in C
    # (https://stackoverflow.com/questions/27407430/how-to-speed-up-process-of-loading-and-reading-json-files-in-python)
