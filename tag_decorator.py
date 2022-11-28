def tag_decorator(tag):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return(f'<{tag}>{res}</{tag}>')
        return wrapper
    return func_decorator


@tag_decorator('div')
def low_word(s):
    return s.lower()


s = input()
print(low_word(s))


