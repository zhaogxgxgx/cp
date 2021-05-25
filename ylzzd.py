import yaml
import os


def zd():
    file_name=os.path.split(os.path.realpath(__file__))[0]
    yamlpath=os.path.join(file_name,'cs.yaml')
    f=open(yamlpath,'r',encoding='utf-8')
    cont=f.read()
    x=yaml.load(cont,Loader=yaml.Loader)
    yaml_str=x['yl']['Fpk'],x['yl']['Ppk'],x['yl']['fgp'],\
             x['yl']['Lot_size'],x['yl']['Cache'],\
             x['yl']['Thread'],x['yl']['Barrel'],\
             x['yl']['Block_number'],x['yl']['Temporary'],\
             x['yl']['Tmp_dir_2'],x['yl']['End'],x['yl']['Domain']
    yaml_list=list(yaml_str)
    return yaml_list


new_list=zd()
new_list1=['&&','chia','plots','create']
new_list2=['-f','-p','-a','-k','-b','-r','-u','-n','-t','-2','-d','-e']
new_dict={new_list2:new_list for new_list2,new_list in zip(new_list2,new_list)}


def lb():
    new_list=[]
    for key,value in new_dict.items():
        if value==None:
            continue
        if key=='-e':
            if value!=True:
                continue
            new_list.append(key)
            continue
        new_list.append(key)
        new_list.append(str(value))
    return new_list


chia_locate=os.path.abspath('chia')

new_list1.extend(lb())
new_list3=[str(fp) for fp in new_list1]
str_1=' '.join(new_list3)


os.system('cd'+' '+chia_locate+' '+str_1)

