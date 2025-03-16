def main():
    # Create an empty list
    my_list = []
    
    # i. Add elements to the list using the append() method
    print("Enter elements to add to the list. Type 'done' to stop.")
    while True:
        item = input("Enter an element to append to the list: ")
        if item.lower() == 'done':
            break
        my_list.append(item)
    
    # ii. Insert an element at a specific position using the insert() method
    print("\nCurrent List:", my_list)
    position = int(input("Enter the position (index) to insert an element: "))
    element = input("Enter the element to insert: ")
    my_list.insert(position, element)
    print("List after insertion:", my_list)
    
    # iii. Remove a specific element from the list using the remove() method
    print("\nCurrent List:", my_list)
    element_to_remove = input("Enter the element you want to remove: ")
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
        print("List after removal:", my_list)
    else:
        print("Element not found in the list.")
    
    # iv. Sort the list in ascending order using the sort() method
    print("\nCurrent List:", my_list)
    my_list.sort()
    print("List after sorting in ascending order:", my_list)
    
    # v. Display the index of any element in the list using the index() method
    print("\nCurrent List:", my_list)
    element_to_find = input("Enter an element to find its index in the list: ")
    if element_to_find in my_list:
        index_of_element = my_list.index(element_to_find)
        print(f"Index of '{element_to_find}' in the list is: {index_of_element}")
    else:
        print("Element not found in the list.")

if __name__ == "__main__":
    main()
