import itertools


def stringify(value, replacer=' ', spaces_count=1):
    if not isinstance(value, dict):
        return str(value)
    else:
        deep_counter = itertools.count(start=2, step=1)

        def walk(value, replacer, spaces_count, deep=1, string='{\n'):
            for key in value:
                if isinstance(value[key], dict):
                    string += replacer*(spaces_count)*deep + str(key) + ': {' + '\n'
                    deep = next(deep_counter)
                    return walk(value[key], replacer, spaces_count, deep, string)
                else:
                    string += replacer*spaces_count*deep + str(key) + ': ' + str(value[key]) + '\n'
            if deep > 1:
                for one_deep in reversed(range(1, deep)):
                    string += replacer*spaces_count*one_deep + '}\n'
                string += '}'
            else:
                string += '}'
            return string

    return walk(value, replacer, spaces_count)
    
