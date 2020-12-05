num_list = []

with open('adventofcode2.txt', 'r') as fh:
    for line in fh:
        num_list.append(int(line))


product_total = 0

#loop
for i in range(len(num_list)):
    var1 = num_list[i]
    for j in range(len(num_list)):
        if j == i:
            continue
        var2 = num_list[j]
        for k in range(len(num_list)):
            if (k == i) or (k == j):
                continue
            var3 = num_list[k]
        
        
            if (var1+var2+var3 == 2020):
                product_total = var1 * var2 * var3

                print(str(var1) + " times " + str(var2) + " time " + str(var3) + " equals " + str(product_total))

