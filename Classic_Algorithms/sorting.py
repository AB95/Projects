

def bubble_sort(values):
    vals = list(values)
    for i in xrange(len(vals)):
        while i != 0 and vals[i-1] > vals[i]:
            vals[i-1], vals[i] = vals[i], vals[i-1]
            i -= 1
    return vals


def merge_sort(values):

    def merge(list1, list2):
        return_vals = []
        list1, list2 = list(list1), list(list2)
        while list1 and list2:
            if list1[0] <= list2[0]:
                return_vals.append(list1.pop(0))
            else:
                return_vals.append(list2.pop(0))

        if list1:
            for x in list1:
                return_vals.append(x)
        else:
            for x in list2:
                return_vals.append(x)
        return return_vals

    vals = list(values)
    if len(vals) > 1:
        half = len(vals)/2
        left = vals[half:]
        right = vals[:half]
        left = merge_sort(left)
        right = merge_sort(right)
        vals = merge(left, right)
    return vals
