def first_task(number):
    result = ""
    for i in range(number):
        text = ""
        for count in range(i + 1):
            text += f"{i+1}"
        result += f"{text}\n"
    return result
        

print(first_task(9))
