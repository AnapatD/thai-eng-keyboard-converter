import sys, os, readchar
method_banner = ('''
 ___________________
|                   |
| [1] : ENG TO THAI |
| [2] : THAI TO ENG |
|___________________|
''')
#choose method
print(method_banner)

#check input
try:
    method = int(input('Please choose your method (1 or 2) : '))
    if method < 1:
        print('Please input a correct method (1 or 2)')
        sys.exit(0)
    elif method > 2:
        print('Please input a correct method (1 or 2)')
        sys.exit(0)
except ValueError:
    print('Please input a correct method (1 or 2)')
    sys.exit(0)
else:
    txt = str(input('input : '))
    dict = {
     'A':'ฤ',
     'a':'ฟ', 
     'B':'ฺ', 
     'b':'ิ', 
     'C':'ฉ', 
     'c':'แ', 
     'D':'ฏ', 
     'd':'ก', 
     'E':'ฎ', 
     'e':'ำ', 
     'F':'โ', 
     'f':'ด', 
     'G':'ฌ', 
     'g':'เ', 
     'H':'็', 
     'h':'้', 
     'I':'ณ', 
     'i':'ร', 
     'J':'๋', 
     'j':'่', 
     'K':'ษ', 
     'k':'า', 
     'L':'ศ', 
     'l':'ส', 
     'M':'?', 
     'm':'ท', 
     'N':'์', 
     'n':'ื', 
     'O':'ฯ', 
     'o':'น', 
     'P':'ญ', 
     'p':'ย', 
     'Q':'๐', 
     'q':'ๆ', 
     'R':'ฑ', 
     'r':'พ', 
     'S':'ฆ', 
     's':'ห', 
     'T':'ธ', 
     't':'ะ', 
     'U':'๊', 
     'u':'ี', 
     'V':'ฮ', 
     'v':'อ', 
     'W':'"', 
     'w':'ไ', 
     'X':')', 
     'x':'ป', 
     'Y':'ํ', 
     'y':'ั', 
     'Z':'(', 
     'z':'ผ', 
     '!':'+', 
     '1':'ๅ', 
     '@':'๑', 
     '2':'/', 
     '#':'๒', 
     '3':'-', 
     '$':'๓', 
     '4':'ภ', 
     '%':'๔', 
     '5':'ถ', 
     '^':'ู', 
     '6':'ุ', 
     '&':'฿', 
     '7':'ึ', 
     '*':'๕', 
     '8':'ค', 
     '(':'ต', 
     '9':'๖', 
     ')':'๗', 
     '0':'จ', 
     '_':'๘', 
     '-':'ข', 
     '+':'๙', 
     '=':'ช', 
     '{':'ฐ', 
     '[':'บ', 
     '}':',', 
     ']':'ล', 
     '|':'ฅ', 
     '\\':'ฃ', 
     ':':'ซ', 
     ';':'ว', 
     '"':'.', 
     "'":'ง', 
     '<':'ฒ', 
     ',':'ม', 
     '>':'ฬ', 
     '.':'ใ', 
     '?':'ฦ', 
     '/':'ฝ'
     }
    eng_dct = {k:v for k, v in dict.items()}
    TH_TO_ENG_Dict = eng_dct
    ENG_TO_TH_Dict = dict
    if method == 1:
        trans = txt.maketrans(ENG_TO_TH_Dict)
    elif method == 2:
        trans = txt.maketrans(TH_TO_ENG_Dict)
    txt = txt.translate(trans)
    print(txt)
    print('Press Any Key To Exit')
    k = readchar.readchar()
