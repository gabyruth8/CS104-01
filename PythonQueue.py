#PythonProgramSimulatingQueueatBank

names = []

for x in range(10):
    acceptedName = input("Enter a name: ")
    names.append(acceptedName)

print(names)

for x in range(len(names)):
    print(names.pop(0))

print(names)
    
