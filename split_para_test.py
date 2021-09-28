import json
import os
import glob
from parasplitter import ParaSplitter

'''
ParaSplitter
- INPUT: rawdata 폴더의 json 파일
- split_by_idx() 사용 -> dictionary 
- OUTPUT: original json + paragraph split dict 
'''

def load_json(json_file):
    with open(json_file, "r", encoding="utf-8-sig") as js:
        content = json.load(js)
    return content

def save_json(fname, dic):
    folder_path = os.path.dirname(fname)
    fn = os.path.basename(fname)
    with open(f'{folder_path}/parasplit/PARASPLIT_{fn}', 'w', encoding="utf-8") as f:
        json.dump(dic, f, ensure_ascii=False)

def add_key(parasplit_res, original_json):
    original_json['case_main_parasplit'] = parasplit_res
    return original_json


if __name__ == "__main__":
    foldername = "rawdata"
    #fname = 'testdata/test.json'
    #fname = 'testdata/test_copy.json'

    #load chapter split indicators
    default_dic = load_json('chapter_dic.json')['chapter_dic']
    
    files = glob.glob(f'{foldername}/*.json')    

    for fname in files:
        
        #load json 
        case = load_json(fname)
        
        #call class obj and split text
        paras = ParaSplitter(default_dic, case, 'case_main') #takes chapter_dic.json, case data, key
        result = paras.split_by_idx()
        
        # print(type(result), result)

        # type(result) -> dictionary

        new_json = add_key(result, case)
        save_json(fname, new_json)



