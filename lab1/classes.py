"""
- Ask user what classes they are taking, 
- Save class names in a list,
- Print each class, one per line
"""

classes = input('What classes are you taking this semester? ')
class_list = classes.split()

for classes in class_list:
    print(classes)
