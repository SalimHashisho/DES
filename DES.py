# DES algorithm code was based on shubhamupadhyay's code from https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/ 
__author__ = "Salim Hashisho"


from tkinter import *
root = Tk("DES")
root.title("")
frame = Frame(root, bd=10, width=500, height=600)
frame.grid(row=0, column=0)
frame.grid_propagate(0)

Title = Label(frame, text="Data Encryption Standard",
              font=("Arial", 13), width=25, height=2)
Title.place(x=250, y=20, anchor="center")

textLabel = Label(frame, text="Text",
                  font=("Arial", 10), width=15, height=1)
textLabel.place(x=100, y=60, anchor="center")
textEntry = Entry(frame, width=20, borderwidth=5)
textEntry.place(x=250, y=60, anchor="center")

KeyLabel = Label(frame, text="Key",
                 font=("Arial", 10), width=15, height=1)
KeyLabel.place(x=100, y=85, anchor="center")
KeyEntry = Entry(frame, width=20, borderwidth=5)
KeyEntry.place(x=250, y=85, anchor="center")


#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################
# Initial Permutation Table
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

# Expansion Table
exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
         6, 7, 8, 9, 8, 9, 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1]

# Permutation Table
per = [16, 7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2, 8, 24, 14,
       32, 27, 3, 9,
       19, 13, 30, 6,
       22, 11, 4, 25]

# S-box Table
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# permutation choice 1
pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# permutation choice 2: from 56 bits to 48 bits
pc2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# Final Permutation Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

# Number of bit shifts in each round
shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################


def hex2bin(hex_numb):
    dictionary = {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111"}
    bin_numb = ""
    for i in range(len(hex_numb)):
        bin_numb = bin_numb + dictionary[hex_numb[i]]
    return bin_numb


def bin2hex(bin_numb):
    dictionary = {
        "0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1110": 'E',
        "1111": 'F'}
    hex_numb = ""
    for i in range(0, len(bin_numb), 4):
        hex_numb += dictionary[bin_numb[i:i+4]]

    return hex_numb


def bin2dec(binary):
    decimal, i = 0, 0
    while(binary != 0):
        # 0 then add nothing, 1 then add 2^rank
        decimal += (binary % 10) * 2**i
        binary = binary//10
        i += 1
    return decimal


def dec2bin(num):
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


def permute(inp, permutation_table, bits_needed):
    # Permute function to rearrange the bits
    permutation = ""
    for i in range(0, bits_needed):
        # -1 since the tables assumes counting start at 1 instead of 0
        permutation += inp[permutation_table[i] - 1]
    return permutation


def shift_left(k, nth_shifts):
    # shifting the bits towards left by nth shifts
    for i in range(nth_shifts):
        k = k[1:len(k)] + k[0]
    return k


def xor(a, b):
    # calculating xow of two strings of binary number a and b
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################


def encrypt(pt, rkb, leftArr, rightArr, expArr, xor1Arr, sboxArr, permArr, xor2Arr):
    pt = hex2bin(pt)

    # Initial Permutation
    pt = permute(pt, initial_perm, 64)
    #print("After initial permutation", bin2hex(pt))

    # Splitting
    left = pt[0:32]
    right = pt[32:64]

    # 16 rounds
    for i in range(0, 16):
        # 1-> Expansion D-box: Expanding the 32 bits data into 48 bits
        right_expanded = permute(right, exp_d, 48)
        expArr.append(bin2hex(right_expanded))

        # 2-> XOR RoundKey[i] and right_expanded
        xor_x = xor(right_expanded, rkb[i])
        xor1Arr.append(bin2hex(xor_x))

        # 3-> S-Box
        sbox_str = ""
        for j in range(0, 8):
            row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = bin2dec(
                int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
            val = sbox[j][row][col]
            sbox_str += dec2bin(val)
        s_res = sbox_str
        sboxArr.append(bin2hex(s_res))

        # 4-> Permutation
        sbox_str = permute(s_res, per, 32)
        permArr.append(bin2hex(sbox_str))

        # 5-> XOR left and sbox_str
        result = xor(left, sbox_str)
        xor2Arr.append(bin2hex(result))

        left = result
        # Swapper
        if(i != 15):
            left, right = right, left
        leftArr.append(bin2hex(left))
        rightArr.append(bin2hex(right))

    # Combination
    combine = left + right

    # Final permutation: final rearranging of bits to get cipher text
    cipher_text = permute(combine, final_perm, 64)
    return bin2hex(cipher_text)

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################


def key_gen(key, rkb, rk):
    # change to binary and acquire the 56-bit key
    key = permute(hex2bin(key), pc1, 56)

    # Splitting
    left = key[0:28]
    right = key[28:56]

    # 16 rounds
    for i in range(0, 16):
        # Shifting the bits by nth shifts
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])

        # Combination of left and right string
        combine_str = left + right

        # Compression of key from 56 to 48 bits
        round_key = permute(combine_str, pc2, 48)

        rkb.append(round_key)
        rk.append(bin2hex(round_key))

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################


def enc(mode):
    # "123456ABCD132536"
    pt = textEntry.get().upper()
    # "AABB09182736CCDD"
    key = KeyEntry.get().upper()

    # binary round keys
    rkb = []
    # hex round keys
    rk = []

    key_gen(key, rkb, rk)

    # binary round keys in reverse for decryption
    rkb_rev = rkb[::-1]
    # hex round keys in reverse for decryption
    rk_rev = rk[::-1]

    left = []
    right = []
    expArr = []
    xor1Arr = []
    sboxArr = []
    permArr = []
    xor2Arr = []
    if mode == 1:
        result = encrypt(pt, rkb_rev, left, right,
                         expArr, xor1Arr, sboxArr, permArr, xor2Arr)
    else:
        result = encrypt(pt, rkb, left, right, expArr,
                         xor1Arr, sboxArr, permArr, xor2Arr)

    p = []
    for i in range(16):
        p.append(left[i] + "      " + right[i] + "      " + rk[i])

    b1 = Button(frame, text="Round " + str(1) + "  ", font=("Arial",
                                                            10), command=lambda: round(1, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145)
    b2 = Button(frame, text="Round " + str(2) + "  ", font=("Arial",
                                                            10), command=lambda: round(2, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25)
    b3 = Button(frame, text="Round " + str(3) + "  ", font=("Arial",
                                                            10), command=lambda: round(3, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*2)
    b4 = Button(frame, text="Round " + str(4) + "  ", font=("Arial",
                                                            10), command=lambda: round(4, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*3)
    b5 = Button(frame, text="Round " + str(5) + "  ", font=("Arial",
                                                            10), command=lambda: round(5, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*4)
    b6 = Button(frame, text="Round " + str(6) + "  ", font=("Arial",
                                                            10), command=lambda: round(6, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*5)
    b7 = Button(frame, text="Round " + str(7) + "  ", font=("Arial",
                                                            10), command=lambda: round(7, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*6)
    b8 = Button(frame, text="Round " + str(8) + "  ", font=("Arial",
                                                            10), command=lambda: round(8, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*7)
    b9 = Button(frame, text="Round " + str(9) + "  ", font=("Arial",
                                                            10), command=lambda: round(9, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*8)
    b10 = Button(frame, text="Round " + str(10), font=("Arial", 10),
                 command=lambda: round(10, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*9)
    b11 = Button(frame, text="Round " + str(11), font=("Arial", 10),
                 command=lambda: round(11, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*10)
    b12 = Button(frame, text="Round " + str(12), font=("Arial", 10),
                 command=lambda: round(12, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*11)
    b13 = Button(frame, text="Round " + str(13), font=("Arial", 10),
                 command=lambda: round(13, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*12)
    b14 = Button(frame, text="Round " + str(14), font=("Arial", 10),
                 command=lambda: round(14, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*13)
    b15 = Button(frame, text="Round " + str(15), font=("Arial", 10),
                 command=lambda: round(15, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*14)
    b16 = Button(frame, text="Round " + str(16), font=("Arial", 10),
                 command=lambda: round(16, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr)).place(x=70, y=145+25*15)

    Label(frame, text="Left                Right              Round Key",
          font=("Arial", 10),  height=1).place(x=170, y=120)
    for i in range(16):
        Label(frame, text=p[i]+"              ",
              font=("Arial", 10),  height=1).place(x=170, y=145+25*i)
    Label(frame, text="Result: " + result + "                   ",
          font=("Arial", 10),  height=1).place(x=70, y=545)


def round(i, left, right, rk, expArr, xor1Arr, sboxArr, permArr, xor2Arr):
    top = Toplevel(root)
    top.title("R " + str(i))
    topframe = Frame(top, bd=10, width=400, height=300)
    topframe.grid(row=0, column=0)
    topframe.grid_propagate(0)
    topTitle = Label(topframe, text="Round " + str(i),
                     font=("Arial", 13), width=25, height=2)
    topTitle.place(x=200, y=20, anchor="center")

    expLabel = Label(topframe, text="Expanding the 32 bits data into 48 bits: " + expArr[i-1],
                     font=("Arial", 10),  height=1).place(x=10, y=50)
    xor1Label = Label(topframe, text="XOR RoundKey[i] with Expanded data: " + xor1Arr[i-1],
                      font=("Arial", 10),  height=1).place(x=10, y=80)
    sboxLabel = Label(topframe, text="S-Box: " + sboxArr[i-1],
                      font=("Arial", 10),  height=1).place(x=10, y=110)
    permLabel = Label(topframe, text="Permutation: " + permArr[i-1],
                      font=("Arial", 10),  height=1).place(x=10, y=140)
    xor2Label = Label(topframe, text="XOR left part with permuted data: " + xor2Arr[i-1],
                      font=("Arial", 10),  height=1).place(x=10, y=170)
    leftLabel = Label(topframe, text="Left part: " + left[i-1],
                      font=("Arial", 10),  height=1).place(x=10, y=200)
    rightLabel = Label(topframe, text="Right part: " + right[i-1],
                       font=("Arial", 10),  height=1).place(x=10, y=230)
    keyLabel = Label(topframe, text="Round key: " + rk[i-1],
                     font=("Arial", 10),  height=1).place(x=10, y=260)


EncryptButton = Button(frame, text="Encrypt", width=7,
                       height=1, command=lambda: enc(0))
EncryptButton.place(x=330, y=58)
DecryptButton = Button(frame, text="Decrypt", width=7,
                       height=1, command=lambda: enc(1))
DecryptButton.place(x=400, y=58)

root.mainloop()
