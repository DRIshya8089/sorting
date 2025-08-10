def bubble_sort_by_length(lst):
    n = len(lst)
    for _ in range(n - 1):
        swapped = False
        for j in range(n - 1):
            if len(lst[j]) > len(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break  # No swaps means the list is already sorted

if __name__ == "__main__":
    foods = ["pizza", "ice cream", "sushi", "burger", "taco", "avocado toast"]
    print("Before:", foods)
    bubble_sort_by_length(foods)
    print("After:", foods)
