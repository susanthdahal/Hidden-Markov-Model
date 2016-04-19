import sys
from collections import defaultdict
def viterbi(text,big_list):
    output_file=open('hmmoutput.txt','w')
    ptrans=big_list[0]
    pemit=big_list[1]
    tags=big_list[2]
    tag_values=tags.keys()
    text=text.split('\n')
    text.remove('')
    for line in text:
        sentence=line.split(' ')
        prob=[defaultdict(lambda :0)]
        tag_list=[]
        for k in tag_values:
            word=sentence[0]
            if(word in pemit and k in pemit[word]):
                temp=ptrans['q0'][k]
                temp=temp*(pemit[word][k]/tags[k])
                prob[0][k]=temp
            elif word not in pemit:
                prob[0][k]=ptrans['q0'][k]
        for i in range(1,len(sentence)):
            prob.append(defaultdict(lambda :0))
            for j in tag_values:
                if(sentence[i] in pemit and j in pemit[sentence[i]]):
                    prob[i][j]=max(prob[i-1][k]*ptrans[k][j]*(pemit[sentence[i]][j]/tags[k]) for k in tag_values)
                elif(sentence[i] not in pemit ):
                     prob[i][j]=max(prob[i-1][k]*ptrans[k][j] for k in tag_values)

        for pairs in prob:
            for tag,val in pairs.items():
                if pairs[tag]==max(pairs.values()):
                    tag_list.append(tag)
        for i in range(len(sentence)-1):
            output_file.write(sentence[i]+'/'+tag_list[i]+' ')
        output_file.write(sentence[len(sentence)-1]+'/'+tag_list[len(sentence)-1]+'\n')


def decoding():
    file=open('hmmmodel.txt','r')
    big_list=eval(file.read())
    file.close()
    test=open(sys.argv[1],'r')
    text=test.read()
    viterbi(text,big_list)


decoding()

