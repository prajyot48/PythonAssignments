def parse_string(s):
    parts = list(filter(None, s.split('0')))
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }
encoded = "Robert000Smith000123"
print(parse_string(encoded))
