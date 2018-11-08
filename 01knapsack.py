""" Script to solve 0/1 knapsack.
    Outputs max value along with selected items
"""
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
    
    def __repr__(self):
        return "Item: (%s, %s)" %(self.weight, self.value)

def max_value_given_weight(items, weight):
    if items:
        item = items[-1]
        if item.weight > weight:
            return max_value_given_weight(items[:-1], weight)
        else:
            consider_item = max_value_given_weight(items[:-1], weight - item.weight)
            consider_item = (consider_item[0] + item.value, consider_item[1])

            dont_consider_item = max_value_given_weight(items[:-1], weight)
            if consider_item[0] > dont_consider_item[0]:
                selected_items = consider_item[1] + [item]
            else:
                selected_items = dont_consider_item[1]
            return max(consider_item[0] , dont_consider_item[0]), selected_items
    else:
        return 0, []


if __name__ == '__main__':
    given_input = [(23, 92), (31, 57), (29, 49), (44, 68), (53, 60), (38, 43), (63, 67), (85, 84), (89, 87), (82, 72)]
    given_input = [(12 ,24),   (7 ,13 ),  (11 ,23),   (8 ,15),   (9 ,16)]
    items = [Item(i[0], i[1]) for i in given_input]
    print(max_value_given_weight(items, 26))