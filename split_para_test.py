import json
import glob
from parasplitter import ParaSplitter

'''
ParaSplitter
split_by_idx() 사용 -> dictionary 
'''

def load_json(json_file):
    with open(json_file, "r", encoding="utf-8-sig") as js:
        content = json.load(js)
    return content


if __name__ == "__main__":
    foldername = "rawdata"
    #fname = 'testdata/test.json'
    #fname = 'testdata/test_copy.json'
    
    #load chapter split indicators
    chapter_dic = load_json('chapter_dic.json')['chapter_dic']
    
    files = glob.glob(f'{foldername}/*.json')    
    for fname in files:
        #load text 
        case = load_json(fname)
        text = case['case_main'].strip().split('\n')
        
        #call class obj and split text
        paras = ParaSplitter(chapter_dic, text)
        result = paras.split_by_idx()
        
        print(type(result), result)
        
        case.update(result)
        print(case)


