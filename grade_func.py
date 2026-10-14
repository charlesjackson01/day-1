def letter(score):
    if score >= 90:
        return "A"

        
    elif score >= 70:
        return "Pass"
    
    else:
        return "Fail"


print(letter(85))
print(letter(95))