'''
https://lovit.github.io/nlp/2018/08/28/levenshtein_hangle/
'''

def levenshtein(s1, s2, cost=None, debug=False):
    if len(s1) < len(s2):
        return levenshtein(s2, s1, debug=debug)

    if len(s2) == 0:
        return len(s1)

    if cost is None:
        cost = {}

    # changed
    def substitution_cost(c1, c2):
        if c1 == c2:
            return 0
        return cost.get((c1, c2), 1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            # Changed
            substitutions = previous_row[j] + substitution_cost(c1, c2)
            current_row.append(min(insertions, deletions, substitutions))

        if debug:
            print(current_row[1:])

        previous_row = current_row

    return previous_row[-1]


def extend_cost_dict(cost_dict):
    new_dict = dict([[(k[1],k[0]),v] for k,v in cost_dict.items()])
    # print(new_dict)
    return {**cost_dict, **new_dict}

def slice_to_same_len(a,b):
    b1 = b[:len(a)]
    b2 = b[-len(a):]
    return [b1,b2]
        
a = '주장의요지'
b = '증거의요지'
cost = {('의', '외'):0.1,('관', '대'):0.1}
b_list = slice_to_same_len(a,b)
new_cost = extend_cost_dict(cost)

res = []
for b in b_list:
    res.append(levenshtein(a, b, new_cost))

print(min(res), res)