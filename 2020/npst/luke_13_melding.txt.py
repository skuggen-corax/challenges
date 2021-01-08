import numpy as np
from PIL import Image
from collections import Counter
#import matplotlib.pyplot as plt
#import seaborn as sns

melding = '''27E522F722F5EE2CF3112E1C327CE73C3E37F1F1EE37CFEE773C57F2E357FE1C2E55FEFCF1332771C31333EC5F27E3353171135CE5C33E5C71F22215F31E7227C517E23E2F2C271C1352EC3231571223C3F172CCEF732EC21DBF1E
790045C2E086B118A6967777401F2E96643591F181CD666D27F6A85EEB1170CCB217AF523CECEC00968E79CEF73326D8F5324A05557E27722864B437E8B4B7F37C3EF2C4BBAE185C20C14664DF5E9A4532917CB1CBCFC935DFEA55
FB332BE1AEF17CC1F01F15EAC34FE6C1FC776A72637615117C922F8CE6F5E4F54C3297E5C37723D35F7379CE751E95C561FBF52851211521C5F4C55FD51C13FF35FCF5412571F4B5E4719E271FF4771D52913E97F0F55B1F157031
7851262C0FE5352FFB2E773A77CF3DF1C1C7A39101EDCF73FF851E951672837F92EEA2F755FC3FD157E31BCC3EFC9F55012DCE55F225E331731471C795FE11F2572F230EEE2F5D545B5205E71256C27B1EAEE635FAEFC9F32126C5
FADB627EF8B935F7347777A5E17EE1BD6FC56EEB0C3D407F7F42C1A32660172578C8E375E3C152A99E1CEB13CF2242CCDECDC40B77FE51357F3857F77A4B1FE57FC5C730865CC92F4D7E00AE121672E91FA9025FFF670E7FCE7F62
EB713717E33245E218553CF85C7FEF17CA2E0E13B254F177FED00DAFFDF10732CC0CC32FC53FE1A75575EA3F27C269B6A328CFC42CFE37C1EC2A7325EF329E5525712F171C9C78FEE0CE9FFF321A0498EE9E1BF5CF2B1C5CF1765E
5A5CEEE13FF3BC27C9FF33F6E54511EC192EB3C14724EC351F4FC2A2747C7B13218F7CC51E7115AE1F51792E2E218F7F0E5B51543F15F5F2777A7ECC21E307E3FFECF1C53CA7342C245FA125C35BF2EA35452167EF3613EE771A1E
503355CFDB9D22E254223C759D23508982F587EF417A89BA37927F85F03EFA3F71ACE5F68940126CCF1278D868176F1187C7ABDE3C064D8EE44804524B44F7ED9D64C3AAD935243CC6514A8A43367E7DE14177B5357AE3579C36C7
1F3CC5273C7C3C5E12E525E577ECFC217CC75F2C1731FC3F1CC122535F311737E172F2C271F153CF25E5CECCC1C71FEE3C7322321EC3F5EC2E332FF77EE322FCEF3F5C3157222E2327FFC3253E25E3553F7151C57FF5E121EDD121
2533512CEC175CEFE552EC2251F3537EE7FCCE171115EE5FF711FF7F5FE31CE1FE755C5F71FE2ECF3225E3FF2FE5CCEF57C3553227222CFF777C52FF3F727575CE531CC111FEC755EC135C15255F7CE221235271EC71E311713711'''

possible_heights = [2, 5, 7 ,10, 13, 14, 26, 35, 65, 70 ,91, 130, 182, 455]

def concat_reshape(mode="1"):
    concat_melding = "".join(melding.split('\n'))

    i = 0
    to_array = []
    while i < len(concat_melding):
        to_array.append(int(concat_melding[i:i+2], 16))
        i += 2

    for height in possible_heights:
        a = np.reshape(np.array(to_array), (height, -1))
        visu = Image.fromarray(a, mode=mode) # 1, L 
        visu.show()
    return 0

def transposed(mode="L"):
    split_melding = melding.split('\n')
    
    list_o_lists = [[] for lists in split_melding[0]]

    for i in range(len(split_melding[0])):
        for j in range(len(split_melding)):
            list_o_lists[i].append(split_melding[j][i])

    transposed_melding = "".join(["".join(list) for list in list_o_lists])

    i = 0
    to_array = []
    while i < len(transposed_melding):
        to_array.append(int(transposed_melding[i:i+2], 16))
        i += 2

    for height in possible_heights:
        a = np.reshape(np.array(to_array), (height, -1))
        visu = Image.fromarray(a, mode=mode) # 1, L 
        visu.show()
    return 0

def as_element():
    concat_melding = "".join(melding.split('\n'))

    i = 0
    to_array = []
    while i < len(concat_melding):
        to_array.append(concat_melding[i:i+2])
        i += 2

    c = Counter(to_array)
    return c
    

def as_high_low():
    new_melding = []
    for c in melding:
        if c == '\n':
            new_melding.append('\n')
        elif c in ['4', '6', 'A', '9', 'B', '0', '8', 'D']:
            new_melding.append('Ø')
        else:
            new_melding.append(' ')
    return new_melding

#transposed('1')
#concat_reshape('1')

#c = as_element()
#print('len', len(c))
#print('counts', c)

#sns.barplot(c)
#plt.show()

h = Counter(melding)
print('len', len(h))
print('counts', h)
# suspicious distribution ...

hightlow = "".join(as_high_low())

for line in hightlow.split('\n'):
    print(line)