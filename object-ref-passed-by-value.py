def reassign(lis):
    lis = ['a', 'b']

def mutate(lis):
    lis.append('b')


l = ['a']
reassign(l)
print(l)
mutate(l)
print(l)
