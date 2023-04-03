with open("E:\studia\Zaawansowane modelowanie molekularne\mgr\FTFSI15.log", "r") as file:
    test = []
    for line in file:
        new_line = line.strip(" \n")
        test.append(new_line)
    num_pos = test.index('Final structure in terms of initial Z-matrix:')
    values = []
    for i in range(30):
        values.append(test[num_pos+i+14])
    for a in values:
        print(a)
    # text = file.readlines()
    # print(text)