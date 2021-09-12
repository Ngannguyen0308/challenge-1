input_str = input('please enter a list:')
list = input_str.split()
list.sort()
print(list)

print('================')
list_input = input("Please enter a list:")
Sequence = list_input.split()
def quick_sort(Sequence):
    length = len(Sequence)
    if length <= 1:
        return Sequence
    else:
        pivot = Sequence.pop()
    item_greater = []
    item_lower = []
    for item in Sequence:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)
    
    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)

print(quick_sort(Sequence))
print('================')
