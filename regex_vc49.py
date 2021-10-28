
# coding: utf-8

# In[31]:


import re #import regular expression


# In[ ]:


#A. Sequence Statistics


# In[3]:


##function from previous homework

def load_fasta(f):
    """
    Function load_fasta(f) takes a fasta file input (str) and returns only the sequences (str),
    the sequence headers were removed.
    Each sequence is separated by a comma. It also checks if the fasta file if empty. If empty, it
    will prompt an error message "empty fast file".
    """
    f= open (f,"r") 
    line=f.readlines() 
    #print (len(line)) #commenting out debugging step
    if len(line) == 0:  #check if the input fasta file is empty
            return ("empty fasta file.") # if no line (empty file), print this text
    #if not empty:
    sequences = [] #empty list for sequences
    seq_id = [] #empty list for seq indentifiers
    for i in line:
            if i[0] == '>': #line starts with '>' helps identify seq_id
                if seq_id:                               
                    sequences.append(seq)
                seq_id = i[1:-1].split('|') #split the seq identifiers by '|' into a separate line..easy to remove and only keep the sequences
                seq = ''                               
            else: #for line that is not seq_id (i.e. sequences)
                seq += i[:-1] #return all elements in each line except the last one which is '\n'
    sequences.append(seq)  #only append the sequences ignoring the seq_id             
    return('\n\n\n'.join(map(str,sequences))) #convert elements in lists to strings I used three \n(s) here so that it is easier to view and also convenient when wrting code for translation as one codon consists of three characters. 
    f.close()


# In[144]:


#DraII restriction site: [AG]GG[ATCG]CC[CT]
def display_restriction_sites( sequence ):
    """
    Displays the DraII restriction enzyme cut sites in  <sequence>
    """
    DraII = '[AG]GG[ATCG]CC[CT]'
    found = re.findall( DraII , sequence ) #use re expression to find all restriction sites of DraII in the input sequence
    # print out the results
    for i in found:
        return '\n'.join(i for i in found) #convert result to string separated by \n


# In[229]:


def seq_statistics(f):
    """
    This funciton takes in a fasta file as an input. It uses the load_fasta function to spit out sequences in the fasta file as string.
    The display_restriction_sites function is used to scan through the whole sequence for DraII restriction sites. The final output of 
    this seq_statistic function is percent distribution of each nucleotide at each index of DraII restriction sites.
    """
    f=load_fasta(f) #open the fasta file
    #print (f)
    a=display_restriction_sites(f) #display restriction sites
    #print (a)
    alist=a.split() #convert all restriction sites into a list
    #print(alist)
    first_pos='' #create empty strings for each index of DraII restriction sites stored in a list above
    second_pos=''
    third_pos=''
    fourth_pos=''
    fifth_pos=''
    sixth_pos=''
    seventh_pos=''
    for i in alist:
        #concatenate the 1st,2nd,3rd,4th,5th,6th and 7th character(element) of each index in the list of all restriction sites found, respectively
        first_pos+= i[0] 
        second_pos+=i[1]
        third_pos+=i[2]
        fourth_pos+=i[3]
        fifth_pos+=i[4]
        sixth_pos+=i[5]
        seventh_pos+=i[6]
        
    #calculating each nucletotide distribution at each position of the DraII restriction sites
    n=len(first_pos) #each element at different positions in a list of all restriction sites should have the same lenght n
    A_1= ((first_pos.count("A")/n)*100)
    T_1= ((first_pos.count("T")/n)*100)
    C_1= ((first_pos.count("C")/n)*100)
    G_1= ((first_pos.count("G")/n)*100)
    
    A_2= ((second_pos.count("A")/n)*100)
    T_2= ((second_pos.count("T")/n)*100)
    C_2= ((second_pos.count("C")/n)*100)
    G_2= ((second_pos.count("G")/n)*100)
    
    A_3= ((third_pos.count("A")/n)*100)
    T_3= ((third_pos.count("T")/n)*100)
    C_3= ((third_pos.count("C")/n)*100)
    G_3= ((third_pos.count("G")/n)*100)
    
    A_4= ((fourth_pos.count("A")/n)*100)
    T_4= ((fourth_pos.count("T")/n)*100)
    C_4= ((fourth_pos.count("C")/n)*100)
    G_4= ((fourth_pos.count("G")/n)*100)
    
    A_5= ((fifth_pos.count("A")/n)*100)
    T_5= ((fifth_pos.count("T")/n)*100)
    C_5= ((fifth_pos.count("C")/n)*100)
    G_5= ((fifth_pos.count("G")/n)*100)
    
    A_6= ((sixth_pos.count("A")/n)*100)
    T_6= ((sixth_pos.count("T")/n)*100)
    C_6= ((sixth_pos.count("C")/n)*100)
    G_6= ((sixth_pos.count("G")/n)*100)
    
    A_7= ((seventh_pos.count("A")/n)*100)
    T_7= ((seventh_pos.count("T")/n)*100)
    C_7= ((seventh_pos.count("C")/n)*100)
    G_7= ((seventh_pos.count("G")/n)*100)
    #print out % distribution of each nucleotide at each position of DraII restriction sites using string.format()
    print ("Distribution of each nucleotide in the 1st position of the restriction sites:\n%A: {}\n%T: {}\n%C: {}\n%G: {}".format(str(A_1),str(T_1),str(C_1),str(G_1)))
    print ("Distribution of each nucleotide in the 2nd position of the restriction sites:\n%A: {}\n%T: {}\n%C: {}\n%G: {}".format(str(A_2),str(T_2),str(C_2),str(G_2)))
    print ("Distribution of each nucleotide in the 3rd postion of the restriction sites:\n%A: {}\n%T: {}\n%C: {}\n%G: {}".format(str(A_3),str(T_3),str(C_3),str(G_3)))
    print ("Distribution of each nucleotide in the 4th position of the restriction sites:\n%A: {}\n%T: {}\n%C: {}\n%G: {}".format(str(A_4),str(T_4),str(C_4),str(G_4)))
    print ("Distribution of each nucleotide in the 5th position of the restriction sites:\n%A: {}\n%T: {}\n%C: {}\n%G: {}".format(str(A_5),str(T_5),str(C_5),str(G_5)))
    print ("Distribution of each nucleotide in the 6th position of the restriction sites:\n%A: {}\n%T: {}\n%C: {}\n%G: {}".format(str(A_6),str(T_6),str(C_6),str(G_6)))
    print ("Distribution of each nucleotide in the 7th position of the restriction sites:\n%A: {}\n%T: {}\n%C: {}\n%G: {}".format(str(A_7),str(T_7),str(C_7),str(G_7)))


# In[230]:


#test the function using 'draII.fa'
seq_statistics("draII.fa")


# In[ ]:


#B.Restriction Site scanning


# In[4]:


#code from previous homework

def get_reverse_complement(seq):
    """
    This function takes DNA sequence input (str) and returns the output as a reverse complement sequence.
    If not DNA seq, it will print out a text telling not DNA seq.
    """
    try:
        seq_upper=seq.upper() #Convert input seq into upper case (would only work for string)
        for base in seq_upper:
            seq_dict = {'A':'T','T':'A','G':'C','C':'G','\n':'\n'} #a dict for complement bps
              #return complement bps in a reverse order
            return "".join([seq_dict[base] for base in reversed(seq_upper)])
    except Exception as e:
        return "The input seq is not a valid DNA seq."  #this prints out an error message telling the input is not a valid DNA seq      


# In[225]:


#StyI restriction site: CC[AT][AT]GG 
def restriction_site_scan(f):
    '''
    This function takes in fasta file as an input. It scans for restriction sites of StyI (CC[AT][AT]GG) in both input sequence and
    the reversed complement of the input sequence. The function returns indices of all the restriction sites found. Finally, it replaces
    all the restriction sites with 'NNNNNN' and return new sequences with Ns for both the input seq and reversed complement seq.
    '''
    f=load_fasta(f) #load fasta file and spit out seq as string
    #print(type(f))
    reversed_complement=get_reverse_complement(f) #convert input seq to its reversed complement
    #print(type(reversed_complement))
    #print("This is the original seq: " +(f)+"\n")
    #print("This is reversed complement: " +(reversed_complement))
    StyI='CC[AT][AT]GG'#styI restriction site
    print ('Indices of where the StyI restriction sites are found for the original seq: '+ str([(m.start(0)) for m in re.finditer(StyI, f)])) #print out indices of all restriction sites found for the input seq
    sub=re.sub(StyI,'NNNNNN',f) #replace all StyI restriction sites found with 'NNNNNN'
    print ('Original sequence with substitues Ns:\n{}'.format(sub)) #print out out the input seq with Ns using string.format
    print ('\n\nIndices of where the StyI restriction sites are found for the reversed complement seq: '+ str([(m.start(0)) for m in re.finditer(StyI, reversed_complement)])) #print out indices of restriction sites in reversed complement
    sub_reversedcompl=re.sub(StyI,'NNNNNN',reversed_complement) #replace restriction sites of StyI with 'NNNNNN' for the reversed complement seq
    print ('Reversed complement sequence with substitues Ns:\n{}'.format(sub_reversedcompl)) #print out the reversed complement seq with Ns
    


# In[226]:


#test the function using 'styI.fa'
restriction_site_scan("styI.fa")


# In[ ]:


##Bonus Point
#I have used the str.format to print out the results for seq_statistic (f) function and restriction_site_scan(f) function.

