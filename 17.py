def new_string(str):
    if len(str)>=2 and str[:2]=="Is":
        return str
    return "IS"+str
print(new_string("array"))
print(new_string("Isempty"))
