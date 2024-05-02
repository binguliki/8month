a = input("Enter valid A : ")
b = input("Enter valid B : ")

br = [int(i) for i in a]
qr = [int(i) for i in b]

def full_adder(bit_a , bit_b , input_carry):
    sum = bit_a ^ bit_b ^ input_carry
    carry = ((bit_a ^ bit_b) & input_carry) | (bit_a & bit_b)
    
    return (sum , carry)

def adder(ans , index , A , B , carry):
    if index == 0:
        sum , output_carry = full_adder(A[index] , B[index] , carry)
        ans.append(sum)
        return
    
    sum , output_carry = full_adder(A[index], B[index] , carry)
    adder(ans , index-1 , A , B , output_carry)
    ans.append(sum)
    return 

def complimenter(array):
    compli = [1 if i==0 else 0 for i in array]
    temp = [0] * len(compli)
    
    ans = []
    adder(ans , len(compli)-1 , compli , temp , 1)
    return ans

br_sub = complimenter(br)
sc = len(qr)
qn_1 = 0
qn = qr[-1]
ac = [0]*len(br)

while sc != 0:
    if qn == 1 and qn_1 == 0:
        ans = []
        adder(ans , len(br_sub)-1 , br_sub , ac , 0)
        ac = ans
    elif qn == 0 and qn_1 == 1:
        ans = []
        adder(ans , len(br)-1 , br , ac , 0)
        ac = ans
    
    ac.insert(0 , ac[0])
    qr.insert(0 , ac.pop(-1))
    qn_1 = qr.pop(-1)
    qn = qr[-1]
    sc -= 1

ac.extend(qr)
ans = ''.join(list(map(str, ac)))
print(ans)