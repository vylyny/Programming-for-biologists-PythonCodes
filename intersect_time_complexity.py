import sys #the sys module is used in running python script on a terminal

if sys.argv[1] == 'set':  #using "set" to find the intersection by typing "set" on the command line at position [1]
    print("Doing set implementation.\n")
    ds = 'set'
else:
    print("Doing list implementation.\n")
    ds = 'list' #using "list" to find the intersection, instead of "set"

with open("celegans_drosophila1.txt", 'r') as f1: #loading the first file
    D1 = f1.readlines() 

with open("drosophila_celegans1.txt", 'r') as f2: #loading the second file
    D2 = f2.readlines()

#creating empty list containers
x = []
y = []
num_xaxis = 50
for num in range(1,num_xaxis): #doing iterations for 49 times
    print("Doing iteration"+str(num)+"\n")

    D_in = D1[0:int(len(D1)*num/num_xaxis)]
    D_in2 = D2[0:int(len(D2)*num/num_xaxis)]

    import time
    print(len(D_in))
    print(len(D_in2))
    x.append(len(D_in))

    if ds == "set":
        D_in = set(D_in)
        D_in2 = set(D_in2)
        num_replicates = 1000
    else:   
        num_replicates = 2  # list is slower, so we do fewer replicates

    D_out = []
    start = time.time()
    for r in range(1, num_replicates):
        if (ds == "set"):
            D_out = D_in.intersection(D_in2)
        else:
            D_out=[]
            # add list implementation of intersection here
            for a in D_in:
                if a in D_in2:
                    D_out.append(a)           

    end = time.time()
    print((end - start)/num_replicates)
    y.append((end - start)/num_replicates)

# Add code here to output pdf of plot of size of input data (x-axis) versus time (y-axis)
# Save the files as "computational_complexity_netid_set.pdf" and "computational_complexity_netid_list.pdf"
import seaborn as sns
snsplot=sns.lineplot(x=x,y=y)
if sys.argv[1] == 'set':
    snsplot.savefig('computational_complexity_vc49_set.pdf')
else:
    snsplot.savefig('computational_complexity_vc49_list.pdf')
