def main():
    # i. Create and check the shape of an array (represented by a list)
    print("Creating a 1D array of 12 elements:")
    arr = [i for i in range(12)]  # Create a list with elements from 0 to 11
    print("Array:", arr)
    print("Length of the array:", len(arr))  # Checking the length of the array (shape)

    # ii. Convert a 1D array of 12 elements into a 3x4 matrix (list of lists)
    print("\nConverting the 1D array into a 3x4 matrix:")
    matrix = [arr[i:i+4] for i in range(0, len(arr), 4)]  # Grouping elements into rows of 4
    print("3x4 Matrix:")
    for row in matrix:
        print(row)

    # iii. Convert a 2D array into a 1D array
    print("\nConverting a 2D array into a 1D array:")
    arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 2D array (list of lists)
    flattened = [item for sublist in arr_2d for item in sublist]  # Flattening the 2D array into 1D
    print("Original 2D array:", arr_2d)
    print("Flattened 1D array:", flattened)

    # iv. Extract a subarray using slicing
    print("\nExtracting a subarray using slicing:")
    subarray = [row[1:] for row in arr_2d[1:]]  # Extracting a subarray starting from index (1, 1)
    print("Subarray (elements from index 1,1 onwards):", subarray)

    # v. Extract every alternate element from a given array
    print("\nExtracting every alternate element from the array:")
    alternate_elements = arr[::2]  # Slicing to get every alternate element
    print("Every alternate element:", alternate_elements)

if __name__ == "__main__":
    main()
