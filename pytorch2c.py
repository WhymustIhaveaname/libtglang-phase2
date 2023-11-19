from classify_fc import *

model = train()
for name, parameters in model.named_parameters():
    numbers = parameters.data.tolist()
    if type(numbers) == float:
        print(numbers)
    elif type(numbers[0]) == float:  # vector
        print('{'+', '.join([str(num) for num in numbers])+'};')
    else:  # matrix
        print('{', end='')
        for nums in numbers:
            print('{'+', '.join([str(num) for num in nums])+'},', end='')
        print('};', end='')
    print('\n')

    #print(name, ':', parameters.data.tolist())
