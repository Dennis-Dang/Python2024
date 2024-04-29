working = False
while not working:
    print('Welcome to your simple adder!')
    print('-----------------------------')
    a: str = input("Enter a value for 'a': ")
    b: str = input("Enter a value for 'b': ")

    try:
        print(f'The result is: {int(a)+int(b)}')
        working = True
    except ValueError:
        print(f'Invalid inputs: a:{a} b:{b}')
        print('Restarting program...\n\n\n')