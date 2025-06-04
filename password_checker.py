import re

def check_password_strength(password):
    score = 0
    remark = []

    if len(password) >= 10:
        score +=1
    else:
        remark.append("Password should be at least 8 characters.")
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score+=1
    else:
        remark.append("Use uppercase and lowercase letters.")
        
    if len(re.findall(r"\d",password))>=2:  
        score += 1 
    else:
        remark.append("Include at least 2 digit")

    if re.search(r"[^A-Za-z0-9]",password):
        score += 1
    else:
        remark.append("include at least one special character (@!~&$) etc. ")
    
    if score == 4:
        strength = "Strong"
    
    elif score == 3:
        strength = "Moderate"

    else:
        strength = "Weak"

    return strength, remark

if __name__ == "__main__": 
    password = input("Enter your password to test: ")
    strenght, remark = check_password_strength(password)

    print(f"\nStrength: {strenght}")

    for i in remark:
        print(f"Feedback: {i}")

