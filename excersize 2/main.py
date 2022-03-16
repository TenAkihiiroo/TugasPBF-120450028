with open('bigNumber1.txt','r') as A:
    read_file1 = A.read()

with open('bigNumber2.txt','r') as B :
    read_file2 = B.read()

def conv_str1(num1):
    num1 = int(read_file1)
    return num1

def conv_str2(num2):
    num2 = int(read_file2)
    return num2

def big_Addition():
    return conv_str1(A) + conv_str2(B)

print("nilai A = ", conv_str1(A))
print("nilai B = ", conv_str2(B))
print("Hasil penjumlahan diatas adalah ",big_Addition())