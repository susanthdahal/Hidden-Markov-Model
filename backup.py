import sys
import time
from collections import defaultdict
def viterbi(text,big_list):
    output_file=open('hmmoutput.txt','w')
    pstart=big_list[0]
    ptrans=big_list[1]
    pemit=big_list[2]
    tags=big_list[3]
    smooth_pstart=big_list[4]
    word_dict=big_list[5]
    tag_values=tags.keys()
    tag_values=list(tag_values)
    text=text.split('\n')
    text.remove('')
    output_list=""
    for line in text:
        sentence=line.split(' ')
        prob=defaultdict(lambda :0.0000001)
        back=defaultdict(lambda :"")
        for i in range(len(sentence)):
            if(i==0):
                for j in range(len(tag_values)):
                    if( not pstart.get(tag_values[j])):
                        pstart[tag_values[j]]=smooth_pstart
                    if(not pemit.get(sentence[i]+'#'+tag_values[j])):
                        prob[str(j)+'#'+str(i)]=pstart[tag_values[j]]
                    else:
                        prob[str(j)+'#'+str(i)]=pstart[tag_values[j]]*pemit[sentence[i]+'#'+tag_values[j]]
                    back[tag_values[j]+'#'+str(i)]="qo"
            else:
                its_tags=tag_values
                if( word_dict.get(sentence[i]) ):
                    its_tags=word_dict[sentence[i]]
                for j in range(len(tag_values)):
                    prob_max=0
                    back_max=0
                    for k in range(len(its_tags)):
                        if(not ptrans.get(tag_values[k]+'#'+tag_values[j])):
                            ptrans[tag_values[k]+'#'+tag_values[j]]=1.0/(tags[tag_values[k]]+len(tag_values))
                        if(pemit.get(sentence[i]+'#'+tag_values[j])):
                            temp=prob[str(k)+'#'+str(i-1)]*ptrans[tag_values[k]+'#'+tag_values[j]]*pemit[sentence[i]+'#'+tag_values[j]]
                        else:
                            temp=prob[str(k)+'#'+str(i-1)]*ptrans[tag_values[k]+'#'+tag_values[j]]
                        back_temp=prob[str(k)+'#'+str(i-1)]*ptrans[tag_values[k]+'#'+tag_values[j]]
                        if temp>prob_max:
                            prob[str(j)+'#'+str(i)]=temp
                            prob_max=temp
                        if back_temp>back_max:
                            back[tag_values[j]+'#'+str(i)]=tag_values[k]
                            back_max=back_temp
        max=0
        ind=-1
        i=len(sentence)-1
        back_ptr=[]
        for j in range(len(tag_values)):
            if(prob[str(j)+'#'+str(i)]>max):
                max=prob[str(j)+'#'+str(i)]
                ind=j
        back_ptr.insert(0,tag_values[ind])
        for i in range(len(sentence)-1,0,-1):
            back_ptr.insert(0,back[back_ptr[0]+'#'+str(i)])
        for i in range(len(sentence)):
            output_list+=sentence[i]
            temp='/'+back_ptr[i]
            output_list+=temp
            output_list+=' '
        output_list+='\n'
    output_file.write(output_list)



def decoding():
    file=open('hmmmodel.txt','r')
    big_list=eval(file.read())
    file.close()
    test=open(sys.argv[1],'r')
    text=test.read()
    viterbi(text,big_list)


t1=time.time()
decoding()
t2=time.time()
print(t2-t1)