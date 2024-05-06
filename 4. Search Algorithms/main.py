# sequence = input('Please provide a sequence of numbers, denote the different numbers with a "space"\n> ')
# sequence = sequence.split(' ')
# number = int(input("Which number would you like to find?\n> "))

# # Linear search
# for i in sequence:
#   if i == number: 
#     print("Number EXISTS!")

# seq = list(map(int, input('Please provide a sequence of numbers, denote the different numbers with a "space"\n> ').split()))
# number = int(input("Which number would you like to find?\n> "))


# for i in range(0, len(seq)):
#   if seq[i] == number:
#     print("Im really smart")

# Binary Search
def binSearch(li, low, high, target):
  midpoint = (low+high)//2 # floor division, means to the base value, minimum integer
  midvalue = li[midpoint]
  if low <= high:
    if midvalue > target:
      high = midpoint - 1
      return binSearch(li, low, high, target)
    elif midvalue < target:
      low = midpoint + 1
      return binSearch(li, low, high, target)
    elif midvalue == target:
      print("Found it! "+str(target)+" is in the "+str(midpoint)+"th index")
    else:
      print("The target is not in the list")


binSearch([1,2,3,4,5,6,7,8,9], 0, 8, 4)