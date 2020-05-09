# imports

import json
import os
from collections import defaultdict

# define and create folders

data_folder = "../data/"

def check_and_mkdir(folder):
    '''
    check if the directory exists and if not, create one
    '''

    if not os.path.isdir(data_folder + folder):
        os.mkdir(data_folder + folder)

    return 

check_and_mkdir("agent/")
check_and_mkdir("customer/")

# load data

with open(data_folder + "train.json") as f:
    train = json.load(f)

with open(data_folder + "dev.json") as f:
    dev = json.load(f)


# distribute data into corresponding folders

def data_distribute(data):
    '''
    distribute data into corresponding folders
    '''

    rd = {'agent':{'source':[],
    'target':[]},
    'customer':{'source':[],
    'target':[]}}

    for conid, utters in data.items():
        for utter in utters:
            rd[utter['speaker']]['source'].append(utter['source'])
            rd[utter['speaker']]['target'].append(utter['target'])

    return rd

def write_to_text(dict, file_prefix):
    '''
    write the retrieved data to txt file
    '''

    for speaker, uttrs in dict.items():
        for typee, sents in uttrs.items():
            path = data_folder + speaker + "/" + file_prefix + "_" + typee + ".txt"
            with open(path, 'w') as f:
                for sent in sents:
                    f.write(sent + "\n")


def explore_lengths(dict):

    for speaker, uttrs in dict.items():
        for typee, sents in uttrs.items():
            print(speaker, typee, len(sents))

rd_train = data_distribute(train)
rd_dev = data_distribute(dev)

# print("train:")
# explore_lengths(rd_train)
# print("dev:")
# explore_lengths(rd_dev)

write_to_text(rd_train, "train")
write_to_text(rd_dev, 'dev')

            





