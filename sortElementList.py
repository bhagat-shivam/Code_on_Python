def sort(li1, li2):
    f1 = {}
    final = [] 
    f1 = {li1[i]: li2[i] for i in range(len(li2))} 
    f1st = {k: v for k, v in sorted(f1.items(), key = lambda item: item[1])}

    for i in f1st.keys():
      final.append(i)
    return final

li1 = ["a", "b", "c","d","e"]
li2 = [0,1,1,0,1]

list3 = sort(li1,li2)
print(list3)