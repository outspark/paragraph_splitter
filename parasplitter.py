import re
from sys import exc_info

class ParaSplitter:

    def __init__(self, dic, text) -> None:
        self.dic = dic.copy()
        self.last_idx = len(text)
        self.text = text
    
    def split_by_idx(self):
        try:
            chapter_dic = self.update_start_idx(self.dic, self.text)
            chapter_dic = self.sort_by_start_idx(chapter_dic)
            chapter_dic = self.update_end_idx(chapter_dic, self.last_idx)
            return self.split_text_by_idx(chapter_dic, self.text)
        except:
            print(f'ParaSplitter 오류 ----> {exc_info}')
            return {self.text}

    def next_key(self,dic,key):
        keys = iter(dic)
        if key in keys:
            return next(keys, None)

    def get_end_idx(self,dic, key):
        n_key = self.next_key(dic,key)
        if n_key:
            end_idx = dic[n_key]['start_idx']
            if end_idx:
                return end_idx
        else:
            return None

    def remove_duplicates(self, cu_dic):
        pass

    def remove_none_keys(self,current_dic):
        remove_keys = []
        for key in current_dic:
            if current_dic[key]['start_idx'] is None:
                remove_keys.append(key)
        if remove_keys:
            for rk in remove_keys:
                print(f'Purging key: -->{rk}(Out of {len(remove_keys)}{remove_keys})')
                del current_dic[rk]
        return current_dic

    def update_start_idx(self,dic,text):
        for key in dic.keys():
            for idx,line in enumerate(text):
                line = line.replace(' ','')
                if re.search(dic[key]['regex'], line):
                    dic[key]['start_idx'] = idx
                    break
                else:
                    dic[key]['start_idx'] =  None
        return dic
                
    def update_end_idx(self,dic,text_length):
        for key in dic:
            end_idx = self.get_end_idx(dic, key)
            if end_idx:
                dic[key]['end_idx'] = end_idx
            else: 
                dic[key]['end_idx'] = text_length 
        return dic
    
    def sort_by_start_idx(self, dic):
        s_dic = self.remove_none_keys(dic)
        n_dic = dict(sorted(s_dic.items(), key=lambda item: item[1]['start_idx']))
        return n_dic

    def split_text_by_idx(self, dic, text):
        new_dic = {}
        for key in dic:
            start_idx = dic[key]['start_idx']
            end_idx = dic[key]['end_idx']
            if start_idx and end_idx:
                new_dic[key] = text[start_idx:end_idx]
                print(f'ParaSplitter found ----> {key} 인덱스값: ({start_idx}, {end_idx})')
            else:
                print(f'ParaSplitter did NOT find an end_idx for 인덱스값: ({start_idx}, {end_idx})')
        if new_dic:
            for k in new_dic:
                new_dic[k] = '\n'.join(new_dic[k])
        return new_dic    