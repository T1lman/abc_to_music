

#read files contens
with open('abc.txt') as f:
    abc_raw = f.readlines()[0]

with open('scale.txt') as f:
    scale_raw = f.readlines()[0]


scale=scale_raw.split()
abc=abc_raw.split()

scale_len=len(scale)
abc_len=len(abc)



print(f"provided scale: {scale}")
print(F"provided abc: {abc}")



verhältniss=abc_len/scale_len
verhältniss_floor=abc_len//scale_len
nachkomma_stelle=verhältniss-verhältniss_floor

stelle_in_liste=nachkomma_stelle*scale_len
anzahl_append=verhältniss_floor-1


og_scale=scale
i=0
while i < anzahl_append:
    i+=1
    scale.extend(scale[0:scale_len-1])


for count, value in enumerate(scale):
    while count<=stelle_in_liste+1:
        scale.append(value)
        break









def str_to_scale(text):
    string_lower=text.lower()

    scale_list=[]

    for count,wordcharac in enumerate(string_lower):
        for count2,list_charac in enumerate(abc):
            if wordcharac==list_charac:
                scale_list.append(scale[count2])
    return scale_list


print("Provide scale in scale.txt aswell as abc in abc.txt")

text_input=input("Enter your Text you want translated to your Scale:\n")
print(str_to_scale(text_input))


