from mytree import BST
from mytree import Node

text_file = open("words.txt", "r")
lines = text_file.readlines()
#print(len(lines))

bst = BST()

for val in lines:
    bst.insert(val)

#print(bst)
print("Min:")
print(bst.getMin())
print("Max:")
print(bst.getMax())
