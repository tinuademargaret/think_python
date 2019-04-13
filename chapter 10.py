# ex 10.1


def nested_sum(nested_list):
    total = 0
    for item in nested_list:
        total += sum(item)
    return total


ages = [[1, 2], [3, 4]]
sum_of_ages = nested_sum(ages)
print(sum_of_ages)

'''loool I wrote this program once!, and I just woke up from sleep'''

# ex 10.2


def capitalize_all(nested_list):
    capitalized_nested = []
    capitalized = []
    for nested in nested_list:
        for item in nested:
            capitalized.append(item.capitalize())
        capitalized_nested.append(capitalized)
    return capitalized_nested


names = [['tinu', 'sola'], ['fayo', 'moyo']]
capitalized_names = capitalize_all(names)
print(capitalized_names)


# ex 10.3


def cumulator(list_of_numbers):
    cumulative_sum = []
    total = 0
    for number in list_of_numbers:
        total += number
        cumulative_sum.append(total)
    return cumulative_sum


size = [1, 2, 3, 4, 5, 6]
cumulative_sum_of_size = cumulator(size)
print(cumulative_sum_of_size)


# ex10.4


def middle(liist):
    liist.pop(0)
    liist.pop(-1)
    return liist


numbers = [1, 2, 3, 4, 5]
print(middle(numbers))


# ex10.5
'''same as above just return None instead of liist'''

