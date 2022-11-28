def increase_sum(start):
    def func_dec(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start
        return wrapper
    return func_dec


@increase_sum(5)
def lst_sum(s):
    return sum(list(map(int, s.split())))


s = input()
print(lst_sum(s))