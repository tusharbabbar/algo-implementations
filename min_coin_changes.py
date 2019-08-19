def min_coin_change(denominations, total):
    if total == 0:
        return 0, []
    res = []
    for denomination in denominations:
        if denomination > total:
            continue
        elif denomination == total:
            res.append((1, [denomination]))
        else:
            coins, selections = min_coin_change(denominations, total - denomination)
            res.append((1+ coins, [denomination] + selections))
    return min(res, key=lambda x: x[0])

if __name__ == '__main__':
    denominations = [1, 5, 6, 8]
    total = 30
    print(min_coin_change(denominations, total))

