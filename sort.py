def bubble_sort(a):
    for i in range(len (a) - 1):
        for j in range (len (a)- 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


#if __name__ == "__main__":
#    test_array = [9, 2, 5, 17, 22]
#    sorted_test_array = bubble_sort(test_array)
#    print(test_array)
#    print(sorted_test_array)
