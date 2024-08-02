#3. Write a Python function to count the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)

# Example usage
my_list = [1, 2, 3, 4, 1, 2, 1, 5, 1]
element_to_count = 1
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")
