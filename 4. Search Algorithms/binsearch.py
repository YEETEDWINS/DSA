def binSearch(li, target):
  high = len(li)-1
  low = 0
  midpoint = (low+high)//2
  midvalue = li[midpoint]
  if low <= high:
    if midvalue > target:
      high = midpoint - 1
      return binSearch(li, target)
    elif midvalue < target:
      low = midpoint + 1
      return binSearch(li, target)
    elif midvalue == target:
      print("Found it! "+str(target)+" is in the "+str(midpoint)+"th index")
    else:
      print("The target is not in the list")

listing = list(map(int, input("Give me a list of numbers, denote the numbers with a space\n> ").split()))
targetting = int(input("Provide a number that needs to be found (or not)\n> "))

binSearch(listing, targetting)