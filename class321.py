# nameStr = input("Name: ")
# age = eval(input("age: "))
# 
# for i in range (0,10):
#   if(i % 2 == 1):
#     print("Found an odd. Breaking")
#     break
#   else:
#     print(i)
#   
# for i in range (0,10):
#   if(i % 2 == 1):
#     print("Skip Odds")
#     continue
#   else:
#     print(i)
# 
# inFile = open("inputFile.txt", "r")
# for line in inFile:
#   print(line.rstrip("\n"))
#   
# inFile.close()

# outFile = open("outputFile.txt", "w")
# outFile.write("Hello World")
# outFile.close()

# outFile = open("outputFile.txt", "a")
# outFile.write("\nHello World")
# outFile.close()
# 
# l = ["a", "b", "c", 2, 4.3]
# for i in l:
#   print (i)
#   
# for i in range(len(l)):
#   print(l[i])

phoneNums = {}
phoneNums['Eric'] = '123-123-1233'
phoneNums['Daniel'] = '456-234-2343'

for num in phoneNums:
  print(phoneNums[num])