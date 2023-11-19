from classify_fc import *

model = train()
f = open('parameters.h', 'w')
i = 1
for name, parameters in model.named_parameters():
    numbers = parameters.data.tolist()
    if name.endswith('weight'):
        f.write('const float weight'+str(i))
    else:
        f.write('const float bias'+str(i))
        i += 1
    if type(numbers) == float:
        f.write(numbers)
        f.write(';\n')
    elif type(numbers[0]) == float:  # vector
        f.write('[]={'+', '.join([str(num) for num in numbers])+'};\n')
    else:  # matrix
        f.write('[]['+str(len(numbers[0]))+']={')
        for nums in numbers:
            f.write('{'+', '.join([str(num) for num in nums])+'},\n    ')
        f.write('};\n')
f.close()

#print(name, ':', parameters.data.tolist())
