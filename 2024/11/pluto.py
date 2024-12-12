import sys




if __name__ == "__main__":
    data = open(sys.argv[1]).read().strip().split()
    blinks = int(sys.argv[2])
    for x in range(blinks):
        tmp_data = []
        for num in data:
            if not num:
                continue
            if len(num) %2==0:
                #breakpoint()
                size = int(len(num)/2)
                tmp_data.append(num[0:size])
                tmp_data.append(str(int(num[size:])))
            elif int(num) == 0:
                tmp_data.append("1")
            else:
                tmp_data.append(str(2024*int(num)))

        print(f"--len: {len(tmp_data)}")
        #print(" ".join(tmp_data))
        data = tmp_data

    print(f"Length of stones: {len(data)}")
    print("2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2")
    #print(" ".join(data))


