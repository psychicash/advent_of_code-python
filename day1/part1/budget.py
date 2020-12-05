num_list = []

with open('adventofcode1.txt', 'r') as fh:
    for line in fh:
        num_list.append(int(line))

variable1 = 0
variable2 = 0
product_total = 0

#loop
for i in range(len(num_list)):
    var1 = num_list[i]
    for j in range(len(num_list)):
        if j == i:
            continue
        #inner_loop
        var2 = num_list[j]
        if (var1+var2 == 2020):

            print(str(var1) + " times " + str(var2) + " equals " + str(var1*var2))

