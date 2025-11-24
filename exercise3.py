# 1. Create tuple for one patient
patient = ("John Doe", 45, "120/80", 72)

# 2. Print age + heart rate
print("Age:", patient[1])
print("Heart Rate:", patient[3])

# 3. Why tuples?
print("\nTuples are suitable because patient vitals must remain unchanged,")
print("ensuring data integrity and preventing accidental modification.")

# 4. Convert to list, update heart rate, convert back
patient_list = list(patient)
patient_list[3] = 78
patient = tuple(patient_list)
print("\nUpdated Patient Tuple:", patient)

# 5. Tuple of 5 patients
patients = (
    ("John Doe", 45, "120/80", 72),
    ("Alice Kim", 30, "110/70", 68),
    ("Brian Oduor", 55, "130/85", 75),
    ("Mary Wambui", 40, "118/76", 70),
    ("Kelvin Otieno", 60, "140/90", 80)
)

# Extract names
names = [p[0] for p in patients]
print("\nAll Patient Names:", names)
