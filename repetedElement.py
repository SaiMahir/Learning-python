n = int (input("enter the no of elements:"))
elements=[]
for i in range (n):
    element = int(input("enter element:"))
    elements.append(element)
print(elements)
repeated_elements = []
element_count = 0
for i in range (elements):

    if i not in repeated_elements:
        element_count = elements.count(elements[i])
        if element_count > 1:
            repeated_elements.append(elements[i])