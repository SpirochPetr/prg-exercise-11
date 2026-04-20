import random
import matplotlib.pyplot as plt

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

def bubble_sort(values):
    values = values.copy()
    n = len(values)
    plt.ion()
    plt.show()

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1

            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"

            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        if not swapped:
            break

    plt.ioff()
    plt.show()

    return values

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
    ##t3#
    test = random_numbers(10)
    print("Původní:", test)
    sorted_list = bubble_sort(test)
    print("Seřazený:", sorted_list)

if __name__ == "__main__":
    main()



