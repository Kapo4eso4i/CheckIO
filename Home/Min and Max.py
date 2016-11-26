def minimax(*args, **kwargs):
    key = kwargs.get('key', lambda x: x)
    mini = kwargs.get('mini', None)
    args = args[0] if len(args) == 1 else args
    result = next(iter(args))
    for arg in iter(args):
        if mini:
            if key(result) > key(arg): result = arg
        else:
            if key(result) < key(arg): result = arg
    return result

def min(*args, **kwargs):
    kwargs['mini'] = True
    return minimax(*args, **kwargs)

def max(*args, **kwargs):
    return minimax(*args, **kwargs)
