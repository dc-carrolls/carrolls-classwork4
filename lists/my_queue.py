my_queue = []
max_size = 5

def enQueue(q, item):
    if not is_full(q):
        q.append(item)
    else:
        return "Full"
    #end if
#end procedure

def deQueue(q):
    if not is_empty(q):
        return q.pop(0)
    return "Empty"
    #end if
#end function

def is_empty(q):
    return len(q) == 0
#end function

def is_full(q):
    global max_size
    return len(q) == max_size
#end function


enQueue(my_queue,"Socks")
print(my_queue)
enQueue(my_queue,"Shoes")
print(my_queue)
enQueue(my_queue,"Hats")
print(my_queue)