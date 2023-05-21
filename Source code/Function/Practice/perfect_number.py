def is_perfect(n):
    def sum_div(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum
    if n == sum_div(n):
        return True
    else: 
        return False
