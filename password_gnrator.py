import random,string
length = int(input("enter password length:"))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print('generated password:',password)