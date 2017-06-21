#function to display stack
def DisplayStack():
    print("Current Items in stack")
    for item in stack:
        print(item)
#function to push element into stack
def Push(value):
    if len(stack) < StackSize:
        stack.append(value)
    else:
        print("Stack is full")
#function to pop element
def Pop(value):
    if len(stack) > 0:
        stack.pop(value)
    else:
        print("Stack is already empty")



s = raw_input("enter characters")
len1 = len(s)
stack = []
StackSize = len1


if len(stack) <= 0:
     for i in range(0,len1):
         if stack[i] != stack [i+1] and s[i] not in stack:
            Push(s[i])
            print  "Element added: " +s[i]
         else:
            print "Element already exist: " +s[i]

DisplayStack()

















