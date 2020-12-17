def get(namespace, arg):
    if arg in space[namespace]['vars']:
        print(namespace)
    elif space[namespace]['parent'] == None:
        print("None")
        return
    else:
        get(space[namespace]['parent'], arg)

n = int(input())
space = {'global': {'parent':None, 'vars': []}}

for i in range(n):
    command, namespace, arg = input().split()
    if command == "add":
        space[namespace]['vars'].append(arg)
    elif command == "create":
        space[namespace] = {'parent':arg, 'vars': []}
    elif command == "get":
        get(namespace, arg)


"""
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b



Space = {'global': {'parent': None, 'vars': {'b'}},
                    'foo1': {'parent': 'global', 'vars': {'a'}},
                             'bar1': {'parent': 'foo1', 'vars': {'a'}},
                                      'new1': {'parent': 'bar1', 'vars': {'a'}},
                    'foo2': {'parent': 'global', 'vars': {'b', 'a'}},
                             'bar2': {'parent': 'foo2', 'vars': {'b'}},
                                      'new2': {'parent': 'bar2', 'vars': {'b'}}}
"""