# Devon Taylor
# DS
# U3L5
# 11/13/24

from random import randint

def bubbleSort(sortList):
  for i in range(len(sortList) - 1):
    for x in range(len(sortList) - i - 1):
      if sortList[x] > sortList[x + 1]:
        sortList[x], sortList[x + 1] = sortList[x + 1], sortList[x]
  return sortList

def main():
  sortList = []
  for i in range(randint(5, 20)):
    sortList.append(randint(0, 50))

  print(f"Starting List: {sortList}")
  sortedList = bubbleSort(sortList)
  print(f"Sorted List: {sortedList}")

if __name__ == "__main__":
  main()