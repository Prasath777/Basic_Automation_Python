from asyncio.windows_events import NULL
from distutils import command
import sys
import clipboard
import json

SAVED_DATA="clipboard.json"

def save_data(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data=json.load(f)
            return data
    except:
        return {}        
    # save_items("test.json",{"key":"value"})

if len(sys.argv) == 2:
    command= sys.argv[1]
    data=load_data(SAVED_DATA)
    
    if command == "save":
        key=input("Enter a key: ")
        data[key]=clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data Saved")
    elif command == "load":
        key=input("Enter a key to load: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard") 
        else:
            print("Key does not exist ")    

    elif command == "list":
        print(data)
    elif command == "delete":
        key= input("Enter a key to be deleted: ")
        if key in data:
            data.pop(key)
            save_data(SAVED_DATA,data)
            print("Key deleted")
        else:
            print("Key does not exist")    
    else:
        print("Unknown command")        
else:
    print("Please, Enter exactly one command")        