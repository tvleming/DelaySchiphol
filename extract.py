"this program serves to extract flight delay data from .csv files"
"the data will be place in one list, with each flight as separate item"
"each flight consists of a number of message lines"
"each message has 19 inputs"
from exctracttools import *
starttime=time.time()

#name of data file
#fname='InputData.csv'
fname='InputData_example.csv'

#list with separate flights as inputs
flightlist=[]
#read data from .csv file
f=open(fname,'rb')
reader=csv.reader(f)

#read each line, assign flight numbers to tmplist
tmplist=[]

for row in reader:
    tmplist.append(row)
tmplist2 = []
f.close()

for i in range(2, len(tmplist)):
    a = tmplist[i-1][0]
    
        
    b = tmplist[i][0]
    c = tmplist[i-1][13]
    if a==b:
        if c =='EBA' or c== 'EBD':
            tmplist2.append(tmplist[i-1])
        if i== (len(tmplist)-1):
            tmplist2.append(tmplist[i])
            flightlist.append(tmplist2)
    else:
        flightlist.append(tmplist2)
        #print tmplist2
        tmplist2 = []
    
                        
    

    
    
                


#print flightlist


#remove first line with legend
del flightlist[0]

endtime=time.time()
dt=endtime-starttime
#print str(round(dt,3))+' s'

#deltat=timediff(flightlist[0][0][2],flightlist[0][0][3])

#calculate actual delay times for each flight, both inbound and outbound flights
delayin,delayout=0,0
for i in range(len(flightlist)):
    hr,mn=[],[]
    #print i,len(flightlist[i])
#    for j in range(4):
#        hr.append(int(flightlist[i][-1][j+2][-5:-3]))
#        mn.append(int(flightlist[i][-1][j+2][-2:]))
        
