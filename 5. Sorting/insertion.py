import copy
# l1 = [4, 2, 578, 28, 32, 21]
# l1.sort()
# l2 = [5, 372, 478, 3, 271, 43]
# l3 = sorted(l2, reverse = True)
# the sort() function will modify the list it is called on. 
# The sorted() function will create a new list containing a sorted version of the list it is given


# def Insertion(lis):
#   sortedL = []
#   for i in range(0, len(lis)):
#     main = lis[i]
#     secondary = lis[i+1]
#     if main < secondary:
#       sortedL.append(lis[i])
#     elif main > secondary:
#       a = 1
#       b = 2
#       #swap a and b
#       t = a # t = 1
#       a = b # a = 2
#       b = t # b = 1
l1 = [5, 448, 291, 282, 433, 8, 2839, 22, 43] # creating variable in memory
# l2 = copy.copy(l1)
# l2.append(10) # 
# print(l2)
# print(l1)

def Insertion(lis):
  for i in range(1, len(lis)):
    current = lis[i]
    j = i-1
    while j >= 0 and current < lis[j]:
      lis[j+1] = lis[j]
      j -= 1
    lis[j+1] = current
  
  print(lis)

# Insertion(l1)

# def Bubble(lis):
#   for i in range(1, len(lis)-1):
#     current = i-1
#     compare = i
#     while current >= 0 and lis[current] > lis[compare]:
#       lis[compare] = lis[current]
#       current+=1
#       compare+=1

def Bubble(lis):
  for i in range(0, len(lis)): # running a loop through the entire list
    for j in range(0, len(lis)-1-i): # running a loop through the list excluding the last element
      if lis[j] > lis[j+1]:
        temp = lis[j+1]
        lis[j+1] = lis[j]
        lis[j] = temp
  print(lis)

# Bubble(l1)

def mergeSort(lis):
  if len(lis) > 1:
    splitting = (len(lis))//2
    split1 = lis[:splitting] # : refers to where to be split from
    split2 = lis[splitting:] # e.g lis = [1, 2, 3], then :2 means splitting list to [1, 2]
    mergeSort(split1)
    mergeSort(split2)
    if len(split1) < 2 and len(split2) < 2:
      if split1[0] > split2[0]:
        sort1 = []
        sort1.append(split2[0])
        sort1.append(split1[0])
      else:
        sort1 = []
        sort1.append(split1[0])
        sort1.append(split2[0])
      print(sort1)

mergeSort(l1)