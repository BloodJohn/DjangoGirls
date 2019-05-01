# test comment

if 3 < 2:
    print('It works!')
else:
    print('Hello world')


# my function
def hi(name: str) -> str:
    print('Hi there! ' + name)
    print('How are you?')


girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for i in range(1, len(girls)):
    hi(girls[i])

