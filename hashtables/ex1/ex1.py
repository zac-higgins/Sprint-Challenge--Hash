def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}
    duplicate_check = False
    duplicate_dict = {}
    # iterate through weights and store them in the dict
    for i in range(0, length):
        current_weight = weights[i]
        weight_dict[current_weight] = i
        sum_check = limit - current_weight
        if sum_check in weight_dict:
            if current_weight > sum_check:
                return (i, weight_dict[sum_check])
            elif current_weight < sum_check:
                return (i, weight_dict[sum_check])
            elif sum_check == current_weight:
                if duplicate_check is False:
                    duplicate_check = True
                    duplicate_dict[current_weight] = i
                elif duplicate_check is True:
                    return (i, duplicate_dict[current_weight])
    return None

# print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
# print(get_indices_of_item_weights([4, 4], 2, 8))