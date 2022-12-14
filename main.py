# Part 1: Understand Recursion

# Chapter 1. What Is Recursion?
print('Example One\n')


def a():
    print('a() was called.')
    b()
    print('a() is returning.')


def b():
    print('b() was called.')
    c()
    print('b() is returning.')


def c():
    print('c() was called.')
    print('c() is returning.')


a()
print('---------------------------------------')

print("Example 2")

# TODO: Create Empty Stack
cardStack = []
# TODO: Push 5 of diamonds onto stack
cardStack.append('5 of diamonds')
print(', '.join(cardStack))
# output: ['5 of diamonds']
# TODO: Push 3 of clubs onto stack
cardStack.append('3 of clubs')
print(', '.join(cardStack))
# output: ['5 of diamonds', '3 of clubs']
# TODO: Push Ace of Hearts onto stack
cardStack.append('Ace of hearts')
print(', '.join(cardStack))
# output: ['5 of diamonds', '3 of clubs', 'Ace of hearts']
# TODO: Pop last element off of stack
cardStack.pop()
print(', '.join(cardStack))
# output: ['5 of diamonds', '3 of clubs']
print('---------------------------------------')
print("Example 3")


def a():
    spam = 'Ant'
    print(f'spam is {spam}')
    b()
    print(f'spam is {spam}')


def b():
    spam = 'Bobcat'
    print(f'spam is {spam}')
    c()
    print(f'spam is {spam}')


def c():
    spam = 'Coyote'
    print(f'spam is {spam}')


a()

