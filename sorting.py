import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

#selection####################################################

def selection_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers

#bubble############################################

def bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

#main########################################

def main():
    ##t1#
    test = [5, 1, 4, 2, 8]
    print("Původní:", test)
    print("Seřazené:", selection_sort(test))
    random_list = random_numbers(20)
    print("Náhodné:", random_list)
    print("Seřazené:", selection_sort(random_list))
    ##t2#
    random_list = random_numbers(20)
    print("\nNáhodný seznam:", random_list)
    print("Seřazený seznam:", bubble_sort(random_list))


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()