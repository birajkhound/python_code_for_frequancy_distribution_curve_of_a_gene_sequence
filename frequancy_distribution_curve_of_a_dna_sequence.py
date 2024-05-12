# our DNA sequence file name
# Ecol_K12_MG1655_gene_sequence.txt
# Bacillus_subtilis_subsp.txt

  # importing matplot library 
import matplotlib.pyplot as plt
import numpy as np


  # declaring 4 array to store sum of all a,t,g,c molecules in each line 
Aa = []
At = []
Ag = []
Ac = []


  # function to calculate total repeatatation of a specific character in a string
def count_letters(input_string , target_character):
    count = 0
    for char in input_string:
        if char.isalpha():
            if char == target_character:
                count += 1
    return count  
   
  # to take the text file addres as input
address = str(input("enter the txt file address of the gene sequance :"))

  #calculation of numbers of a,t,g,c in each line
with open(address, 'r') as file:
    for line in file:
         # to Skip header lines
        if not line.startswith(">"): 
            Na = count_letters(line, 'a')
            Nt = count_letters(line, 't')
            Ng = count_letters(line, 'g')
            Nc = count_letters(line, 'c')
            Aa.append(Na)
            At.append(Nt)
            Ag.append(Ng)
            Ac.append(Nc)

  #finding unique values and frequency distribution
unique_valuesA, countsA = np.unique(Aa, return_counts=True)
unique_valuesT, countsT = np.unique(At, return_counts=True)
unique_valuesG, countsG = np.unique(Ag, return_counts=True)
unique_valuesC, countsC = np.unique(Ac, return_counts=True)

# print( unique_valuesA , countsA )

   #ploting frequency distribution graph of A,T,G,C-
plt.plot(unique_valuesA, countsA,  marker='o', color = 'green')
plt.plot(unique_valuesT,countsT, marker='o', color = 'red')
plt.plot(unique_valuesG,countsG, marker='o', color = 'blue')
plt.plot(unique_valuesC,countsC, marker='o', color = 'yellow')

  # Add labels and title
plt.xlabel('Class Intervals')
plt.ylabel('Frequency')
plt.title("Frequency Distribution Curve Of ATGC-(chargaff's second parity rule)")
# plt.text(20,7000,"red is T, green is A, Blue is G, Yellow is C")
  # Identify color meaning (place text at top right corner)
plt.text(35, 8000, f"{"T"}: {"red   "}", ha='center', va='center', fontsize=10, bbox=dict(boxstyle="round", facecolor='white', edgecolor='0.3'))
plt.text(35, 7200, f"{"A"}: {"green "}", ha='center', va='center', fontsize=10, bbox=dict(boxstyle="round", facecolor='white', edgecolor='0.3'))
plt.text(35, 6400, f"{"G"}: {"blue  "}", ha='center', va='center', fontsize=10, bbox=dict(boxstyle="round", facecolor='white', edgecolor='0.3'))
plt.text(35, 5600, f"{"C"}: {"yellow"}", ha='center', va='center', fontsize=10, bbox=dict(boxstyle="round", facecolor='white', edgecolor='0.3'))
  # display plot
plt.show()