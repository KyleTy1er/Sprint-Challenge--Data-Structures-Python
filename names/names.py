import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
# change
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#You may not use the built in Python list, set, or dictionary in your solution for this problem.
# However, you can and should use the provided duplicates list to return your solution.
class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return str(self.value)

    def insert(self, value):

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if self.value is None:
            return False
        else:
            if self.value == target:
                return True
            if target < self.value:
              if self.left:
                if self.left.contains(target):
                    return True
                else: return False
            if target >= self.value:
              if self.right:
                if self.right.contains(target):
                    return True
                else: return False

    def get_max(self):
      if self is None:
          return "Tree is empty."
      else:
          if self.right is None:
              return self.value
          else:
              return self.right.get_max()

    def for_each(self, fn):
      fn(self.value)
      if self.left:
        self.left.for_each(fn)
      if self.right:
        self.right.for_each(fn)

duplicates = []
node = BSTNode(names_1[0])
for each_name in names_1:
    node.insert(each_name)

for each_name2 in names_2:
    if node.contains(each_name2):
        duplicates.append(each_name2)

print(duplicates)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------------attempt graveyard---------------------#

# for each_name in names_1:
#     each_name = BSTNode(each_name)
#     each_name.insert(each_name)
#     duplicates.append(each_name)
#
# for each_name2 in names_2:
#     each_name2 = BSTNode(each_name2)
#     each_name2.insert(each_name2)
#     duplicates.append(each_name2)
#
#
# print (len(duplicates))
#
# return_duplicates(data)


# def return_duplicates(self, data):
#     self.data = data
#     if self.value is None:
#         return None
#     else:
#         if self.value in data:
#             return data.append(self.value)
#         if self.left:
#             if self.left.return_duplicates():
#                 return data.append(self.value)
#             else: return None
#         if self.right:
#             if self.right.return_duplicates():
#                 return data.append(self.value)
#             else: return None
#         return data

# def insert(self, value):
#     if len(value) < len(self.value):
#         if self.left:
#             self.left.insert(value)
#         else:
#             self.left = BSTNode(value)
#     else:
#         if self.right:
#             self.right.insert(value)
#         else:
#             self.right = BSTNode(value)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


