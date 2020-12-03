with open('chal1_input.txt','r') as file:
    contents=file.read().split('\n')[:-1]

for i in contents:
    for j in contents:
        i=int(i)
        j=int(j)
        if i+j==2020:
            print(f"Correct match found: {i} and {j} whose multiplication is {i*j}")
            quit()
        else:
            print('nah')
