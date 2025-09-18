#Start defining a new function

def calculate_gc_content(dna_sequence): 
    """
    Calculates the GC content (percentage) of a given DNA sequence string.
    This function is useful for batch processing multiple DNA sequences without code duplication.
    'calculate_gc_content' is the custom name of this function.
    'dna_sequence' is the parameter name, representing the input DNA string when the function is called.
    """
    # 1. Convert the sequence to uppercase to ensure case consistency.
    # This prevents errors because 'g' and 'G' are considered different characters in programming.
    sequence = dna_sequence.upper() 

    # 2. Count the number of 'G' and 'C' nucleotides in the sequence.
    g_count = sequence.count('G') #Count the number of 'G's in the sequence.
    c_count = sequence.count('C') #Same principle as above
    total_length = len(sequence) #calculate the total length of the sequence.# Note: This includes any non-nucleotide characters (e.g., spaces, line breaks) if present.

    # 3. Avoid division by zero error if the sequence is empty.
    if total_length == 0:
        return 0.0

    # 4. Calculate and return the GC content as a percentage.
    gc_content = (g_count + c_count) / total_length * 100

    # 5. return result
    return gc_content

abc = "ATCG"
result = calculate_gc_content(abc) # Pass the variable 'abc' into the previously defined function
print(result) # 50.0
print(f"The GC content of {abc} is {result:.2f}%") 
#:.2fspecifies floating-point precision in formatting—the number indicates decimal places (e.g., ':.3f' for three decimals)
#Note: The actual value of `result` remains 50.0; it is only displayed as 50.00

print("=" * 60)#Alternative way of printing the value
print("The GC content of ATCG is {:.2f}%".format(result)) 
print("The GC content of ATCG is {}%".format(result)) 

print("=" * 60)#Don’t forget the 'f' ,this is the difference between having it and not
print(f"The GC content of {abc} is {result}%") 
print("The GC content of {abc} is {result}%") 

print("=" * 60)
#If you need a new variable with rounded decimal values, use the round() function
result = 50.123124
print("The GC content is {:.2f}%".format(result)) 
print(result) #This will output 50.123124 since ':.2f' only affects how the variable is displayed when printed
round1 = round(result, 4) #Define a new variable to store the number with rounded decimals
#Syntax of round(): round(variable, number_of_decimals)
print(round1)

