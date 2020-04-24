with open("binary", "bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))  # for bytes we are actually writing a list

with open("binary", "br") as bin_file2:
    for b in bin_file2:
        print(b)
