from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import os, sys, datetime
from numpy import array

stopWords = set(stopwords.words('english'))
# folderName
folderName = sys.argv[1]
parsefolder = sys.argv[2]
writeinfolder = sys.argv[3]
tweetfolder =sys.argv[4]
# All Files inside the folder
filesList = os.listdir(folderName)
def filerename():
    
    os.chdir(folderName)
    for filename in filesList:
        f=filename.split('_')
        
        os.rename(filename,parsefolder+f[7]+'_'+filename)
    files = sorted(os.listdir(parsefolder))
    cluster(files)
def cluster(files):
    os.chdir(parsefolder)
    mylist=[]    
    for x in range(0,len(files)):
        pass
        count=x
        
        a=files[x].split('_')
        
        adt=a[8][:8]
        
        if x==0:
            pass
            
            d1 = datetime.datetime.strptime(a[0], "%Y%m%d%H%M%S")
            #print(d1)
        d2=d1+datetime.timedelta(minutes=10)
        s2=int(d2.strftime("%H%M%S"))
        d3=datetime.datetime.strptime(a[0], "%Y%m%d%H%M%S")
        mylist.append(d3.strftime("%H%M%S"))
        #print(mylist)
        i=0
        
                
        
        
        writenFile = writeinfolder+a[3]+'.txt'
        writenFile1 = writeinfolder+'@'+a[4]+'.txt'
        writenFile2 = writeinfolder+adt+'.txt'
        cluster_by_type(writenFile,files,x,a)
        cluster_by_user(writenFile1,files,x,a)
        cluster_by_date(writenFile2,files,x,a)
    cluster_by_time(mylist)
    tweetify()    
        
def cluster_by_type(writenFile,files,x,a):        
        os.chdir(parsefolder)
        oFile = open(writenFile,"a")
        
        f=files[x]
        # open each file
        
        with open(f, 'r') as content_file:
        # read contents of the file
            
            content = content_file.read()+" "+str(a[4])+" "+str(a[6])+"_"+str(a[7])+" "+str(a[8])
            
            oFile.write(content+"\n")
def cluster_by_user(writenFile1,files,x,a):          
        oFile = open(writenFile1,"a")
        
        f=files[x]
        
        with open(f, 'r') as content_file:
        # read contents of the file
            
            content = content_file.read()+" "+str(a[4])+" "+str(a[6])+"_"+str(a[7])+" "+str(a[8])
            
            oFile.write(content+"\n")    
def cluster_by_date(writenFile2,files,x,a):
        oFile = open(writenFile2,"a")

        f=files[x]
        # open each file

        with open(f, 'r') as content_file:
        # read contents of the file

            content = content_file.read()+" "+str(a[4])+" "+str(a[6])+"_"+str(a[7])+" "+str(a[8])

            oFile.write(content+"\n")
def cluster_by_time(mylist):
    os.chdir(parsefolder) 
    fileslice = sorted(os.listdir(parsefolder)) 
    #print(len(fileslice)) 
    c=1
    i=1
    start=int(mylist[0])
    end=start+ 1000
    length=len(mylist)
    #print(length)
    while(i < length):
        pass
        #print(mylist[i])
        
        fi=fileslice[i]
        a1=fileslice[i].split('_')
        

        node=int(mylist[i])
        #print(node)
        
        #print(mylist[i])
        #print(start)
        #print(end)
        
        if (node>=start and node<=end):
            pass
            #print(node)
        # open each file
            writenFile3 = writeinfolder+'timestamp'+str(c)+'.txt'
            oFile = open(writenFile3,"a")
            #print(node)
            with open(fi, 'r') as content_file:
            # read contents of the file
                content = content_file.read()+" "+str(a1[4])+" "+str(a1[6])+"_"+str(a1[7])+" "+str(a1[8])
                #print(content)
                #print(oFile)
                oFile.write(content+"\n")
                #print(content)
            i=i+1    
        else:
            start= end
            end = end + 1000
            c=c+1


               
#print(writeinfolder)
#print(filesList)
def tweetify():
    
    os.chdir(writeinfolder)
    filelist=sorted(os.listdir(writeinfolder))
    #print(filelist)
    for f in filelist:
        
        s=f.split('.')
        #print(s)
        #print(f)
        ofile=open(tweetfolder+s[0]+'_parsed.txt','w')
        #print(ofile)
        with open(f, 'r+') as fp:
                #print("checkpoint1")
                if f=='timestamp5.txt':
                    pass
                    print("inside")
                    fl=fp.read()
                    print(fl)
                    print(fp)
                for data in fp:
                    print(data)
                    words = word_tokenize(data)
                    print(words)
                    wordsFiltered = []
                    
                    ofile.write(data.rstrip()+" ")
                    for w in words:
                        if w not in stopWords and not w.isdigit() and len(w) > 3 :
                            wordsFiltered.append(w)
                            ofile.write(" ")
                            ofile.write("#"+w)
                    ofile.write(" #disaster.\n")
           
def main():
    filerename()

if __name__ == '__main__':
            
            main()

