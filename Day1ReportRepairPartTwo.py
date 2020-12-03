with open('challenge2_input.txt', 'r') as file:
    contents=file.read().split('\n')[:-1]

print(contents)

for i in contents:
    for j in contents:
        for k in contents:
            i=int(i); j=int(j); k=int(k);
            if i+j+k==2020:
                print(f'Found the correct match: {i}+{j}+{k} whose multiplication is {i*j*k}')
                quit()
            else:
                print("nah")
