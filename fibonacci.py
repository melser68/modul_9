list_fib = []
count =0
check = True

def fibonacci(n): 
    global count
    global check

    while count <n and check == True:
        check = False
        fibonacci(count)        
    if check == False:    
        if count == 0:
            list_fib.append(0)
            count +=1
            check = True
        elif count == 1 or count == 2:
            list_fib.append(1)
            count +=1
            check = True
        else:
            list_fib.append(list_fib[count-1] + list_fib[count-2])
            count +=1
            check = True

    return list_fib    

print(fibonacci(0))
