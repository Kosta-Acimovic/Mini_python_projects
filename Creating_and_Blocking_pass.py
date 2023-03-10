Tpass="admin123"
your_try=" "
num_of_try=0
max_num_of_try=8
max_try="NotReached"

while your_try!=Tpass and max_try!="Reached":
    if num_of_try<max_num_of_try:
        your_try=input("Enter your password:\t")
        num_of_try+=1
    else:
        max_try="Reached"

if max_try=="Reached":
    print("Access denied\n"
          "This account is blocked from now on, for more information call your support")
else:
    print("Access granted\n"
          "Welcome and enjoy your time")