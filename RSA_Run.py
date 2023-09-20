def ExpMod(x,n,m):
    if n == 0 : return 1
    if n == 1 : return x%m
    if n%2 == 0 : return (ExpMod(x,n//2,m)**2)%m
    else : return (ExpMod(x,n//2,m)**2*ExpMod(x,1,m))%m

def ModularInverse_PhiEuler(a,m):
    return ExpMod(a,PhiEuler(m)-1,m)

def ModularInverse_Euclid(a,m):
    r_1, r_2 = a, m
    r = r_2%r_1
    q = r_2//r_1
    x_1, x_2, y_1, y_2 = 1,0,0,1
    x = x_2 - q*x_1
    y = y_2 - q*y_1
    while(r != 1):
        r_2 = r_1
        r_1 = r
        r = r_2%r_1
        q = r_2//r_1
        x_2 = x_1
        x_1 = x
        x = x_2 - q*x_1
        y_2 = y_1
        y_1 = y
        y = y_2 - q*y_1
    if x<0 : return x + m
    return x

def PhiEuler(m):
    result = m
    index = 2
    while index**2 <= m :
        if m%index == 0 : 
            while m%index == 0:
                m = m//index
            result = result - result//index
        index += 1
    if m != 1 : result -= result//m
    return result
print("***** INPUT *****")
My_p,My_q = map(int,input("Enter p and q : ").split())
My_n = My_p*My_q
My_m = ( My_p - 1 )*( My_q - 1)

while True:
    My_e = int(input("Enter prime 'e' so that (e,{}) = 1 : ".format(My_m)))
    if My_m % My_e : break

My_privateKey = ModularInverse_Euclid(My_e,My_m)
print("My private key : ", My_privateKey)
print("My public key : ({},{})".format(My_n,My_e))

print("***** YOUR PARTNER *****")

Partner_n,Partner_e = map(int,input("Enter your partner's public key : ").split())

while True:
    print("1: Encode message")
    print("2: Decode message")
    yourOption = int(input("Your option : "))
    if yourOption == 1:
        message = int(input("Enter your message : "))
        encodeMessage = ExpMod(message,Partner_e,Partner_n)
        print("Your message has been encode :",encodeMessage)
    elif yourOption == 2:
        message = int(input("Enter your message : "))
        decodeMessage = ExpMod(message,My_privateKey,My_n)
        print("decode :",decodeMessage)
