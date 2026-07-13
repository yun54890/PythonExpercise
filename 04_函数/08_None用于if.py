

def check_age(age):
    if age < 18:
        return None
    return "SUCCESS"

if check_age(19):
    print("成年人")
else:
    print("未成年人")