from player import *
from output_functions import *


# read file content
with open('assets\\abc.txt') as f:
    abc_raw = f.readlines()[0]

with open('assets\\scale.txt') as f:
    scale_raw = f.readlines()[0]


# import scale into python list type
scale = scale_raw.split()
# import abc into python list type
abc = abc_raw.split()

# get length of list and abc
scale_len = len(scale)
abc_len = len(abc)


print(f"provided scale: {scale}")
print(F"provided abc: {abc}")

# calculate values for padding scale
verhältniss = abc_len/scale_len
verhältniss_floor = abc_len//scale_len
nachkomma_stelle = verhältniss-verhältniss_floor

# position until needs to append at
stelle_in_liste = nachkomma_stelle*scale_len
# how often it needs to extend the list
anzahl_extend = verhältniss_floor-1


# extend the scale
i = 0
while i < anzahl_extend:
    i += 1
    scale.extend(scale[0:scale_len-1])


# append missing to get to abc length
for count, value in enumerate(scale):
    while count <= stelle_in_liste+1:
        scale.append(value)
        break


# matching logic
# match padded scale to abc
def str_to_scale(text):
    string_lower = text.lower()

    scale_list = []

    for count, wordcharac in enumerate(string_lower):
        for count2, list_charac in enumerate(abc):
            if wordcharac == list_charac:
                scale_list.append(scale[count2])
    return scale_list


# ui logic option to read from file aswell
print("Provide scale in scale.txt aswell as abc in abc.txt")

text_input = input("Enter your Text you want translated to your Scale:\n")
if text_input == "!from(text.txt)!":
    with open('text.txt') as f:
        text = f.read()
    notes = str_to_scale(text)
else:
    notes = str_to_scale(text_input)


print("please choose your Output Mode:")

print("0: only printing out notes")
print("1: saving notes in file note_output.txt")
print("2: interactive printing + playback")
print("3: saving audio in output.wav")
print("4: saving audio in audio_output.wav + saving notes in output")
print("5: saving audio + printing out notes")

output_mode = input().strip()

if output_mode == "0":
    output_0(notes)
elif output_mode == "1":
    output_1(notes)
elif output_mode == "2":
    output_2(notes)
elif output_mode == "3":
    output_3(notes)
elif output_mode == "4":
    output_4(notes)
elif output_mode == "5":
    output_5(notes)
else:
    print("invalid outputmode!")
