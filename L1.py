def count_lines():
    count = 0

    while True:
        s = input("Enter line: ")
        
        if s == "END":
            break
        
        if  not s.startswith("T"):
            count += 1
        else:
            count=count
    return count

print("no of lines  not starting with T :",count_lines())
      
 
