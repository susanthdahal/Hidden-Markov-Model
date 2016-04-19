import sys
tags={}
ptrans={}
pemit={}
ptrans['q0']={}
tags['q0']=0.0
def make_model():
    file=open(sys.argv[1])
    lines=file.read()
    my_list=lines.split('\n')
    my_list.remove('')
    for i in range(len(my_list)):
        words=my_list[i].split(' ')
        prev=''
        for j in words:
            key=j[:-3]
            value=j[-2:]
            if(value in tags):
                tags[value]+=1.0
            else:
                tags[value]=1.0
            if(prev==''):
                if(value in ptrans['q0']):
                    ptrans['q0'][value]+=1.0
                else:
                    ptrans['q0'][value]=1.0
                tags['q0']+=1.0
            else:
                if(prev not in ptrans):
                    ptrans[prev]={}
                else:
                    if(value not in ptrans[prev]):
                        ptrans[prev][value]=1.0
                    else:
                        ptrans[prev][value]+=1.0
            prev=value

            if(key not in pemit):
                pemit[key]={}
                pemit[key][value]=1.0
            else:
                if(value not in pemit[key]):
                    pemit[key][value]=1.0
                else:
                    pemit[key][value]+=1.0

    for prev in tags:
        for current in tags:
            if prev not in ptrans:
                ptrans[prev] = {}
                ptrans[prev][current] =1.0/(sum(tags.values()+len(tags)))
            else:
            	if(current not in ptrans[prev]):
               		ptrans[prev][current]=0.0
            	ptrans[prev][current]=(ptrans[prev][current]+1.0)/(tags[prev]+len(tags))

    output_list=[ptrans,pemit,tags]
    file.close()
    file=open('hmmmodel.txt','w')
    file.write(str(output_list))

make_model()