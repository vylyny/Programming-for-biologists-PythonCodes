
#Import modules needed:
from Bio.Blast import NCBIXML
import sys

############################################# Supplementary Functions ######################################

def return_hits(a):
    '''

    Using biopython this function first parses the input xml file and then returns only the hits with e-value less than 1e-20.The final     
    output is a list of hits with lengths correspond to the number of query with hit sequences (i.e those without hits were ignored)

    ''' 
    record=NCBIXML.parse(open(a)) #parsing xml file
    hit=[] #create an empty list to concatenate all the hits
    for blast_record in record:
        hit_sub=[] #sub_hit per query. If one query has more than one hit, those hits would be concatenated to form one list
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect<1e-20: #only include hit with e-value less than 1e-20
                    hit_sub.append(alignment.title) #for query  with multiple hits, each hit is appended to form a list of hits
        if len(hit_sub)>0: #iteration with no hit found (len(hit_sub)==0 is ignored
            hit.append(hit_sub) #append all hits from each query that has hits
    return hit #a list of all hits
    record.close()

####################################

def return_query_if_hits(a):
    '''
    
    This function takes in an xml file and returns only the query ids that have hits. Those without are ignored. The indices of the output list correspond to those of the list of hits 
    identified using the above function.This is important to build a dictionary later.  I separated return_hits function and this function because it is too complicated or maybe 
    impossible (?) to try to return two values using one function.

    '''    
    record=NCBIXML.parse(open(a)) #parsing input xml file
    query=[] #create an empty list of query
    for blast_record in record:
        hit_sub=[]
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < 1e-20:
                    hit_sub.append(alignment.title)
        if len(hit_sub)>0: #only for query with at least one hit
            query.append(blast_record.query) #append all query with at least one hit into a list
    return query
    record.close()
    
####################################

def convert_key_value_dict_to_list(a,no_reverse):
    '''
    
    This function takes in a dictionary and a boolean flag (no_reverse). The output is a list of a dictionary's key concatenated to its corresponding value. If flag is true,
    the output would be a key+value. If false, it would be a value + key. I reversed them so that it is easier to compare and find intersects of paired orthologs between
    the two species down the line.

    '''
    r=[]
    for i in a: #i is the key of dict
        for x in a[i]: #x is the value..this would iterate through all values of each key (Certain key has a list of multiple hit values)
            if no_reverse:
                r.append(x+"    "+i)  #making a tab in the middle for ease of writing out a tab-delimited file as an output
            else:
                r.append(i+"    "+x)
    return r

############################################################# Identify ortholog pairs #######################################

    '''

    Imported the sys module to run the ortholog script on the terminal.Numbers in [] correspond to positions to be typed on the 
    terminal. By default the python scrip is sys.argv[0] and the boolean flag is optional (if not typed in, it would be assumed to be "TRUE".

    '''
xml_1=sys.argv[1] #first xml input
xml_2=sys.argv[2] #second xml input
output=open(sys.argv[3],'w') # file output to be written to


dict_xml_1=dict(zip(return_query_if_hits(xml_1),return_hits(xml_1))) #Creating a dictionary of the first xml file with query as keys and corresponding hits as values
dict_xml_2=dict(zip(return_query_if_hits(xml_2),return_hits(xml_2)))  #Creating a dictionary of the second xml file with query as keys and corresponding hits as values

xml_1_key_value_in_a_list=convert_key_value_dict_to_list(dict_xml_1,True) #Convert key and values of dict_xml_1 into a list of key,value,key,value,key,value...and so on
xml_2_key_value_in_a_list=convert_key_value_dict_to_list(dict_xml_2,False) #Do the same as aboove for xml2, but this time, the order is reversed so that it would match the xml_1 list created above

##BOOLEAN flag

if len(sys.argv)==4 or sys.argv[4].upper()=='TRUE': #boolean flag is optional or if true, it would return a reciprocal ortholog match
    intersection=list(set(xml_1_key_value_in_a_list)&set(xml_2_key_value_in_a_list)) #converting the two lists above (xml_1_key_value_in_a_list and xml_2_key_vallue_in_a_list) into sets and find the intersections
    for i in intersection:  #writing output file delimited by tab and sparated by two indentations in between each ortholog 
        output.write('%s\n\n' % i)
     
elif sys.argv[4].upper()=='FALSE': #if FALSE is passed, the output would be  HSP from either species A to B or B to A
    union=list(set(xml_1_key_value_in_a_list)|set(xml_2_key_value_in_a_list)) #finding union of the two sets; duplicates are removed
    for l in union:  #writing out the output file delimited by tab and separated by two indentations in between each pair
        output.write('%s\n\n' % l )
    
#####This script runs perfectly on the terminal. It takes  slightly longer time though. About 10 minutes per run...The algorithm complexity for finding the intersection is big O (n*n)
#####where n is the lenght of the shortest set..