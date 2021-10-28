import sys
"""
    Import the sys module to run the ortholog script on the terminal.Numbers in [] correspond to positions to be typed on the 
    terminal. By default the boolean flag is 'False'
"""
xml_1=open(sys.argv[1],'r') #first xml input
xml_2=open(sys.argv[2],'r') #second xml input
output=open(sys.argv[3],'w') # file output to be written to
flag=sys.argv[4].upper()=='TRUE' #boolean flag to return reciprocal ortholog pairs if 'True' and return pairs from either speciesA to B or B to A if 'False'



#############################################Supplementary Functions######################################

from Bio.Blast import NCBIXML
def return_hits(a):
    """
    Using biopython this function first parse the xml file and then return only the hits with e-value less than 1e-20.The final     output is a list of hits with lengths correspond to the number of query with hit sequences (i.e those without hits were igno    red)
    """ 
    record=NCBIXML.parse(open(a)) #parsing xml file
    hit=[] #create an empty list to concatenate all the hits
    for blast_record in record:
        hit_sub=[] #sub_hit per query. If one query has more than one hit, those hits would be concatenated to form one list
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect<1e-20:
                    hit_sub.append(alignment.title) #for query  with multiple hits, each hit is appended to form a list of hits
        if len(hit_sub)>0: #iteration with no hit found (len(hit_sub)==0 is ignored
            hit.append(hit_sub) #append all hits from each query that has hits
    return hit #a list of all hits
    record.close()


def return_query_if_hits(a):
    """
    This function returns only the query ids that have hits. Those without are ignored. The indexes of the output list correspon    ds to those of  the list of hits identified using the above function. I separated them because it is too complicated or mayb    e impossible (?) to try to return two values using one function.
    """    
    record=NCBIXML.parse(open(a))
    query=[]
    for blast_record in record:
        hit_sub=[]
        for alignment in blast_record.alignments:
            if hsp.expect < 1e-20:
                hit_sub.append(alignment.title)
        if len(hit_sub)>0:
            query.append(blast_record.query)
    return query
    record.close()


def iterate_all_elements_in_list(a):
    r=[]
    for i in a:
        for j in i:
            r.append(j)
    return r



      
############################################################# Main_Function #######################################
    
def orthologs_pairs(xml_1,xml_2,flag='TRUE'):
    xml_1_hits=return_hits(xml_1)
    xml_1_query=return_query_if_hits(xml_1)
    dict_xml_1=dict(zip(xml_1_query,xml_1_hits)
    #xml_1_query_ALL=iterate_all_elements_in_list(xml_1_query)
   # xml_2_hits=return_hits(xml_2)
    xml_2_query=return_query_if_hits(xml_2)
    dict_xml_2=dict(zip(xml_2_query,xml_2_hits)
    #xml_1_hits_ALL=iterate_all_elements_in_list(xml_2_hits)
    if flag:
        intersect=list((set(iterate_all_elements_in_list(xml_1_query)&set(iterate_all_elements_in_list(xml_1_hits)))
        results=dict((k,dict_xml_1[k]) for k i intersect)
        return results
    else:
        results= merge{**dict_xml_1,**dict_xml_2}
        return results
    with open('output','w') as f:
    f.writelines('{}\t\t{}\n'.format(k,v) for k,v in results.items())
    
