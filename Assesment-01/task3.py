def format_string(*args):
    val1 = args[0]
    val2 = args[1:]
    
    finalString = ""
    indexNo = 0
    
    i = 0
    while i < len(val1):
        
        if(val1[i] == '!' and i+2 < len(val1) and val1[i+1]=='{' and val1[i+2] == '}'):
            finalString += str(val2[indexNo])
            indexNo += 1
            i+=3
        elif (val1[i] == '{' and i+1 < len(val1) and val1[i+1] == '}'):
            finalString += str(val2[indexNo])
            indexNo += 1
            i += 2
        else:
            finalString += val1[i]
            i+=1
    
    return finalString

print(format_string("Hello, {}!", "John"))
# Output: "Hello, John!"
print(format_string("Today is {} and the temperature is {} degrees.", "Monday", 25))
# Output: "Today is Monday and the temperature is 25 degrees."