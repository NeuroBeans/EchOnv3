def open_file(path):
    f = open(path, 'rb')
    for i in range(10):
        f.readline()
    data = []
    data2 = []
    count = 0
    for i in f:
        if count < 1000:
            line = i.decode().strip().split()
            data.append(float(line[2]))
            data2.append(float(line[3]))
            count += 1
    data.extend(data2)
    return data





