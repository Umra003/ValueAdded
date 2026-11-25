n=12344639808
freq=[0]*10
while(n!=0):
    last_digit=n%10
    freq[last_digit] +=1
    n =n//10
print(freq)