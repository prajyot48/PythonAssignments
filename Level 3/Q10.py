def count_unserved_customers(n, sequence):
    occupied = set()
    seen = set()
    walked_away = 0

    for customer in sequence:
        if customer not in seen:
            seen.add(customer)
            if len(occupied) < n:
                occupied.add(customer)
            else:
                walked_away += 1
        else:
            if customer in occupied:
                occupied.remove(customer)

    return walked_away

N = 3
S = "GACCBDDBAGEE"
print("Walked away customers:", count_unserved_customers(N, S))  
