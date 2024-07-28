def extract_rear_elements(tuple_string):
     return [string[-1] for string in tuple_string]

tuple_string = ("python", "learn", "includehelp")
result = extract_rear_elements(tuple_string)
print(result)  