import json
from sys import exc_info
from parasplitter import ParaSplitter

'''
ParaSplitter
split_by_idx() 사용 -> dictionary 
'''

def load_json(json_file, file_type):
    with open(json_file, "r", encoding="utf-8-sig") as js:
        content = json.load(js)
    return content[file_type]
    

if __name__ == "__main__":
        
    fname = 'testdata/test.json'
    #fname = 'testdata/test_copy.json'

    #load text 
    text = load_json(fname, 'case_main').split('\n')

    #load chapter split indicators
    chapter_dic = load_json('chapter_dic.json', 'chapter_dic')

    #call class obj and split text
    paras = ParaSplitter(chapter_dic, text)
    result = paras.split_by_idx()
    
    print(type(result), result)
        


