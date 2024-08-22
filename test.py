# 3.3
biological_gender = input("Enter your biological_gender(female/male):")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l):"))
if biological_gender == "female":
    if hemoglobin_value < 117:
        print("Your hemoglobin is LOW!")
    elif hemoglobin_value > 155:
        print("Your hemoglobin is HIGH!")
    else:
        print("Yuor hemoglobin value is normal!")
elif biological_gender == "male":
    if hemoglobin_value < 134:
        print("Your hemoglobin is LOW!")
    elif hemoglobin_value > 167:
        print("Your hemoglobin is HIGH!")
    else:
        print("Yuor hemoglobin value is normal!")