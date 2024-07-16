name = input("your name: ")

while True:
        password = input("your password: ")
        if  len(password) < 8:
                print("atleast 8 characters needed")
        elif not any((char.islower() for char in password) and (c>
                print("upper and lower case needed")
        elif not any(char.isdigit() for char in password):
                print("atleast one number is needed")
        elif not any(char in "~!@#$%^&*()_+=-`{}|\][:;'?><,./" fo>
                print("atleast one special character needed")

        else:
                print("successful")
                break

