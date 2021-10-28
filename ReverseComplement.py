
# coding: utf-8
##############A.Reverse Complement##################
#Q.1. Writing Function (A)
#Q.3. Self-critique:1. Readability: This function is simple to understand.
                   #2. Robustness: Input besides string would cause issues.
                   #3. Correctness:DNA seq input with space or other symbols (eg. tabs,*,%...) would not be recognized as DNA seq and no output generated.
                                   
def ReverseComplement1(seq):
    """
    This function takes DNA sequence input and return the output as a reverse complement sequence.
    It also validates that the input is DNA seq with DNA nucleotides (ATCG). If not DNA seq, it will print out a text 
    telling not DNA seq and no output would be generated.
    """
#Convert input seq into upper case (would only work for string)
    seq_upper=seq.upper()
    #print out each step output--helpful in debugging
    print ("Input sequence in upper case: "+(seq_upper)) 
    
#Assess if DNA seq and return reverse complement of the input only if it is DNA seq
    for base in seq_upper:
        if "ATCG" not in base: #if not DNA seq, no output generated
            return ("This is not DNA--No output generated.")
        else: #if DNA seq
            #replace original nucleotides with complement bps
            seq_dict = {'A':'T','T':'A','G':'C','C':'G'} 
            #return complement bps in a reverse order
            return "".join([seq_dict[base] for base in reversed(seq_upper)]) 

#Test robustness of the function by entering input as numeric
ReverseComplement1(123) #error at the seq.upper step because numeric can't be converted to upper case
#Test robustness of function with non-DNA seq as input (starting with non-DNA nucleotides)..the code works!
ReverseComplement1("NTlAC")
#Test robustness of function with non-DNA seq as input (non-DNA nucleotides in the middle)..the code doesn't work!
ReverseComplement1("AHXCGT")
#Test correctness of the function: DNA seq input with space
ReverseComplement1("ACT CGTT")

#Q.1. Writing Function (B)
#Q.3. Self-critique:1. Readability: This function is a bit more complicated than ReverseComplement1
                   #2. Robustness: Input besides string does not work. 
                   #3. Correctness: The function is not accurate if you have a space in between your DNA seq. It will see it as non DNA seq. 
def ReverseComplement2(seq):
    """
    This function takes input and returns the output in a reversed order.
    For ATCG, it will be replaced with complement bps such as TAGC respectively.
    If not DNA seq as input (not ATCG), the function will return a text telling it is not DNA seq and no output generated.
    """
#convert input to upper case (would only work for string variables)
    seq_upper=seq.upper()
    #printing each step output--help in debugging
    print("This is the input seq in upper case: "+(seq))
    
#reverse the order of the input
    Reversed_upper=(seq_upper)[::-1] 
    print("This is the reverse of the input seq: "+(Reversed_upper))
    
#Replace the input DNA bps with their complements
    #create an empty list container for the output
    Reversed_Complement_Seq=[] 
    #replace ACTG with their complements
    for base in Reversed_upper: 
        if base=="A":
            Reversed_Complement_Seq.append("T")
        if base=="C":
            Reversed_Complement_Seq.append("G")
        if base=="T":
            Reversed_Complement_Seq.append("A")
        if base=="G":
            Reversed_Complement_Seq.append("C")
        results="".join(Reversed_Complement_Seq) #Concatenate the output
    
#Validate if the input seq is DNA seq:
    #Because of the nature of the loop written above, if the input strings are not ATCG, the results will ignore them, generating unequal numbers of input and output. 
    if len(seq)==len(results): #DNA seq would have no difference between the numbers of output elements and inputs
        print("Reversed Complement of the input seq: "+(results)) 
    else: #if not DNA seq, there would be difference in length of outputs and inputs. 
        print("Not DNA seq--No output generated.")
#Test robustness of the function by entering input as numeric
ReverseComplement2(123) #error at the seq.upper step because numeric can't be converted to upper case
#Test robustness of the function if not-DNA seq (starting with non-DNA nucleotides)..the code works!
ReverseComplement2("NTlAC")
#Test robustness of the function if not-DNA seq (non-DNA nucleotides in the middle): the code works!
ReverseComplement2("AHXCGT")

#Test correctness of the function: DNA seq input with space
ReverseComplement2("ACT CGTT")
#Q2. Test the funtions  
dna_sequence="ATGGAATGTTGTCCAAGATGAATAGTTTGTCATGATGCCCGTCGGGCAGATGGAGGACGGAGCTGAAGCCGCCGGGCCCGCAGCAAACTTCGTCTAGACAGCCATGGCCTGTAAAGGTAGGGATATGCGCTTAG"
#Test function1: ReverseComplement1
ReverseComplement1(dna_sequence)
#Test function2: ReverseComplement2
ReverseComplement2(dna_sequence)
###########################B.Tuples##################################
#Q.1.Create a tuple: 
tuple_1=("Met", 443, "Ser", "Arg", 567.5, "Lys", "Glu", 787, 8768, "Val", "Glu", "Pro", "Tyr", "57", "Ser", "His")
print(tuple_1)
#Q.2. Add strings to tuple_1
tuple_2=tuple_1+("Pro", "Lys", "Gln", "Thr", "Val", "Glu", "Cys", "Ala", "Glu")
print(tuple_2)
#Q.3.Determine if tuple_2 has same number of Glu and Val
print (("Number of Glu in tuple_2: ")+str(tuple_2.count("Glu")))
print (("Number of Val in tuple_2: ")+str(tuple_2.count("Val")))
if tuple_2.count("Glu")==tuple_2.count("Val"):
    print ("tuple_2 has same number of Glu and Val.")
if tuple_2.count("Glu")>tuple_2.count("Val"):
    print ("tuple_2 has more Glu than Val.")
else:
    print ("tuple_2 has fewer Glu than Val.")

#Q.3.(The easiest way to check if Glu and Val have the same number in tuple_2)
tuple_2.count("Glu")==tuple_2.count("Val")

#Q.4.Determine if Thr is present in tuple_2
"Thr" in tuple_2 #if Thr is present in tuple_2, it will return "True"; otherwise, "False"
#Q.5.Convert list to tuple
list = ["convert", "this", "list", "to", "a", "tuple"]
tuple_3=tuple(list)
print(tuple_3)
type(tuple_3)

#Q.6.Determine position of word "list"
tuple_3.index("list")

#Q.7.Try replace the word "convert" with "not converted"
tuple_3[0]="not converted" #the index of the word "convert" is zero
print(tuple_3)
#elements in tuple are not mutable. If we want to modify tuple elements, we would need to re-assign the whole tuple.
