dic = {
    0: " ",
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
    27: "\n",
    28: ":"
}


def reverse_dic(dic: dict):
    new_dic = {}
    for key in dic:
        k = dic[key]
        v = key
        new_dic[k] = v
    return new_dic


encode_dic = {
    " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "\n": 27,
    ":": 28
}


def encode(text: str):
    encoded_str = ''
    for c in text.lower():
        encoded_str += str(encode_dic[c])+'.'
    return encoded_str[:-1]

def decode(n):
    numbers = n.split('.')
    str = ''
    for k in numbers:
        str += dic[int(k)]
    return str


str = decode('19.1.13.5.18.0.9.19.0.1.0.7.15.15.4.0.16.18.15.7.18.1.13.13.5.18.0.20.5.3.8.5.1.18')
print(str)