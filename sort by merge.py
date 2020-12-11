def sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        sort(a, p, q)
        sort(a, q + 1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):
    left_copy = a[p:q + 1]
    right_copy = a[q + 1:r + 1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = p
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            a[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            a[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
    while left_copy_index < len(left_copy):
        a[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index +=1
    while right_copy_index < len(right_copy):
        a[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1


a = [5, 2, 4, 6, 1, 3, 2, 6]
sort(a, 1, len(a))
print(a)

