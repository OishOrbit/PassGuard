import random 
import string
common_passwords = ["12345678","password","qwerty","asdfghjkl","letmein","admin123","zxcvbnm","qazwsxedc","1q2w3e4r"]
def common_password(password):
    if password.lower() in common_passwords:
        return True
    else:
        return False
    
    
def password_score ( password ):
    score = 0
    lower_count = upper_count = digit_count = sp_char_count  = 0
    passlen = len(password)
    if passlen >= 16:
        score += 20
    elif  passlen >= 12 and passlen <= 15:
        score+=10
    else:
        score +=5
        
    for x in password:
        if x.islower():
            lower_count += 1
     
    for x in password:
        if x.isupper():
            upper_count += 1     
            
    for x in password:
        if x.isdigit():
            digit_count += 1 
            
    for x in password:
        if x in string.punctuation:
            sp_char_count += 1
    
    feedback = []
    if passlen <8:
        feedback.append("Length is less than 8 characters, Increase Length of the password !")
    if lower_count == 0:
        feedback.append("No lowercase letters in the password, Add lowercase letters to make it stronger !")
    if upper_count == 0:
        feedback.append("No Uppercase letters in the password, Add uppercase letters to make it stronger !")
    if digit_count == 0:
        feedback.append("No digits in the password, Add digits to make it stronger !")
    if sp_char_count == 0:
        feedback.append("No special character in the password, Add special characters to make it stronger !")
    if feedback:
        print(feedback)
    
    lower_score = lower_count * 3 
    
    upper_score = upper_count * 3
    
    digit_score = digit_count * 3
    
    sp_score   = sp_char_count * 3   
    
    score = score + min(20,lower_score) + min(20,upper_score) + min(20,digit_score) + min(20,sp_score) 
    
    total_score = score / 10   
    
    return total_score

def generate_secure_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation

    new_password = ""
    for i in range(length):
        new_password += random.choice(chars)

    return new_password





def main():
    print("Welcome to PassGuard.")   
    password = input("Enter your password :")
    if common_password(password):
        print(f"Your entered password {password} is a very common password. change it asap!") 
    else:
        final_score = password_score(password)
        print(f"Your password bears this score: {final_score}")
        if final_score>=0 and final_score<=2:
            print("VERY WEAK PASSWORD !!!!")
        elif final_score>=3 and final_score<=4:
            print("WEAK PASSWORD !!!!")
        elif final_score>=5 and final_score<=7:
            print("MEDIUM PASSWORD !!!!")    
        elif final_score>=7 and final_score<=9:
            print("STRONG PASSWORD !!!!")
        elif final_score==10:
            print("VERY STRONG PASSWORD !!!!")
        else:
            print("INVALID !")
        
    new_password = generate_secure_password()
    print(f"You can use this password {new_password}")


if __name__ == "__main__":
    main()