# loops_for.py - for循环

# 1. iterating through a list
print("\n=== iterating through a list ===")
drugs = ["Aspirin", "Insulin", "Antibiotics", "Vitamin C"]
print("Medication list:")
for drug in drugs:#Iterate through each element in 'drugs', using 'drug' to refer to the current element
    print("- " + drug) #Pay attention to indentation - incorrect indentation will cause an error

# 2.You can also iterate through each character in a string
print("\n=== Iterate through characters ===")
dna_sequence = "ATCG"
for base in dna_sequence:
    print(f"Found nucleotide: {base}")

# 3. Basic range loop
print("\n=== range loop ===")
print("Prints 0-4:")
for i in range(5):  # 0,1,2,3,4
    print("Current number:", i)

print("\nPrints 1-5:")
for i in range(1, 6):  # 1,2,3,4,5
    print("Current number:", i)

print("\nPrint odd numbers from 1 to 10:")
for i in range(1, 11, 2):  # 1,3,5,7,9；Start at 1, end before 11, step by 2
    print("odd number:", i)


# 4. Calculate the sum
print("\n=== Calculate the sum from 1 to 100 ===")
total = 0
for number in range(1, 101):
    total += number  # Equivalent to“ total = total + number ”

print("The sum of numbers from 1 to 100 is:", total)

# 5. Nested loops - multiplication table
print("\n=== Simple multiplication table ===")
for i in range(1, 4):  # 1,2,3
    for j in range(1, 4):  # 1,2,3
        print(f"{i} × {j} = {i * j}", end="  ") #Print each row of the multiplication table，and add two spaces after each operation
    print()  #  Line break after each row
    
    
    
    


