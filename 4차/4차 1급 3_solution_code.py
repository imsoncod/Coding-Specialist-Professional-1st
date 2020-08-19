def solution(one_day_price, multi_day, multi_day_price, n):
    if one_day_price * multi_day <= multi_day_price:
        return n * one_day_price
    else:
        return (n // multi_day) * multi_day_price + (n % multi_day) * one_day_price