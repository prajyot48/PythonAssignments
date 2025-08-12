def run_length_encode(s):
    encoded = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        encoded += s[i] + str(count)
        i += 1
    return encoded

input_str = "wwwwaaadebbbbbw"
print(run_length_encode(input_str)) 
