arr =[100, 101, 100, 102, 101, 100]
freq = [0] * 3
for i in arr:
    freq[i - 100] += 1
for i in range(len(freq)):
    print(f"Frequency of {i + 100} is: {freq[i]}")
