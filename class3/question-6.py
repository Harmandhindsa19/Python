#stack implementation
stack=[1,4,5,7,9,0]
print("the entered stack is:" , stack)
stack.append(10)
stack.append(11)
print("stack after insertion" , stack)
del stack[0]
print("stack after deletion is:", stack)
#queue implementation
queue=[6,7,8,9,3,3]
print("the entered queue is:" , queue)
queue.insert(0,8)
queue.insert(0,9)
print("queue after insertion is:" , queue)
del queue[0]
print("queue after deletion is:", queue)
