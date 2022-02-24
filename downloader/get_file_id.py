string = input(" Enter link : ")
lst = []
for i in string:
    lst.append(i)

lst2 = lst[25:]

file_id = ""
for i in lst2:
    if i == "/":
        break;
    else:
        file_id += i
print(file_id)
    
        
