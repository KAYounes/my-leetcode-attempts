from collections import defaultdict
import json
from turtle import rt


def print_dict(_dict, identifier='dict'):
    json_data = json.dumps(_dict, indent=4)

    print(identifier, sep="", end=" =\n")
    print(json_data)

def printArrayWithPointers(array, pointers=None):

    # from groups, each group reps a printed line
    groups = defaultdict(list) 
    for j, (index, values) in enumerate(pointers):
        if isinstance(values, list):
            unique_values = _remove_duplicates(values)
            for i, value in enumerate(unique_values):
                groups[i].append((index, value))
        else:
            groups[0].append((index, values))
    
    # calculate slots
    slots = []
    for i, el in enumerate(array):
        size = len(str(el)) + 2;
        slots.append(size)
    
    # create empty lines
    lines = [[" " * x for x in slots] for _ in groups]
    lines.append([" " * x for x in slots])

    # insert symbols in line slots
    for group_n, group in enumerate(groups.values()):
        for slot, symb in group:
            if(group_n == 0):
                lines[0][slot] = " ^"  + " " * (slots[slot] - 2)

            lines[group_n + 1][slot  ]= " " + symb  + " " * (slots[slot] - 2)
    
    # print array
    print(array)

    # print lines
    for line in lines:
        for slot in line:
            print(slot, end="")
        print()

__all__ = ["printArrayWithPointers", "print_dict"]

def _remove_duplicates(data):
  """
  Removes duplicates from an array of numbers while preserving order.

  Args:
      data (list): An array of numbers.

  Returns:
      list: A new list with duplicates removed.
  """

  # Create a set to store unique elements
  seen = set()
  # Create a new list to store unique elements in order
  unique_data = []

  for num in data:
    if num not in seen:
      seen.add(num)
      unique_data.append(num)

  return unique_data

if(__name__ == "__main__"):
    printArrayWithPointers(list(range(0,20)), [
        (0, ['a', 'b', 'c', 'a']),
        (1, ['b', 'c']),
        (5, ['a']),
        (6, 'a'),
        (12, ['g', 'd']),
        (19, 'f')]
    )

    # print(list(range(0, 20)))
    # print(" " * 1 + "|", sep="", end="")
    # print(" " * 2 + "|", sep="", end="")
    # print(" " * (2 * (4 - 1) + 2) + "|", sep="", end="")
    # print(" " * (2 * (7 - 4) + (6 - 3 - 1)) + "|", sep="", end="")
