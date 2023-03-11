def percentage_to_letter(score=0):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"

def is_passing(letter=None):
    if str(letter) == "A" or str(letter) == "B" or str(letter) == "C":
        return True
    else:
        return False

score = float(input("What is your grade? "))
letter = percentage_to_letter(score)
print(letter)
print(is_passing(letter))