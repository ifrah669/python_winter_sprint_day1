def check_age(age):
    if age >= 0 and age <= 120:
        return True
    else:
        return False
    
def check_heart_rate(hr):
    if hr > 180:
        return "warning"
    elif hr > 0:
        return "ok"
    else:
        return "invalid"

def get_heart_rates(n, rates):
    if n == 0:
        return rates

    hr = int(input("Enter heart rate: "))
    rates.append(hr)

    return get_heart_rates(n - 1, rates)

def clinical_audit():
    flag = False
    warning = False

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))

    if not check_age(age):
        flag = True

    count = int(input("Enter number of heart rate readings: "))
    heart_rates = get_heart_rates(count, [])

    for hr in heart_rates:
        result = check_heart_rate(hr)

        if result == "invalid":
            flag = True
        elif result == "warning":
            warning = True

    if flag:
        status = "FAIL"
    elif warning:
        status = "REVIEW"
    else:
        status = "PASS"

    print("\n--- Audit Result ---")
    print("Patient Name:", name)
    print("Audit Status:", status)

clinical_audit()