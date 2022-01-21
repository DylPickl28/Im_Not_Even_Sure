# needs numpy 1.19.3 installed rather than numpy 1.19.4 installed, windows 10 2004 doesn't like 1.19.4 for some reason
import array
from array import *
import numpy
from numpy import array
import math
import cmath

secret_word = "Hello Javi"
secret_word2 = "Hello JAvi"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False
cooldown = 0
trial = 1
too_many = False
while guess != secret_word and guess != secret_word2 and not (out_of_guesses) and not (too_many):
    if guess_count < guess_limit:
        guess = input("Enter Password: ")
        guess_count += 1
        if guess == secret_word:
            break
        elif guess == secret_word2:
            break
        else:
            print("Incorrect Password ")
    else:
        if guess_count <= 20:
            cooldown += 15
            print("Password Attempt Limit Exceeded, Wait " + str(cooldown) + " Seconds Before Guessing Again.")
            import time

            time.sleep(cooldown)
            guess_limit += 4
        else:
            too_many = True
if too_many:
    print("Too Many Failed Password Attempts, Restart To Try Again ")
    exit()

if out_of_guesses:
    print("Password Attempt Limit Exceeded, Wait " + str(cooldown) + " Seconds Before Guessing Again.")
    import time

    time.sleep(cooldown)

print("Hello Sir, It Is Nice To See You Again.\n")

import time

time.sleep(1.10)

analysis = 0
while analysis == 0:
    als1 = input("Encryption Analysis On Or Off?\n1: On\n2: Off\n")
    if als1 == "1":
        als = True
        break
    elif als1 == "on":
        als = True
        break
    elif als1 == "On":
        als = True
        break
    elif als1 == "2":
        als = False
        break
    elif als1 == "off":
        als = False
        break
    elif als1 == "Off":
        als = False
        break
    else:
        print("\nInvalid Selection\n")
print("")


def encrypt(code):
    global range
    length_code = len(code)
    message = str(input("Enter Message You Would Like To Encrypt:\n"))
    length_mess = len(message)

    def split2(code):
        return [char for char in code]

    def split(message):
        return [char for char in message]

    def split_list2(list_code):
        half_split2 = length_code // 2
        return list_code[:half_split2], list_code[half_split2:]

    def split_list(nums):
        half_split = length_mess // 2
        return nums[:half_split], nums[half_split:]

    code_2lines = False
    mess_2lines = False
    if int(length_code) % 2 == 0:
        list_code = split2(code)
        list_code = list(map(int, list_code))
        list_code = [int(i) for i in list_code]
        split_code_list1, split_code_list2 = split_list2(list_code)
        split2_code_list1, split2_code_list2 = split_list2(list_code)
        code_2lines = True
    else:
        list_code = array(split2(code))
        list_code = list(map(int, list_code))
        list_code = [int(i) for i in list_code]
        list_code2 = [int(k) for k in list_code]

    if int(length_mess) % 2 == 0:
        nums = split(message)
        alsmess = split(message)
        nums1, nums2 = split_list(nums)
    else:
        alsmess = split(message)
        nums = array(split(message))
    mess_to_code = {
        " ": 1,
        "a": 2,
        "b": 3,
        "c": 4,
        "d": 5,
        "e": 6,
        "f": 7,
        "g": 8,
        "h": 9,
        "i": 10,
        "j": 11,
        "k": 12,
        "l": 13,
        "m": 14,
        "n": 15,
        "o": 16,
        "p": 17,
        "q": 18,
        "r": 19,
        "s": 20,
        "t": 21,
        "u": 22,
        "v": 23,
        "w": 24,
        "x": 25,
        "y": 26,
        "z": 27,
        "A": 28,
        "B": 29,
        "C": 30,
        "D": 31,
        "E": 32,
        "F": 33,
        "G": 34,
        "H": 35,
        "I": 36,
        "J": 37,
        "K": 38,
        "L": 39,
        "M": 40,
        "N": 41,
        "O": 42,
        "P": 43,
        "Q": 44,
        "R": 45,
        "S": 46,
        "T": 47,
        "U": 48,
        "V": 49,
        "W": 50,
        "X": 51,
        "Y": 52,
        "Z": 53,
        ".": 54,
        ",": 55,
        "!": 56,
        "?": 57,
        "_": 58,
        "\'": 59,
        "\"": 60,
        "/": 61,
        "^": 62,
        "$": 63,
        "#": 64,
        "@": 65,
        "%": 66,
        "&": 67,
        "*": 68,
        "(": 69,
        ")": 70,
        "{": 71,
        "}": 72,
        "[": 73,
        "]": 74,
        "\n": 75,
        "\t": 76,
        "\\": 77,
        ":": 78,
        ";": 79,
        "<": 80,
        ">": 81,
        "=": 82,
        "+": 83,
        "-": 84,
        "1": 85,
        "2": 86,
        "3": 87,
        "4": 88,
        "5": 89,
        "6": 90,
        "7": 91,
        "8": 92,
        "9": 93,
        "0": 94,
    }
    uu = 0
    length_list = []
    while uu < length_mess:
        length_list.append(uu)
        uu += 1
    length_dict = dict(zip(length_list, nums))
    trials = 1
    new_mess = []
    mess_dict = dict(zip(length_list, new_mess))
    while trials <= length_mess:
        if trials <= len(length_dict):
            new_mess.append(mess_to_code.get(length_dict[(trials - 1)]))
            trials += 1
        else:
            break

    def split_list(new_mess):
        half_split = length_mess // 2
        return new_mess[:half_split], new_mess[half_split:]

    if int(length_mess) % 2 == 0:
        new_mess1, new_mess2 = split_list(new_mess)
        mess_2lines = True
    else:
        mess_2lines = False

    matr1 = []
    matr2 = []
    if code_2lines:
        matr1 = [split_code_list1,
                 split_code_list2]
    else:
        matr1 = [list_code]

    if mess_2lines:
        matr2 = [new_mess1,
                 new_mess2]
    else:
        matr2 = [new_mess]

    a = 0
    x = 0
    if code_2lines and mess_2lines:
        ans1 = []
        ans1a = []
        ans1ab = []
        ans1b = []
        ans1bb = []
        ans1_list = []
        ans1_length = len(ans1) - 1
        split_code_length1 = len(split_code_list1)
        new_mess_length1 = len(new_mess1)
        new_mess_length3 = len(new_mess1) + len(new_mess2)
        split_code_length3 = len(split_code_list1) + len(split_code_list2)
    elif code_2lines and not mess_2lines:
        ans1 = []
        ans1a = []
        ans1ab = []
        ans1b = []
        ans1bb = []
        ans1_list = []
        ans1_length = len(ans1) - 1
        split_code_length1 = len(split_code_list1)
        new_mess_length = len(new_mess)
        split_code_length3 = len(split_code_list1) + len(split_code_list2)
        new_mess_length = len(new_mess)
        remove_splcode = len(new_mess) - 1
    elif mess_2lines and not code_2lines:
        ans1 = []
        ans1a = []
        ans1ab = []
        ans1b = []
        ans1bb = []
        ans1_list = []
        ans1_length = len(ans1) - 1
        split_code_length = len(list_code)
        new_mess_length1 = len(new_mess1)
        new_mess_length3 = len(new_mess1) + len(new_mess2)
        resize_code = ()
    else:
        ans1 = []
        ans1a = []
        ans1ab = []
        ans1b = []
        ans1bb = []
        ans1_list = []
        ans1_length = len(ans1) - 1
        split_code_length = len(list_code)
        new_mess_length = len(new_mess)
        remove_splcode = len(new_mess) - 1
        resize_code = ()

    if code_2lines and mess_2lines:
        while a < length_mess:
            split_code_length1 = len(split_code_list1)
            new_mess_length1 = len(new_mess1)
            if split_code_length1 < new_mess_length1:
                split_code_list1.insert(a + split_code_length1, split_code_list1[a])
                split_code_list2.insert(a + split_code_length1, split_code_list2[a])
                a += 1
            elif split_code_length1 > new_mess_length1:
                del (split_code_list1[new_mess_length1:])
                del (split_code_list2[new_mess_length1:])
                a += 1
            else:
                ans1a = numpy.add(new_mess1, split_code_list2)
                ans1b = numpy.add(new_mess2, split_code_list1)
                ans1a = numpy.multiply(ans1a, split_code_list1)
                ans1b = numpy.multiply(ans1b, split_code_list2)
                ans1 = numpy.append(ans1a, ans1b)
                ans1_length = len(ans1) - 1
                a = length_mess
        else:
            if als == True:
                bibs_list = []
                sans2 = list(alsmess)
                entry = True
                t = 0
                while entry == True:
                    try:
                        if len(bibs_list) < len(sans2):
                            bib = str(sans2[t])
                            bibs_list.append(bib)
                            t += 1
                        else:
                            break
                    except:
                        print("\ninvalid entry\n")

                bibs_list.sort()
                print("\n\nDECRYPTED MESSAGE ANALYSIS")
                bibs2 = bibs_list
                bibs4 = []
                amt = []
                n = 0
                for x in bibs2:
                    while n < len(bibs2):
                        amt.append(bibs2.count(bibs2[n]))
                        try:
                            while bibs2[n] == bibs2[(n + 1)]:
                                del (bibs2[n])
                            else:
                                bibs4.append(bibs2[n])
                                n += 1
                        except:
                            bibs4.append(bibs2[n])
                            n += 1
                amt_tot = 0
                o = 0
                for l in amt:
                    while o < len(amt):
                        amt5 = int(amt[o])
                        amt_tot += amt5
                        o += 1
                ncomp = bibs_list

                z = 0
                c = 0
                y = 0
                nums9 = []
                p = 0
                while p < len(bibs4):
                    nums9.append(str(bibs4[p]))
                    p += 1
                longstry = max(nums9, key=len)
                len_longy = len(str(longstry))
                len_long1y = len_longy + 1
                while y < len(bibs4):
                    len_long2y = (len_long1y - len(str(bibs4[z])))
                    z += 1
                    c += 1
                    y += 1
                print("")

                len_nums = len(bibs_list)
                print("total number of entries = " + str(amt_tot))
                print("\nData Quantity Representation: ")
                h = 0
                j = 0
                k = 0
                bibs7 = []
                u = 0
                while u < len(bibs4):
                    bibs7.append(str(bibs4[u]))
                    u += 1
                total_amt = len_nums
                longstr = max(bibs7, key=len)
                len_long = len(longstr)
                len_long1 = len_long + 1
                while h < len(bibs4):
                    monum = amt[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (amt[j] / amt_tot) * 100
                    len_long2 = (len_long1 - len(bibs4[k]))
                    print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                    h += 1
                    j += 1
                    k += 1

                print("")
                hh = 0
                jj = 0
                kk = 0
                nums8 = []
                u = 0
                while u < len(bibs4):
                    nums8.append(str(bibs4[u]))
                    u += 1
                longstrx = max(nums8, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                print("Data Percent Represenation")
                while hh < len(amt):
                    monum2 = round((amt[jj] * 100) / amt_tot)
                    monum3 = (amt[jj])
                    monum4 = ((amt[jj]) * 100) / amt_tot
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / amt_tot) * 100
                    len_long2x = (len_long1x - len(str(bibs4[kk])))
                    print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1
            if als == True:
                sans1 = list(ans1)
                nums = []
                entry = 0
                while entry < len(sans1):
                    try:
                        number = int(sans1[entry])
                        nums.append(number)
                        entry += 1
                    except:
                        try:
                            number = float(number)
                            nums.append(number)
                            entry += 1
                        except:
                            print("\nnumbers only in list\n")

                nums.sort()
                print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                ncomp = nums
                ncomp2 = (sum(ncomp))

                n = 0
                nums3 = nums
                lists = []
                ncomp9 = nums
                ncomp7 = len(ncomp9)
                nums2 = []
                for x in nums3:
                    while n < len(nums3):
                        lists.append(nums3.count(nums3[n]))
                        try:
                            while nums3[n] == nums3[(n + 1)]:
                                del (nums3[n])
                            else:
                                nums2.append(nums3[n])
                                n += 1
                        except:
                            nums2.append(nums3[n])
                            n += 1

                tot_sum = sum(nums)
                len_nums = len(nums)
                mean = (tot_sum / len_nums)
                print("mean = " + str(mean))
                import statistics

                if int(len_nums) % 2 == 0:
                    len1 = (len_nums // 2)
                    len2 = ((len_nums // 2) + 1)
                    median1 = (nums[len1] + nums[len2]) / 2
                    median = statistics.median(nums)
                    print("median = " + str(median))
                else:
                    len1 = round((len_nums // 2) + 1)
                    median1 = nums[len1]
                    median = statistics.median(nums)
                    print("median = " + str(median))
                high_num = max(lists)
                index1 = lists.index(high_num)
                mode = nums2[index1]
                print("mode = " + str(mode))
                d = nums2[0]
                lenz2 = len(nums2) - 1
                f = nums2[lenz2]
                range = (f - d)
                print("range = " + str(range) + "; " + str([d, f]))

                hh = 0
                jj = 0
                kk = 0
                nums7 = []
                u = 0
                while u < len(nums2):
                    nums7.append(str(nums2[u]))
                    u += 1
                longstr = max(nums7, key=len)
                len_long = len(str(longstr))
                len_long1 = len_long + 1
                print("total sum = " + str(ncomp2))
                print("\npercent composition by value: ")
                while hh < len(nums2):
                    monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                    monum3 = (nums2[jj] * lists[jj])
                    monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp2) * 100
                    len_long2 = (len_long1 - len(str(nums2[kk])))
                    print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1

                print("\npercent composition by quantity: ")
                h = 0
                j = 0
                k = 0
                longstrx = max(nums7, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                total_amt = sum(lists)
                while h < len(nums2):
                    monum = lists[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (monum / total_amt) * 100
                    len_long2x = (len_long1x - len(str(nums2[k])))
                    print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                    h += 1
                    j += 1
                    k += 1

                rr = 0
                tt = 0
                yy = 0
                print("\ndata percent represenation:")
                while rr < len(lists):
                    monum2 = round((lists[tt] * 100) / ncomp7)
                    monum3 = (lists[tt])
                    monum4 = ((lists[tt]) * 100) / ncomp7
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp7) * 100
                    len_long2x = (len_long1x - len(str(ncomp[yy])))
                    print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    rr += 1
                    tt += 1
                    yy += 1
            import random
            alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            rand_alpha = random.choice(alpha)
            print("\nEncrypted Message: ")
            vv = 0
            ans11 = []
            while vv < len(ans1):
                ans11.append(str(ans1[vv]) + str(random.choice(alpha)))
                vv += 1
            print(*ans11, sep=("."))
    elif code_2lines and not mess_2lines:
        while a < length_mess:
            split_code_length1 = len(split_code_list1)
            new_mess_length = len(new_mess)
            if new_mess_length == 1:
                ans1a = numpy.add(new_mess, split_code_list2[0])
                ans1 = numpy.multiply(ans1a, split_code_list1[0])
                ans1_length = len(ans1) - 1
                a = length_mess
            elif split_code_length1 < new_mess_length:
                split_code_list1.insert(a + split_code_length1, split_code_list1[a])
                split_code_list2.insert(a + split_code_length1, split_code_list2[a])
                a += 1
            elif split_code_length1 > new_mess_length:
                del (split_code_list1[new_mess_length:])
                del (split_code_list2[new_mess_length:])
                a += 1
            else:
                ans1a = numpy.add(new_mess, split_code_list2)
                ans1 = numpy.multiply(ans1a, split_code_list1)
                ans1_length = len(ans1) - 1
                a = length_mess
        else:
            if als == True:
                bibs_list = []
                sans2 = list(alsmess)
                entry = True
                t = 0
                while entry == True:
                    try:
                        if len(bibs_list) < len(sans2):
                            bib = str(sans2[t])
                            bibs_list.append(bib)
                            t += 1
                        else:
                            break
                    except:
                        print("\ninvalid entry\n")

                bibs_list.sort()
                print("\n\nDECRYPTED MESSAGE ANALYSIS")
                bibs2 = bibs_list
                bibs4 = []
                amt = []
                n = 0
                for x in bibs2:
                    while n < len(bibs2):
                        amt.append(bibs2.count(bibs2[n]))
                        try:
                            while bibs2[n] == bibs2[(n + 1)]:
                                del (bibs2[n])
                            else:
                                bibs4.append(bibs2[n])
                                n += 1
                        except:
                            bibs4.append(bibs2[n])
                            n += 1
                amt_tot = 0
                o = 0
                for l in amt:
                    while o < len(amt):
                        amt5 = int(amt[o])
                        amt_tot += amt5
                        o += 1
                ncomp = bibs_list

                z = 0
                c = 0
                y = 0
                nums9 = []
                p = 0
                while p < len(bibs4):
                    nums9.append(str(bibs4[p]))
                    p += 1
                longstry = max(nums9, key=len)
                len_longy = len(str(longstry))
                len_long1y = len_longy + 1
                while y < len(bibs4):
                    len_long2y = (len_long1y - len(str(bibs4[z])))
                    z += 1
                    c += 1
                    y += 1
                print("")

                len_nums = len(bibs_list)
                print("total number of entries = " + str(amt_tot))
                print("\nData Quantity Representation: ")
                h = 0
                j = 0
                k = 0
                bibs7 = []
                u = 0
                while u < len(bibs4):
                    bibs7.append(str(bibs4[u]))
                    u += 1
                total_amt = len_nums
                longstr = max(bibs7, key=len)
                len_long = len(longstr)
                len_long1 = len_long + 1
                while h < len(bibs4):
                    monum = amt[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (amt[j] / amt_tot) * 100
                    len_long2 = (len_long1 - len(bibs4[k]))
                    print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                    h += 1
                    j += 1
                    k += 1

                print("")
                hh = 0
                jj = 0
                kk = 0
                nums8 = []
                u = 0
                while u < len(bibs4):
                    nums8.append(str(bibs4[u]))
                    u += 1
                longstrx = max(nums8, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                print("Data Percent Represenation")
                while hh < len(amt):
                    monum2 = round((amt[jj] * 100) / amt_tot)
                    monum3 = (amt[jj])
                    monum4 = ((amt[jj]) * 100) / amt_tot
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / amt_tot) * 100
                    len_long2x = (len_long1x - len(str(bibs4[kk])))
                    print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1
            if als == True:
                sans1 = list(ans1)
                nums = []
                entry = 0
                while entry < len(sans1):
                    try:
                        number = int(sans1[entry])
                        nums.append(number)
                        entry += 1
                    except:
                        try:
                            number = float(number)
                            nums.append(number)
                            entry += 1
                        except:
                            print("\nnumbers only in list\n")

                nums.sort()
                print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                ncomp = nums
                ncomp2 = (sum(ncomp))

                n = 0
                nums3 = nums
                lists = []
                ncomp9 = nums
                ncomp7 = len(ncomp9)
                nums2 = []
                for x in nums3:
                    while n < len(nums3):
                        lists.append(nums3.count(nums3[n]))
                        try:
                            while nums3[n] == nums3[(n + 1)]:
                                del (nums3[n])
                            else:
                                nums2.append(nums3[n])
                                n += 1
                        except:
                            nums2.append(nums3[n])
                            n += 1

                tot_sum = sum(nums)
                len_nums = len(nums)
                mean = (tot_sum / len_nums)
                print("mean = " + str(mean))
                import statistics

                if int(len_nums) % 2 == 0:
                    len1 = (len_nums // 2)
                    len2 = ((len_nums // 2) + 1)
                    median1 = (nums[len1] + nums[len2]) / 2
                    median = statistics.median(nums)
                    print("median = " + str(median))
                else:
                    len1 = round((len_nums // 2) + 1)
                    median1 = nums[len1]
                    median = statistics.median(nums)
                    print("median = " + str(median))
                high_num = max(lists)
                index1 = lists.index(high_num)
                mode = nums2[index1]
                print("mode = " + str(mode))
                d = nums2[0]
                lenz2 = len(nums2) - 1
                f = nums2[lenz2]
                range = (f - d)
                print("range = " + str(range) + "; " + str([d, f]))

                hh = 0
                jj = 0
                kk = 0
                nums7 = []
                u = 0
                while u < len(nums2):
                    nums7.append(str(nums2[u]))
                    u += 1
                longstr = max(nums7, key=len)
                len_long = len(str(longstr))
                len_long1 = len_long + 1
                print("total sum = " + str(ncomp2))
                print("\npercent composition by value: ")
                while hh < len(nums2):
                    monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                    monum3 = (nums2[jj] * lists[jj])
                    monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp2) * 100
                    len_long2 = (len_long1 - len(str(nums2[kk])))
                    print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1

                print("\npercent composition by quantity: ")
                h = 0
                j = 0
                k = 0
                longstrx = max(nums7, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                total_amt = sum(lists)
                while h < len(nums2):
                    monum = lists[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (monum / total_amt) * 100
                    len_long2x = (len_long1x - len(str(nums2[k])))
                    print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                    h += 1
                    j += 1
                    k += 1

                rr = 0
                tt = 0
                yy = 0
                print("\ndata percent represenation:")
                while rr < len(lists):
                    monum2 = round((lists[tt] * 100) / ncomp7)
                    monum3 = (lists[tt])
                    monum4 = ((lists[tt]) * 100) / ncomp7
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp7) * 100
                    len_long2x = (len_long1x - len(str(ncomp[yy])))
                    print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    rr += 1
                    tt += 1
                    yy += 1
            import random
            alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            rand_alpha = random.choice(alpha)
            print("\nEncrypted Message: ")
            vv = 0
            ans11 = []
            while vv < len(ans1):
                ans11.append(str(ans1[vv]) + str(random.choice(alpha)))
                vv += 1
            print(*ans11, sep=("."))
    elif mess_2lines and not code_2lines:
        while a < length_mess:
            split_code_length = len(list_code)
            new_mess_length1 = len(new_mess1)
            if split_code_length < new_mess_length1:
                list_code.insert(a + split_code_length, list_code[a])
                a += 1
            elif split_code_length > new_mess_length1:
                del (list_code[new_mess_length1:])
                a += 1
            else:
                ans1a = numpy.add(new_mess1, list_code)
                ans1b = numpy.add(new_mess2, list_code)
                ans1a = numpy.multiply(ans1a, list_code)
                ans1b = numpy.multiply(ans1b, list_code)
                ans1 = numpy.append(ans1a, ans1b)
                ans1_length = len(ans1) - 1
                a = length_mess
        else:
            if als == True:
                bibs_list = []
                sans2 = list(alsmess)
                entry = True
                t = 0
                while entry == True:
                    try:
                        if len(bibs_list) < len(sans2):
                            bib = str(sans2[t])
                            bibs_list.append(bib)
                            t += 1
                        else:
                            break
                    except:
                        print("\ninvalid entry\n")

                bibs_list.sort()
                print("\n\nDECRYPTED MESSAGE ANALYSIS")
                bibs2 = bibs_list
                bibs4 = []
                amt = []
                n = 0
                for x in bibs2:
                    while n < len(bibs2):
                        amt.append(bibs2.count(bibs2[n]))
                        try:
                            while bibs2[n] == bibs2[(n + 1)]:
                                del (bibs2[n])
                            else:
                                bibs4.append(bibs2[n])
                                n += 1
                        except:
                            bibs4.append(bibs2[n])
                            n += 1
                amt_tot = 0
                o = 0
                for l in amt:
                    while o < len(amt):
                        amt5 = int(amt[o])
                        amt_tot += amt5
                        o += 1
                ncomp = bibs_list

                z = 0
                c = 0
                y = 0
                nums9 = []
                p = 0
                while p < len(bibs4):
                    nums9.append(str(bibs4[p]))
                    p += 1
                longstry = max(nums9, key=len)
                len_longy = len(str(longstry))
                len_long1y = len_longy + 1
                while y < len(bibs4):
                    len_long2y = (len_long1y - len(str(bibs4[z])))
                    z += 1
                    c += 1
                    y += 1
                print("")

                len_nums = len(bibs_list)
                print("total number of entries = " + str(amt_tot))
                print("\nData Quantity Representation: ")
                h = 0
                j = 0
                k = 0
                bibs7 = []
                u = 0
                while u < len(bibs4):
                    bibs7.append(str(bibs4[u]))
                    u += 1
                total_amt = len_nums
                longstr = max(bibs7, key=len)
                len_long = len(longstr)
                len_long1 = len_long + 1
                while h < len(bibs4):
                    monum = amt[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (amt[j] / amt_tot) * 100
                    len_long2 = (len_long1 - len(bibs4[k]))
                    print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                    h += 1
                    j += 1
                    k += 1

                print("")
                hh = 0
                jj = 0
                kk = 0
                nums8 = []
                u = 0
                while u < len(bibs4):
                    nums8.append(str(bibs4[u]))
                    u += 1
                longstrx = max(nums8, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                print("Data Percent Represenation")
                while hh < len(amt):
                    monum2 = round((amt[jj] * 100) / amt_tot)
                    monum3 = (amt[jj])
                    monum4 = ((amt[jj]) * 100) / amt_tot
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / amt_tot) * 100
                    len_long2x = (len_long1x - len(str(bibs4[kk])))
                    print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1
            if als == True:
                sans1 = list(ans1)
                nums = []
                entry = 0
                while entry < len(sans1):
                    try:
                        number = int(sans1[entry])
                        nums.append(number)
                        entry += 1
                    except:
                        try:
                            number = float(number)
                            nums.append(number)
                            entry += 1
                        except:
                            print("\nnumbers only in list\n")

                nums.sort()
                print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                ncomp = nums
                ncomp2 = (sum(ncomp))

                n = 0
                nums3 = nums
                lists = []
                ncomp9 = nums
                ncomp7 = len(ncomp9)
                nums2 = []
                for x in nums3:
                    while n < len(nums3):
                        lists.append(nums3.count(nums3[n]))
                        try:
                            while nums3[n] == nums3[(n + 1)]:
                                del (nums3[n])
                            else:
                                nums2.append(nums3[n])
                                n += 1
                        except:
                            nums2.append(nums3[n])
                            n += 1

                tot_sum = sum(nums)
                len_nums = len(nums)
                mean = (tot_sum / len_nums)
                print("mean = " + str(mean))
                import statistics

                if int(len_nums) % 2 == 0:
                    len1 = (len_nums // 2)
                    len2 = ((len_nums // 2) + 1)
                    median1 = (nums[len1] + nums[len2]) / 2
                    median = statistics.median(nums)
                    print("median = " + str(median))
                else:
                    len1 = round((len_nums // 2) + 1)
                    median1 = nums[len1]
                    median = statistics.median(nums)
                    print("median = " + str(median))
                high_num = max(lists)
                index1 = lists.index(high_num)
                mode = nums2[index1]
                print("mode = " + str(mode))
                d = nums2[0]
                lenz2 = len(nums2) - 1
                f = nums2[lenz2]
                range = (f - d)
                print("range = " + str(range) + "; " + str([d, f]))

                hh = 0
                jj = 0
                kk = 0
                nums7 = []
                u = 0
                while u < len(nums2):
                    nums7.append(str(nums2[u]))
                    u += 1
                longstr = max(nums7, key=len)
                len_long = len(str(longstr))
                len_long1 = len_long + 1
                print("total sum = " + str(ncomp2))
                print("\npercent composition by value: ")
                while hh < len(nums2):
                    monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                    monum3 = (nums2[jj] * lists[jj])
                    monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp2) * 100
                    len_long2 = (len_long1 - len(str(nums2[kk])))
                    print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1

                print("\npercent composition by quantity: ")
                h = 0
                j = 0
                k = 0
                longstrx = max(nums7, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                total_amt = sum(lists)
                while h < len(nums2):
                    monum = lists[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (monum / total_amt) * 100
                    len_long2x = (len_long1x - len(str(nums2[k])))
                    print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                    h += 1
                    j += 1
                    k += 1

                rr = 0
                tt = 0
                yy = 0
                print("\ndata percent represenation:")
                while rr < len(lists):
                    monum2 = round((lists[tt] * 100) / ncomp7)
                    monum3 = (lists[tt])
                    monum4 = ((lists[tt]) * 100) / ncomp7
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp7) * 100
                    len_long2x = (len_long1x - len(str(ncomp[yy])))
                    print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    rr += 1
                    tt += 1
                    yy += 1
            import random
            alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            rand_alpha = random.choice(alpha)
            print("\nEncrypted Message: ")
            vv = 0
            ans11 = []
            while vv < len(ans1):
                ans11.append(str(ans1[vv]) + str(random.choice(alpha)))
                vv += 1
            print(*ans11, sep=("."))
    else:
        while a < length_mess:
            split_code_length = len(list_code)
            new_mess_length = len(new_mess)
            remove_splcode = int(len(list_code) - 1)
            if new_mess_length == 1:
                ans1a = numpy.add(new_mess, list_code[0])
                ans1 = numpy.multiply(ans1a, list_code[0])
                ans1_length = len(ans1) - 1
                a = length_mess
            elif split_code_length < new_mess_length:
                list_code.insert(a + split_code_length, list_code[a])
                a += 1
            elif split_code_length > new_mess_length:
                del (list_code[new_mess_length:])
                a += 1
            else:
                ans1a = numpy.add(new_mess, list_code)
                ans1 = numpy.multiply(ans1a, list_code)
                ans1_length = len(ans1) - 1
                a = length_mess
        else:
            if als == True:
                bibs_list = []
                sans2 = list(alsmess)
                entry = True
                t = 0
                while entry == True:
                    try:
                        if len(bibs_list) < len(sans2):
                            bib = str(sans2[t])
                            bibs_list.append(bib)
                            t += 1
                        else:
                            break
                    except:
                        print("\ninvalid entry\n")

                bibs_list.sort()
                print("\n\nDECRYPTED MESSAGE ANALYSIS")
                bibs2 = bibs_list
                bibs4 = []
                amt = []
                n = 0
                for x in bibs2:
                    while n < len(bibs2):
                        amt.append(bibs2.count(bibs2[n]))
                        try:
                            while bibs2[n] == bibs2[(n + 1)]:
                                del (bibs2[n])
                            else:
                                bibs4.append(bibs2[n])
                                n += 1
                        except:
                            bibs4.append(bibs2[n])
                            n += 1
                amt_tot = 0
                o = 0
                for l in amt:
                    while o < len(amt):
                        amt5 = int(amt[o])
                        amt_tot += amt5
                        o += 1
                ncomp = bibs_list

                z = 0
                c = 0
                y = 0
                nums9 = []
                p = 0
                while p < len(bibs4):
                    nums9.append(str(bibs4[p]))
                    p += 1
                longstry = max(nums9, key=len)
                len_longy = len(str(longstry))
                len_long1y = len_longy + 1
                while y < len(bibs4):
                    len_long2y = (len_long1y - len(str(bibs4[z])))
                    z += 1
                    c += 1
                    y += 1
                print("")

                len_nums = len(bibs_list)
                print("total number of entries = " + str(amt_tot))
                print("\nData Quantity Representation: ")
                h = 0
                j = 0
                k = 0
                bibs7 = []
                u = 0
                while u < len(bibs4):
                    bibs7.append(str(bibs4[u]))
                    u += 1
                total_amt = len_nums
                longstr = max(bibs7, key=len)
                len_long = len(longstr)
                len_long1 = len_long + 1
                while h < len(bibs4):
                    monum = amt[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (amt[j] / amt_tot) * 100
                    len_long2 = (len_long1 - len(bibs4[k]))
                    print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                    h += 1
                    j += 1
                    k += 1

                print("")
                hh = 0
                jj = 0
                kk = 0
                nums8 = []
                u = 0
                while u < len(bibs4):
                    nums8.append(str(bibs4[u]))
                    u += 1
                longstrx = max(nums8, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                print("Data Percent Represenation")
                while hh < len(amt):
                    monum2 = round((amt[jj] * 100) / amt_tot)
                    monum3 = (amt[jj])
                    monum4 = ((amt[jj]) * 100) / amt_tot
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / amt_tot) * 100
                    len_long2x = (len_long1x - len(str(bibs4[kk])))
                    print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1
            if als == True:
                sans1 = list(ans1)
                nums = []
                entry = 0
                while entry < len(sans1):
                    try:
                        number = int(sans1[entry])
                        nums.append(number)
                        entry += 1
                    except:
                        try:
                            number = float(number)
                            nums.append(number)
                            entry += 1
                        except:
                            print("\nnumbers only in list\n")

                nums.sort()
                print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                ncomp = nums
                ncomp2 = (sum(ncomp))

                n = 0
                nums3 = nums
                lists = []
                ncomp9 = nums
                ncomp7 = len(ncomp9)
                nums2 = []
                for x in nums3:
                    while n < len(nums3):
                        lists.append(nums3.count(nums3[n]))
                        try:
                            while nums3[n] == nums3[(n + 1)]:
                                del (nums3[n])
                            else:
                                nums2.append(nums3[n])
                                n += 1
                        except:
                            nums2.append(nums3[n])
                            n += 1

                tot_sum = sum(nums)
                len_nums = len(nums)
                mean = (tot_sum / len_nums)
                print("mean = " + str(mean))
                import statistics

                if int(len_nums) % 2 == 0:
                    len1 = (len_nums // 2)
                    len2 = ((len_nums // 2) + 1)
                    median1 = (nums[len1] + nums[len2]) / 2
                    median = statistics.median(nums)
                    print("median = " + str(median))
                else:
                    len1 = round((len_nums // 2) + 1)
                    median1 = nums[len1]
                    median = statistics.median(nums)
                    print("median = " + str(median))
                high_num = max(lists)
                index1 = lists.index(high_num)
                mode = nums2[index1]
                print("mode = " + str(mode))
                d = nums2[0]
                lenz2 = len(nums2) - 1
                f = nums2[lenz2]
                range = (f - d)
                print("range = " + str(range) + "; " + str([d, f]))

                hh = 0
                jj = 0
                kk = 0
                nums7 = []
                u = 0
                while u < len(nums2):
                    nums7.append(str(nums2[u]))
                    u += 1
                longstr = max(nums7, key=len)
                len_long = len(str(longstr))
                len_long1 = len_long + 1
                print("total sum = " + str(ncomp2))
                print("\npercent composition by value: ")
                while hh < len(nums2):
                    monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                    monum3 = (nums2[jj] * lists[jj])
                    monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp2) * 100
                    len_long2 = (len_long1 - len(str(nums2[kk])))
                    print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                    hh += 1
                    jj += 1
                    kk += 1

                print("\npercent composition by quantity: ")
                h = 0
                j = 0
                k = 0
                longstrx = max(nums7, key=len)
                len_longx = len(str(longstrx))
                len_long1x = len_longx + 1
                total_amt = sum(lists)
                while h < len(nums2):
                    monum = lists[j]
                    graph_len = "[]"
                    graph = monum * graph_len
                    percent = (monum / total_amt) * 100
                    len_long2x = (len_long1x - len(str(nums2[k])))
                    print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                    h += 1
                    j += 1
                    k += 1

                rr = 0
                tt = 0
                yy = 0
                print("\ndata percent represenation:")
                while rr < len(lists):
                    monum2 = round((lists[tt] * 100) / ncomp7)
                    monum3 = (lists[tt])
                    monum4 = ((lists[tt]) * 100) / ncomp7
                    if monum4 > 0 and monum4 < 1:
                        graph2 = "-"
                    else:
                        graph_len2 = "|"
                        graph2 = monum2 * graph_len2
                    percent2 = (monum3 / ncomp7) * 100
                    len_long2x = (len_long1x - len(str(ncomp[yy])))
                    print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                    rr += 1
                    tt += 1
                    yy += 1
            import random
            alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            rand_alpha = random.choice(alpha)
            print("\nEncrypted Message: ")
            vv = 0
            ans11 = []
            while vv < len(ans1):
                ans11.append(str(ans1[vv]) + str(random.choice(alpha)))
                vv += 1
            print(*ans11, sep=("."))


def decrypt(code2):
    code_to_mess = {
        1: " ",
        2: "a",
        3: "b",
        4: "c",
        5: "d",
        6: "e",
        7: "f",
        8: "g",
        9: "h",
        10: "i",
        11: "j",
        12: "k",
        13: "l",
        14: "m",
        15: "n",
        16: "o",
        17: "p",
        18: "q",
        19: "r",
        20: "s",
        21: "t",
        22: "u",
        23: "v",
        24: "w",
        25: "x",
        26: "y",
        27: "z",
        28: "A",
        29: "B",
        30: "C",
        31: "D",
        32: "E",
        33: "F",
        34: "G",
        35: "H",
        36: "I",
        37: "J",
        38: "K",
        39: "L",
        40: "M",
        41: "N",
        42: "O",
        43: "P",
        44: "Q",
        45: "R",
        46: "S",
        47: "T",
        48: "U",
        49: "V",
        50: "W",
        51: "X",
        52: "Y",
        53: "Z",
        54: ".",
        55: ",",
        56: "!",
        57: "?",
        58: "_",
        59: "\'",
        60: "\"",
        61: "/",
        62: "^",
        63: "$",
        64: "#",
        65: "@",
        66: "%",
        67: "&",
        68: "*",
        69: "(",
        70: ")",
        71: "{",
        72: "}",
        73: "[",
        74: "]",
        75: "\n",
        76: "\t",
        77: "\\",
        78: ":",
        79: ";",
        80: "<",
        81: ">",
        82: "=",
        83: "+",
        84: "-",
        85: "1",
        86: "2",
        87: "3",
        88: "4",
        89: "5",
        90: "6",
        91: "7",
        92: "8",
        93: "9",
        94: "0"
    }

    code2 = str(code2)
    length_code2 = len(code2)

    def split4(code2):
        return [char for char in code2]

    def split_list4(list_code2):
        half_split4 = length_code2 // 2
        return list_code2[:half_split4], list_code2[half_split4:]

    code_2lines2 = False
    if int(length_code2) % 2 == 0:
        list_code2 = split4(code2)
        list_code2 = list(map(int, list_code2))
        list_code2 = [int(k) for k in list_code2]
        split2_code_list1, split2_code_list2 = split_list4(list_code2)
        code_2lines2 = True
    else:
        list_code2 = array(split4(code2))
        list_code2 = list(map(int, list_code2))
        list_code2 = [int(k) for k in list_code2]
        code_2lines2 = False

    def input_to_list(encrypted_mess):
        encrypted_mess1 = list(encrypted_mess.split("."))
        return encrypted_mess1

    def encrypted_mess_islist(encrypted_mess_num):
        if isinstance(encrypted_mess_num, int):
            return True
        if isinstance(encrypted_mess_num, float):
            return encrypted_mess_num.is_integer()
        return False

    encrypted_mess = ()
    all_nums = False
    while all_nums == False:
        encrypted_mess = input("Enter Message You Would Like To Decrypt:\n")
        encrypted_mess1 = input_to_list(encrypted_mess)
        c = 0
        d = 0
        encrypted_mess_num = (encrypted_mess1[c])
        encryp_length1 = len(encrypted_mess1)
        bb = 0
        bbb = False
        while bb < encryp_length1:
            try:
                int(encrypted_mess1[bb])
                bbb = False
                bb += 1
            except:
                lle = len(str(encrypted_mess1[bb]))
                bbstr = str(encrypted_mess1[bb])
                bbb = True
            if bbb == True:
                try:
                    encrypted_mess1[bb] = bbstr[:-1]
                    int(encrypted_mess1[bb])
                    bb += 1
                except:
                    print("\nError: Encrypted Message Must Be Made Up Of Integers\n")
                    break
        try:
            all(type(int(f)) for f in encrypted_mess1)
            list_enc1 = map(int, encrypted_mess1)
            list_enc1 = [int(l) for l in list_enc1]
            list_enc1 = [abs(u) for u in list_enc1]
            break
        except ValueError:
            print("\nError: Encrypted Message Must Be Made Up Of Integers\n")

    def split_list(list_enc1):
        half_split = encryp_length1 // 2
        return list_enc1[:half_split], list_enc1[half_split:]

    enc_2lines = False
    if int(encryp_length1) % 2 == 0:
        split_enc1, split_enc2 = split_list(list_enc1)
        enc_2lines = True
    else:
        enc_2lines = False

    t = 0
    y = 0
    if code_2lines2 and enc_2lines:
        ans2 = []
        ans2a = []
        ans2ab = []
        ans2b = []
        ans2bb = []
        ans2_list = []
        ans2_length = len(ans2) - 1
        split2_code_length2 = len(split2_code_list1)
        split_enc1_length = len(split_enc1)
        trials2 = 1
        ans5 = []
        split_enc_length = len(split_enc1) + len(split_enc2)
        split2_code_length3 = len(split2_code_list1) + len(split2_code_list2)
    elif code_2lines2 and not enc_2lines:
        ans2 = []
        ans2a = []
        ans2ab = []
        ans2b = []
        ans2bb = []
        ans2_list = []
        ans2_length = len(ans2) - 1
        split2_code_length2 = len(split2_code_list1)
        split_enc1_length = len(list_enc1)
        trials2 = 1
        ans5 = []
        split2_code_length3 = len(split2_code_list1) + len(split2_code_list2)
    elif enc_2lines and not code_2lines2:
        ans2 = []
        ans2a = []
        ans2ab = []
        ans2b = []
        ans2bb = []
        ans2_list = []
        ans2_length = len(ans2) - 1
        split2_code_length2 = len(list_code2)
        split_enc1_length = len(split_enc1)
        trials2 = 1
        ans5 = []
        split_enc_length = len(split_enc1) + len(split_enc2)
    else:
        ans2 = []
        ans2a = []
        ans2ab = []
        ans2b = []
        ans2bb = []
        ans2_list = []
        ans2_length = len(ans2) - 1
        split2_code_length2 = len(list_code2)
        split_enc1_length = len(list_enc1)
        trials2 = 1
        ans5 = []
    if code_2lines2 and enc_2lines:
        try:
            while t < encryp_length1:
                split2_code_length2 = len(split2_code_list1)
                split_enc1_length = len(split_enc1)
                if split2_code_length2 < split_enc1_length:
                    split2_code_list1.insert(t + split2_code_length2, split2_code_list1[t])
                    split2_code_list2.insert(t + split2_code_length2, split2_code_list2[t])
                    t += 1
                elif split2_code_length2 > split_enc1_length:
                    del (split2_code_list1[split_enc1_length:])
                    del (split2_code_list2[split_enc1_length:])
                    t += 1
                else:
                    ans2a = numpy.floor_divide(split_enc1, split2_code_list1)
                    ans2b = numpy.floor_divide(split_enc2, split2_code_list2)
                    ans2a = numpy.subtract(ans2a, split2_code_list2)
                    ans2b = numpy.subtract(ans2b, split2_code_list1)
                    ans2 = numpy.append(ans2a, ans2b)
                    ans2_length = len(ans2)
                    t = encryp_length1
            else:
                trials2 = 1
                ans5 = []
                while trials2 <= ans2_length:
                    ans5.append(code_to_mess.get(ans2[trials2 - 1]))
                    trials2 += 1
                if als == True:
                    sans1 = list(list_enc1)
                    nums = []
                    entry = 0
                    while entry < len(sans1):
                        try:
                            number = int(sans1[entry])
                            nums.append(number)
                            entry += 1
                        except:
                            try:
                                number = float(number)
                                nums.append(number)
                                entry += 1
                            except:
                                print("\nnumbers only in list\n")

                    nums.sort()
                    print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                    ncomp = nums
                    ncomp2 = (sum(ncomp))

                    n = 0
                    nums3 = nums
                    lists = []
                    ncomp9 = nums
                    ncomp7 = len(ncomp9)
                    nums2 = []
                    for x in nums3:
                        while n < len(nums3):
                            lists.append(nums3.count(nums3[n]))
                            try:
                                while nums3[n] == nums3[(n + 1)]:
                                    del (nums3[n])
                                else:
                                    nums2.append(nums3[n])
                                    n += 1
                            except:
                                nums2.append(nums3[n])
                                n += 1

                    tot_sum = sum(nums)
                    len_nums = len(nums)
                    mean = (tot_sum / len_nums)
                    print("mean = " + str(mean))
                    import statistics

                    if int(len_nums) % 2 == 0:
                        len1 = (len_nums // 2)
                        len2 = ((len_nums // 2) + 1)
                        median1 = (nums[len1] + nums[len2]) / 2
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    else:
                        len1 = round((len_nums // 2) + 1)
                        median1 = nums[len1]
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    high_num = max(lists)
                    index1 = lists.index(high_num)
                    mode = nums2[index1]
                    print("mode = " + str(mode))
                    d = nums2[0]
                    lenz2 = len(nums2) - 1
                    f = nums2[lenz2]
                    range = (f - d)
                    print("range = " + str(range) + "; " + str([d, f]))

                    hh = 0
                    jj = 0
                    kk = 0
                    nums7 = []
                    u = 0
                    while u < len(nums2):
                        nums7.append(str(nums2[u]))
                        u += 1
                    longstr = max(nums7, key=len)
                    len_long = len(str(longstr))
                    len_long1 = len_long + 1
                    print("total sum = " + str(ncomp2))
                    print("\npercent composition by value: ")
                    while hh < len(nums2):
                        monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                        monum3 = (nums2[jj] * lists[jj])
                        monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp2) * 100
                        len_long2 = (len_long1 - len(str(nums2[kk])))
                        print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1

                    print("\npercent composition by quantity: ")
                    h = 0
                    j = 0
                    k = 0
                    longstrx = max(nums7, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    total_amt = sum(lists)
                    while h < len(nums2):
                        monum = lists[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (monum / total_amt) * 100
                        len_long2x = (len_long1x - len(str(nums2[k])))
                        print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                        h += 1
                        j += 1
                        k += 1

                    rr = 0
                    tt = 0
                    yy = 0
                    print("\ndata percent represenation:")
                    while rr < len(lists):
                        monum2 = round((lists[tt] * 100) / ncomp7)
                        monum3 = (lists[tt])
                        monum4 = ((lists[tt]) * 100) / ncomp7
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp7) * 100
                        len_long2x = (len_long1x - len(str(ncomp[yy])))
                        print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        rr += 1
                        tt += 1
                        yy += 1
                if als == True:
                    print("\n\nDECRYPTED MESSAGE ANALYSIS")
                    bibs_list = []
                    sans2 = list(ans5)
                    entry = True
                    t = 0
                    while entry == True:
                        try:
                            if len(bibs_list) < len(sans2):
                                bib = str(sans2[t])
                                bibs_list.append(bib)
                                t += 1
                            else:
                                break
                        except:
                            print("\ninvalid entry\n")

                    bibs_list.sort()
                    bibs2 = bibs_list
                    bibs4 = []
                    amt = []
                    n = 0
                    for x in bibs2:
                        while n < len(bibs2):
                            amt.append(bibs2.count(bibs2[n]))
                            try:
                                while bibs2[n] == bibs2[(n + 1)]:
                                    del (bibs2[n])
                                else:
                                    bibs4.append(bibs2[n])
                                    n += 1
                            except:
                                bibs4.append(bibs2[n])
                                n += 1
                    amt_tot = 0
                    o = 0
                    for l in amt:
                        while o < len(amt):
                            amt5 = int(amt[o])
                            amt_tot += amt5
                            o += 1
                    ncomp = bibs_list

                    z = 0
                    c = 0
                    y = 0
                    nums9 = []
                    p = 0
                    while p < len(bibs4):
                        nums9.append(str(bibs4[p]))
                        p += 1
                    longstry = max(nums9, key=len)
                    len_longy = len(str(longstry))
                    len_long1y = len_longy + 1
                    while y < len(bibs4):
                        len_long2y = (len_long1y - len(str(bibs4[z])))
                        z += 1
                        c += 1
                        y += 1
                    print("")

                    len_nums = len(bibs_list)
                    print("total number of entries = " + str(amt_tot))
                    print("\nData Quantity Representation: ")
                    h = 0
                    j = 0
                    k = 0
                    bibs7 = []
                    u = 0
                    while u < len(bibs4):
                        bibs7.append(str(bibs4[u]))
                        u += 1
                    total_amt = len_nums
                    longstr = max(bibs7, key=len)
                    len_long = len(longstr)
                    len_long1 = len_long + 1
                    while h < len(bibs4):
                        monum = amt[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (amt[j] / amt_tot) * 100
                        len_long2 = (len_long1 - len(bibs4[k]))
                        print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                        h += 1
                        j += 1
                        k += 1

                    print("")
                    hh = 0
                    jj = 0
                    kk = 0
                    nums8 = []
                    u = 0
                    while u < len(bibs4):
                        nums8.append(str(bibs4[u]))
                        u += 1
                    longstrx = max(nums8, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    print("Data Percent Represenation")
                    while hh < len(amt):
                        monum2 = round((amt[jj] * 100) / amt_tot)
                        monum3 = (amt[jj])
                        monum4 = ((amt[jj]) * 100) / amt_tot
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / amt_tot) * 100
                        len_long2x = (len_long1x - len(str(bibs4[kk])))
                        print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1
                print("\nDecrypted Message: ")
                print("".join(ans5))
        except:
            print("Decryption Error, Invalid Input")
    elif code_2lines2 and not enc_2lines:
        try:
            while t < split_enc1_length:
                split2_code_length1 = len(split2_code_list1)
                split_enc1_length = len(list_enc1)
                if split_enc1_length == 1:
                    ans2a = numpy.floor_divide(list_enc1, split2_code_list1[0])
                    ans2 = numpy.subtract(ans2a, split2_code_list2[0])
                    ans2_length = len(ans2)
                    t = split_enc1_length
                elif split2_code_length1 < split_enc1_length:
                    split2_code_list1.insert(t + split2_code_length1, split2_code_list1[t])
                    split2_code_list2.insert(t + split2_code_length1, split2_code_list2[t])
                    t += 1
                elif split2_code_length1 > split_enc1_length:
                    del (split2_code_list1[split_enc1_length:])
                    del (split2_code_list2[split_enc1_length:])
                    t += 1
                else:
                    ans2a = numpy.floor_divide(list_enc1, split2_code_list1)
                    ans2 = numpy.subtract(ans2a, split2_code_list2)
                    ans2_length = len(ans2)
                    t = split_enc1_length
            else:
                trials2 = 1
                ans5 = []
                while trials2 <= ans2_length:
                    ans5.append(code_to_mess.get(ans2[trials2 - 1]))
                    trials2 += 1
                if als == True:
                    sans1 = list(list_enc1)
                    nums = []
                    entry = 0
                    while entry < len(sans1):
                        try:
                            number = int(sans1[entry])
                            nums.append(number)
                            entry += 1
                        except:
                            try:
                                number = float(number)
                                nums.append(number)
                                entry += 1
                            except:
                                print("\nnumbers only in list\n")

                    nums.sort()
                    print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                    ncomp = nums
                    ncomp2 = (sum(ncomp))

                    n = 0
                    nums3 = nums
                    lists = []
                    ncomp9 = nums
                    ncomp7 = len(ncomp9)
                    nums2 = []
                    for x in nums3:
                        while n < len(nums3):
                            lists.append(nums3.count(nums3[n]))
                            try:
                                while nums3[n] == nums3[(n + 1)]:
                                    del (nums3[n])
                                else:
                                    nums2.append(nums3[n])
                                    n += 1
                            except:
                                nums2.append(nums3[n])
                                n += 1

                    tot_sum = sum(nums)
                    len_nums = len(nums)
                    mean = (tot_sum / len_nums)
                    print("mean = " + str(mean))
                    import statistics

                    if int(len_nums) % 2 == 0:
                        len1 = (len_nums // 2)
                        len2 = ((len_nums // 2) + 1)
                        median1 = (nums[len1] + nums[len2]) / 2
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    else:
                        len1 = round((len_nums // 2) + 1)
                        median1 = nums[len1]
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    high_num = max(lists)
                    index1 = lists.index(high_num)
                    mode = nums2[index1]
                    print("mode = " + str(mode))
                    d = nums2[0]
                    lenz2 = len(nums2) - 1
                    f = nums2[lenz2]
                    range = (f - d)
                    print("range = " + str(range) + "; " + str([d, f]))

                    hh = 0
                    jj = 0
                    kk = 0
                    nums7 = []
                    u = 0
                    while u < len(nums2):
                        nums7.append(str(nums2[u]))
                        u += 1
                    longstr = max(nums7, key=len)
                    len_long = len(str(longstr))
                    len_long1 = len_long + 1
                    print("total sum = " + str(ncomp2))
                    print("\npercent composition by value: ")
                    while hh < len(nums2):
                        monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                        monum3 = (nums2[jj] * lists[jj])
                        monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp2) * 100
                        len_long2 = (len_long1 - len(str(nums2[kk])))
                        print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1

                    print("\npercent composition by quantity: ")
                    h = 0
                    j = 0
                    k = 0
                    longstrx = max(nums7, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    total_amt = sum(lists)
                    while h < len(nums2):
                        monum = lists[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (monum / total_amt) * 100
                        len_long2x = (len_long1x - len(str(nums2[k])))
                        print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                        h += 1
                        j += 1
                        k += 1

                    rr = 0
                    tt = 0
                    yy = 0
                    print("\ndata percent represenation:")
                    while rr < len(lists):
                        monum2 = round((lists[tt] * 100) / ncomp7)
                        monum3 = (lists[tt])
                        monum4 = ((lists[tt]) * 100) / ncomp7
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp7) * 100
                        len_long2x = (len_long1x - len(str(ncomp[yy])))
                        print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        rr += 1
                        tt += 1
                        yy += 1
                if als == True:
                    print("\n\nDECRYPTED MESSAGE ANALYSIS")
                    bibs_list = []
                    sans2 = list(ans5)
                    entry = True
                    t = 0
                    while entry == True:
                        try:
                            if len(bibs_list) < len(sans2):
                                bib = str(sans2[t])
                                bibs_list.append(bib)
                                t += 1
                            else:
                                break
                        except:
                            print("\ninvalid entry\n")

                    bibs_list.sort()
                    bibs2 = bibs_list
                    bibs4 = []
                    amt = []
                    n = 0
                    for x in bibs2:
                        while n < len(bibs2):
                            amt.append(bibs2.count(bibs2[n]))
                            try:
                                while bibs2[n] == bibs2[(n + 1)]:
                                    del (bibs2[n])
                                else:
                                    bibs4.append(bibs2[n])
                                    n += 1
                            except:
                                bibs4.append(bibs2[n])
                                n += 1
                    amt_tot = 0
                    o = 0
                    for l in amt:
                        while o < len(amt):
                            amt5 = int(amt[o])
                            amt_tot += amt5
                            o += 1
                    ncomp = bibs_list

                    z = 0
                    c = 0
                    y = 0
                    nums9 = []
                    p = 0
                    while p < len(bibs4):
                        nums9.append(str(bibs4[p]))
                        p += 1
                    longstry = max(nums9, key=len)
                    len_longy = len(str(longstry))
                    len_long1y = len_longy + 1
                    while y < len(bibs4):
                        len_long2y = (len_long1y - len(str(bibs4[z])))
                        z += 1
                        c += 1
                        y += 1
                    print("")

                    len_nums = len(bibs_list)
                    print("total number of entries = " + str(amt_tot))
                    print("\nData Quantity Representation: ")
                    h = 0
                    j = 0
                    k = 0
                    bibs7 = []
                    u = 0
                    while u < len(bibs4):
                        bibs7.append(str(bibs4[u]))
                        u += 1
                    total_amt = len_nums
                    longstr = max(bibs7, key=len)
                    len_long = len(longstr)
                    len_long1 = len_long + 1
                    while h < len(bibs4):
                        monum = amt[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (amt[j] / amt_tot) * 100
                        len_long2 = (len_long1 - len(bibs4[k]))
                        print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                        h += 1
                        j += 1
                        k += 1

                    print("")
                    hh = 0
                    jj = 0
                    kk = 0
                    nums8 = []
                    u = 0
                    while u < len(bibs4):
                        nums8.append(str(bibs4[u]))
                        u += 1
                    longstrx = max(nums8, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    print("Data Percent Represenation")
                    while hh < len(amt):
                        monum2 = round((amt[jj] * 100) / amt_tot)
                        monum3 = (amt[jj])
                        monum4 = ((amt[jj]) * 100) / amt_tot
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / amt_tot) * 100
                        len_long2x = (len_long1x - len(str(bibs4[kk])))
                        print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1
                print("\nDecrypted Message: ")
                print("".join(ans5))
        except:
            print("Decryption Error, Invalid Input")
    elif enc_2lines and not code_2lines2:
        try:
            while t < split_enc1_length:
                split2_code_length = len(list_code2)
                split_enc1_length = len(split_enc1)
                if split2_code_length < split_enc1_length:
                    list_code2.insert(t + split2_code_length, list_code2[t])
                    t += 1
                elif split2_code_length > split_enc1_length:
                    del (list_code2[split_enc1_length:])
                    t += 1
                else:
                    ans2a = numpy.floor_divide(split_enc1, list_code2)
                    ans2b = numpy.floor_divide(split_enc2, list_code2)
                    ans2a = numpy.subtract(ans2a, list_code2)
                    ans2b = numpy.subtract(ans2b, list_code2)
                    ans2 = numpy.append(ans2a, ans2b)
                    ans2_length = len(ans2)
                    t = split_enc1_length
            else:
                trials2 = 1
                ans5 = []
                while trials2 <= ans2_length:
                    ans5.append(code_to_mess.get(ans2[trials2 - 1]))
                    trials2 += 1
                if als == True:
                    sans1 = list(list_enc1)
                    nums = []
                    entry = 0
                    while entry < len(sans1):
                        try:
                            number = int(sans1[entry])
                            nums.append(number)
                            entry += 1
                        except:
                            try:
                                number = float(number)
                                nums.append(number)
                                entry += 1
                            except:
                                print("\nnumbers only in list\n")

                    nums.sort()
                    print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                    ncomp = nums
                    ncomp2 = (sum(ncomp))

                    n = 0
                    nums3 = nums
                    lists = []
                    ncomp9 = nums
                    ncomp7 = len(ncomp9)
                    nums2 = []
                    for x in nums3:
                        while n < len(nums3):
                            lists.append(nums3.count(nums3[n]))
                            try:
                                while nums3[n] == nums3[(n + 1)]:
                                    del (nums3[n])
                                else:
                                    nums2.append(nums3[n])
                                    n += 1
                            except:
                                nums2.append(nums3[n])
                                n += 1

                    tot_sum = sum(nums)
                    len_nums = len(nums)
                    mean = (tot_sum / len_nums)
                    print("mean = " + str(mean))
                    import statistics

                    if int(len_nums) % 2 == 0:
                        len1 = (len_nums // 2)
                        len2 = ((len_nums // 2) + 1)
                        median1 = (nums[len1] + nums[len2]) / 2
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    else:
                        len1 = round((len_nums // 2) + 1)
                        median1 = nums[len1]
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    high_num = max(lists)
                    index1 = lists.index(high_num)
                    mode = nums2[index1]
                    print("mode = " + str(mode))
                    d = nums2[0]
                    lenz2 = len(nums2) - 1
                    f = nums2[lenz2]
                    range = (f - d)
                    print("range = " + str(range) + "; " + str([d, f]))

                    hh = 0
                    jj = 0
                    kk = 0
                    nums7 = []
                    u = 0
                    while u < len(nums2):
                        nums7.append(str(nums2[u]))
                        u += 1
                    longstr = max(nums7, key=len)
                    len_long = len(str(longstr))
                    len_long1 = len_long + 1
                    print("total sum = " + str(ncomp2))
                    print("\npercent composition by value: ")
                    while hh < len(nums2):
                        monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                        monum3 = (nums2[jj] * lists[jj])
                        monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp2) * 100
                        len_long2 = (len_long1 - len(str(nums2[kk])))
                        print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1

                    print("\npercent composition by quantity: ")
                    h = 0
                    j = 0
                    k = 0
                    longstrx = max(nums7, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    total_amt = sum(lists)
                    while h < len(nums2):
                        monum = lists[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (monum / total_amt) * 100
                        len_long2x = (len_long1x - len(str(nums2[k])))
                        print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                        h += 1
                        j += 1
                        k += 1

                    rr = 0
                    tt = 0
                    yy = 0
                    print("\ndata percent represenation:")
                    while rr < len(lists):
                        monum2 = round((lists[tt] * 100) / ncomp7)
                        monum3 = (lists[tt])
                        monum4 = ((lists[tt]) * 100) / ncomp7
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp7) * 100
                        len_long2x = (len_long1x - len(str(ncomp[yy])))
                        print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        rr += 1
                        tt += 1
                        yy += 1
                if als == True:
                    print("\n\nDECRYPTED MESSAGE ANALYSIS")
                    bibs_list = []
                    sans2 = list(ans5)
                    entry = True
                    t = 0
                    while entry == True:
                        try:
                            if len(bibs_list) < len(sans2):
                                bib = str(sans2[t])
                                bibs_list.append(bib)
                                t += 1
                            else:
                                break
                        except:
                            print("\ninvalid entry\n")

                    bibs_list.sort()
                    bibs2 = bibs_list
                    bibs4 = []
                    amt = []
                    n = 0
                    for x in bibs2:
                        while n < len(bibs2):
                            amt.append(bibs2.count(bibs2[n]))
                            try:
                                while bibs2[n] == bibs2[(n + 1)]:
                                    del (bibs2[n])
                                else:
                                    bibs4.append(bibs2[n])
                                    n += 1
                            except:
                                bibs4.append(bibs2[n])
                                n += 1
                    amt_tot = 0
                    o = 0
                    for l in amt:
                        while o < len(amt):
                            amt5 = int(amt[o])
                            amt_tot += amt5
                            o += 1
                    ncomp = bibs_list

                    z = 0
                    c = 0
                    y = 0
                    nums9 = []
                    p = 0
                    while p < len(bibs4):
                        nums9.append(str(bibs4[p]))
                        p += 1
                    longstry = max(nums9, key=len)
                    len_longy = len(str(longstry))
                    len_long1y = len_longy + 1
                    while y < len(bibs4):
                        len_long2y = (len_long1y - len(str(bibs4[z])))
                        z += 1
                        c += 1
                        y += 1
                    print("")

                    len_nums = len(bibs_list)
                    print("total number of entries = " + str(amt_tot))
                    print("\nData Quantity Representation: ")
                    h = 0
                    j = 0
                    k = 0
                    bibs7 = []
                    u = 0
                    while u < len(bibs4):
                        bibs7.append(str(bibs4[u]))
                        u += 1
                    total_amt = len_nums
                    longstr = max(bibs7, key=len)
                    len_long = len(longstr)
                    len_long1 = len_long + 1
                    while h < len(bibs4):
                        monum = amt[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (amt[j] / amt_tot) * 100
                        len_long2 = (len_long1 - len(bibs4[k]))
                        print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                        h += 1
                        j += 1
                        k += 1

                    print("")
                    hh = 0
                    jj = 0
                    kk = 0
                    nums8 = []
                    u = 0
                    while u < len(bibs4):
                        nums8.append(str(bibs4[u]))
                        u += 1
                    longstrx = max(nums8, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    print("Data Percent Represenation")
                    while hh < len(amt):
                        monum2 = round((amt[jj] * 100) / amt_tot)
                        monum3 = (amt[jj])
                        monum4 = ((amt[jj]) * 100) / amt_tot
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / amt_tot) * 100
                        len_long2x = (len_long1x - len(str(bibs4[kk])))
                        print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1
                print("\nDecrypted Message: ")
                print("".join(ans5))
        except:
            print("Decryption Error, Invalid Input")
    else:
        try:
            while t < split_enc1_length:
                split2_code_length = len(list_code2)
                split_enc1_length = len(list_enc1)
                remove_splcode = int(len(list_code2) - 1)
                if split_enc1_length == 1:
                    ans2a = numpy.floor_divide(list_enc1, list_code2[0])
                    ans2 = numpy.subtract(ans2a, list_code2[0])
                    ans2_length = len(ans2)
                    t = split_enc1_length
                elif split2_code_length < split_enc1_length:
                    list_code2.insert(t + split2_code_length, list_code2[t])
                    t += 1
                elif split2_code_length > split_enc1_length:
                    del (list_code2[split_enc1_length:])
                    t += 1
                else:
                    ans2a = numpy.floor_divide(list_enc1, list_code2)
                    ans2 = numpy.subtract(ans2a, list_code2)
                    ans2_length = len(ans2)
                    t = split_enc1_length
            else:
                trials2 = 1
                ans5 = []
                while trials2 <= ans2_length:
                    ans5.append(code_to_mess.get(ans2[trials2 - 1]))
                    trials2 += 1
                if als == True:
                    sans1 = list(list_enc1)
                    nums = []
                    entry = 0
                    while entry < len(sans1):
                        try:
                            number = int(sans1[entry])
                            nums.append(number)
                            entry += 1
                        except:
                            try:
                                number = float(number)
                                nums.append(number)
                                entry += 1
                            except:
                                print("\nnumbers only in list\n")

                    nums.sort()
                    print("\n\nENCRYPTED MESSAGE ANALYSIS\n")
                    ncomp = nums
                    ncomp2 = (sum(ncomp))

                    n = 0
                    nums3 = nums
                    lists = []
                    ncomp9 = nums
                    ncomp7 = len(ncomp9)
                    nums2 = []
                    for x in nums3:
                        while n < len(nums3):
                            lists.append(nums3.count(nums3[n]))
                            try:
                                while nums3[n] == nums3[(n + 1)]:
                                    del (nums3[n])
                                else:
                                    nums2.append(nums3[n])
                                    n += 1
                            except:
                                nums2.append(nums3[n])
                                n += 1

                    tot_sum = sum(nums)
                    len_nums = len(nums)
                    mean = (tot_sum / len_nums)
                    print("mean = " + str(mean))
                    import statistics

                    if int(len_nums) % 2 == 0:
                        len1 = (len_nums // 2)
                        len2 = ((len_nums // 2) + 1)
                        median1 = (nums[len1] + nums[len2]) / 2
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    else:
                        len1 = round((len_nums // 2) + 1)
                        median1 = nums[len1]
                        median = statistics.median(nums)
                        print("median = " + str(median))
                    high_num = max(lists)
                    index1 = lists.index(high_num)
                    mode = nums2[index1]
                    print("mode = " + str(mode))
                    d = nums2[0]
                    lenz2 = len(nums2) - 1
                    f = nums2[lenz2]
                    range = (f - d)
                    print("range = " + str(range) + "; " + str([d, f]))

                    hh = 0
                    jj = 0
                    kk = 0
                    nums7 = []
                    u = 0
                    while u < len(nums2):
                        nums7.append(str(nums2[u]))
                        u += 1
                    longstr = max(nums7, key=len)
                    len_long = len(str(longstr))
                    len_long1 = len_long + 1
                    print("total sum = " + str(ncomp2))
                    print("\npercent composition by value: ")
                    while hh < len(nums2):
                        monum2 = round(((nums2[jj] * lists[jj]) * 100) / ncomp2)
                        monum3 = (nums2[jj] * lists[jj])
                        monum4 = ((nums2[jj] * lists[jj]) * 100) / ncomp2
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp2) * 100
                        len_long2 = (len_long1 - len(str(nums2[kk])))
                        print(str(nums2[kk]) + (" ") * len_long2 + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1

                    print("\npercent composition by quantity: ")
                    h = 0
                    j = 0
                    k = 0
                    longstrx = max(nums7, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    total_amt = sum(lists)
                    while h < len(nums2):
                        monum = lists[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (monum / total_amt) * 100
                        len_long2x = (len_long1x - len(str(nums2[k])))
                        print(str(nums2[k]) + (" ") * len_long2x + str(graph) + "  " + str(percent) + "%")
                        h += 1
                        j += 1
                        k += 1

                    rr = 0
                    tt = 0
                    yy = 0
                    print("\ndata percent represenation:")
                    while rr < len(lists):
                        monum2 = round((lists[tt] * 100) / ncomp7)
                        monum3 = (lists[tt])
                        monum4 = ((lists[tt]) * 100) / ncomp7
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / ncomp7) * 100
                        len_long2x = (len_long1x - len(str(ncomp[yy])))
                        print(str(ncomp[yy]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        rr += 1
                        tt += 1
                        yy += 1
                if als == True:
                    print("\n\nDECRYPTED MESSAGE ANALYSIS")
                    bibs_list = []
                    sans2 = list(ans5)
                    entry = True
                    t = 0
                    while entry == True:
                        try:
                            if len(bibs_list) < len(sans2):
                                bib = str(sans2[t])
                                bibs_list.append(bib)
                                t += 1
                            else:
                                break
                        except:
                            print("\ninvalid entry\n")

                    bibs_list.sort()
                    bibs2 = bibs_list
                    bibs4 = []
                    amt = []
                    n = 0
                    for x in bibs2:
                        while n < len(bibs2):
                            amt.append(bibs2.count(bibs2[n]))
                            try:
                                while bibs2[n] == bibs2[(n + 1)]:
                                    del (bibs2[n])
                                else:
                                    bibs4.append(bibs2[n])
                                    n += 1
                            except:
                                bibs4.append(bibs2[n])
                                n += 1
                    amt_tot = 0
                    o = 0
                    for l in amt:
                        while o < len(amt):
                            amt5 = int(amt[o])
                            amt_tot += amt5
                            o += 1
                    ncomp = bibs_list

                    z = 0
                    c = 0
                    y = 0
                    nums9 = []
                    p = 0
                    while p < len(bibs4):
                        nums9.append(str(bibs4[p]))
                        p += 1
                    longstry = max(nums9, key=len)
                    len_longy = len(str(longstry))
                    len_long1y = len_longy + 1
                    while y < len(bibs4):
                        len_long2y = (len_long1y - len(str(bibs4[z])))
                        z += 1
                        c += 1
                        y += 1
                    print("")

                    len_nums = len(bibs_list)
                    print("total number of entries = " + str(amt_tot))
                    print("\nData Quantity Representation: ")
                    h = 0
                    j = 0
                    k = 0
                    bibs7 = []
                    u = 0
                    while u < len(bibs4):
                        bibs7.append(str(bibs4[u]))
                        u += 1
                    total_amt = len_nums
                    longstr = max(bibs7, key=len)
                    len_long = len(longstr)
                    len_long1 = len_long + 1
                    while h < len(bibs4):
                        monum = amt[j]
                        graph_len = "[]"
                        graph = monum * graph_len
                        percent = (amt[j] / amt_tot) * 100
                        len_long2 = (len_long1 - len(bibs4[k]))
                        print(str(bibs4[k]) + (" ") * len_long2 + str(graph))
                        h += 1
                        j += 1
                        k += 1

                    print("")
                    hh = 0
                    jj = 0
                    kk = 0
                    nums8 = []
                    u = 0
                    while u < len(bibs4):
                        nums8.append(str(bibs4[u]))
                        u += 1
                    longstrx = max(nums8, key=len)
                    len_longx = len(str(longstrx))
                    len_long1x = len_longx + 1
                    print("Data Percent Represenation")
                    while hh < len(amt):
                        monum2 = round((amt[jj] * 100) / amt_tot)
                        monum3 = (amt[jj])
                        monum4 = ((amt[jj]) * 100) / amt_tot
                        if monum4 > 0 and monum4 < 1:
                            graph2 = "-"
                        else:
                            graph_len2 = "|"
                            graph2 = monum2 * graph_len2
                        percent2 = (monum3 / amt_tot) * 100
                        len_long2x = (len_long1x - len(str(bibs4[kk])))
                        print(str(bibs4[kk]) + (" ") * len_long2x + str(graph2) + "  " + str(percent2) + "%")
                        hh += 1
                        jj += 1
                        kk += 1
                print("\nDecrypted Message: ")
                print("".join(ans5))
        except:
            print("Decryption Error, Invalid Input")

def BlackJack():
    import time
    import random

    Win = 0
    Loss = 0
    Tie = 0
    numplay = "0"

    def house_rules():
        Win1 = False
        Loss1 = False
        Tie1 = False
        shuffle = True
        if shuffle == True:
            deck = {
                1: "Ace of Spades",
                2: "2 of Spades",
                3: "3 of Spades",
                4: "4 of Spades",
                5: "5 of Spades",
                6: "6 of Spades",
                7: "7 of Spades",
                8: "8 of Spades",
                9: "9 of Spades",
                10: "10 of Spades",
                11: "Jack of Spades",
                12: "Queen of Spades",
                13: "King of Spades",
                14: "Ace of Hearts",
                15: "2 of Hearts",
                16: "3 of Hearts",
                17: "4 of Hearts",
                18: "5 of Hearts",
                19: "6 of Hearts",
                20: "7 of Hearts",
                21: "8 of Hearts",
                22: "9 of Hearts",
                23: "10 of Hearts",
                24: "Jack of Hearts",
                25: "Queen of Hearts",
                26: "King of Hearts",
                27: "Ace of Diamonds",
                28: "2 of Diamonds",
                29: "3 of Diamonds",
                30: "4 of Diamonds",
                31: "5 of Diamonds",
                32: "6 of Diamonds",
                33: "7 of Diamonds",
                34: "8 of Diamonds",
                35: "9 of Diamonds",
                36: "10 of Diamonds",
                37: "Jack of Diamonds",
                38: "Queen of Diamonds",
                39: "King of Diamonds",
                40: "Ace of Clubs",
                41: "2 of Clubs",
                42: "3 of Clubs",
                43: "4 of Clubs",
                44: "5 of Clubs",
                45: "6 of Clubs",
                46: "7 of Clubs",
                47: "8 of Clubs",
                48: "9 of Clubs",
                49: "10 of Clubs",
                50: "Jack of Clubs",
                51: "Queen of Clubs",
                52: "King of Clubs"
            }
            card_value = {
                "2 of Spades": 2,
                "3 of Spades": 3,
                "4 of Spades": 4,
                "5 of Spades": 5,
                "6 of Spades": 6,
                "7 of Spades": 7,
                "8 of Spades": 8,
                "9 of Spades": 9,
                "10 of Spades": 10,
                "Jack of Spades": 10,
                "Queen of Spades": 10,
                "King of Spades": 10,
                "2 of Hearts": 2,
                "3 of Hearts": 3,
                "4 of Hearts": 4,
                "5 of Hearts": 5,
                "6 of Hearts": 6,
                "7 of Hearts": 7,
                "8 of Hearts": 8,
                "9 of Hearts": 9,
                "10 of Hearts": 10,
                "Jack of Hearts": 10,
                "Queen of Hearts": 10,
                "King of Hearts": 10,
                "2 of Diamonds": 2,
                "3 of Diamonds": 3,
                "4 of Diamonds": 4,
                "5 of Diamonds": 5,
                "6 of Diamonds": 6,
                "7 of Diamonds": 7,
                "8 of Diamonds": 8,
                "9 of Diamonds": 9,
                "10 of Diamonds": 10,
                "Jack of Diamonds": 10,
                "Queen of Diamonds": 10,
                "King of Diamonds": 10,
                "2 of Clubs": 2,
                "3 of Clubs": 3,
                "4 of Clubs": 4,
                "5 of Clubs": 5,
                "6 of Clubs": 6,
                "7 of Clubs": 7,
                "8 of Clubs": 8,
                "9 of Clubs": 9,
                "10 of Clubs": 10,
                "Jack of Clubs": 10,
                "Queen of Clubs": 10,
                "King of Clubs": 10
            }
            Bust3 = False
            cards = []
            cards.append(random.randint(1, 52))
            cards.append(random.randint(1, 52))
            a = 0
            card1 = cards[a]
            card2 = cards[a + 1]
            while a < len(cards):
                if card1 == card2:
                    del (cards[a])
                    cards.append(random.randint(1, 52))
                else:
                    a += 1

            b = 0
            print("\nyour cards are the " + deck.get(cards[b]) + " and the " + deck.get(cards[b + 1]))
            print("")

            cardname1 = deck.get(cards[b])
            cardname2 = deck.get(cards[b + 1])
            card_val1 = card_value.get(cardname1)
            card_val2 = card_value.get(cardname2)

            total = 0
            while total <= 21:
                if str(card1) == "1":
                    if str(card2) == "14":
                        total = 12
                        break
                    elif str(card2) == "27":
                        total = 12
                        break
                    elif str(card2) == "40":
                        total = 12
                        break
                    else:
                        card_val1 = 11
                        total = int(card_val1 + card_val2)
                        break
                elif str(card1) == "14":
                    if str(card2) == "1":
                        total = 12
                        break
                    elif str(card2) == "27":
                        total = 12
                        break
                    elif str(card2) == "40":
                        total = 12
                        break
                    else:
                        card_val1 = 11
                        total = int(card_val1 + card_val2)
                        break
                elif str(card1) == "27":
                    if str(card2) == "1":
                        total = 12
                        break
                    elif str(card2) == "14":
                        total = 12
                        break
                    elif str(card2) == "40":
                        total = 12
                        break
                    else:
                        card_val1 = 11
                        total = int(card_val1 + card_val2)
                        break
                elif str(card1) == "40":
                    if str(card2) == "1":
                        total = 12
                        break
                    elif str(card2) == "14":
                        total = 12
                        break
                    elif str(card2) == "27":
                        total = 12
                        break
                    else:
                        card_val1 = 11
                        total = int(card_val1 + card_val2)
                        break
                elif str(card2) == "1":
                    if str(card1) == "14":
                        total = 12
                        break
                    elif str(card1) == "27":
                        total = 12
                        break
                    elif str(card1) == "40":
                        total = 12
                        break
                    else:
                        card_val2 = 11
                        total = int(card_val1 + card_val2)
                        break
                elif str(card2) == "14":
                    if str(card1) == "1":
                        total = 12
                        break
                    elif str(card1) == "27":
                        total = 12
                        break
                    elif str(card1) == "40":
                        total = 12
                        break
                    else:
                        card_val2 = 11
                        total = int(card_val1 + card_val2)
                        break
                elif str(card2) == "27":
                    if str(card1) == "1":
                        total = 12
                        break
                    elif str(card1) == "14":
                        total = 12
                        break
                    elif str(card1) == "40":
                        total = 12
                        break
                    else:
                        card_val2 = 11
                        total = int(card_val1 + card_val2)
                        break
                elif str(card2) == "40":
                    if str(card1) == "14":
                        total = 12
                        break
                    elif str(card1) == "27":
                        total = 12
                        break
                    elif str(card1) == "40":
                        total = 12
                        break
                    else:
                        card_val2 = 11
                        total = int(card_val1 + card_val2)
                        break
                else:
                    total = int(card_val1 + card_val2)
                    break
            Spades = [1, 14, 27, 40]

            print("Your Total Is " + str(total))

            cc = 2
            bb = 0
            while total <= 21:
                print("\nDo You Want To Hit or Stay?")
                print("1: Hit")
                print("2: Stay")
                action = input()
                if action == "1":
                    cards.append(random.randint(1, 52))
                    card3 = cards[cc]
                    while bb < len(cards):
                        if card3 == cards[bb]:
                            del (cards[cc])
                            cards.append(random.randint(1, 52))
                        else:
                            bb += 1
                    card3 = cards[cc]
                    print("\nYou Drew The " + str(deck.get(card3)))
                    if cards[cc] == 1:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    elif cards[cc] == 14:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    elif cards[cc] == 27:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    elif cards[cc] == 40:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    else:
                        cvalnew = card_value.get(str(deck.get(card3)))
                        total = (total + cvalnew)
                        print("\nYour New Total Is " + str(total))
                        if total > 21:
                            deviation1 = total - 21
                            Bust3 = True
                            print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    cc += 1
                elif action == "hit":
                    cards.append(random.randint(1, 52))
                    card3 = cards[cc]
                    while bb < len(cards):
                        if card3 == cards[bb]:
                            del (cards[cc])
                            cards.append(random.randint(1, 52))
                        else:
                            bb += 1
                    card3 = cards[cc]
                    print("\nYou Drew The " + str(deck.get(card3)))
                    if cards[cc] == 1:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    elif cards[cc] == 14:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    elif cards[cc] == 27:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    elif cards[cc] == 40:
                        if int(total) + 11 <= 21:
                            total = total + 11
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                        else:
                            total = total + 1
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    else:
                        cvalnew = card_value.get(str(deck.get(card3)))
                        total = (total + cvalnew)
                        print("\nYour New Total Is " + str(total))
                        if total > 21:
                            deviation1 = total - 21
                            Bust3 = True
                            print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                    cc += 1
                elif action == "2":
                    deviation1 = 21 - total
                    print("\nYour Score Was " + str(deviation1) + " Off of 21")
                    break
                elif action == "stay":
                    deviation1 = 21 - total
                    print("\nYour Score Was " + str(deviation1) + " Off of 21")
                    break

        dealer = True
        if dealer == True:
            deck = {
                1: "Ace of Spades",
                2: "2 of Spades",
                3: "3 of Spades",
                4: "4 of Spades",
                5: "5 of Spades",
                6: "6 of Spades",
                7: "7 of Spades",
                8: "8 of Spades",
                9: "9 of Spades",
                10: "10 of Spades",
                11: "Jack of Spades",
                12: "Queen of Spades",
                13: "King of Spades",
                14: "Ace of Hearts",
                15: "2 of Hearts",
                16: "3 of Hearts",
                17: "4 of Hearts",
                18: "5 of Hearts",
                19: "6 of Hearts",
                20: "7 of Hearts",
                21: "8 of Hearts",
                22: "9 of Hearts",
                23: "10 of Hearts",
                24: "Jack of Hearts",
                25: "Queen of Hearts",
                26: "King of Hearts",
                27: "Ace of Diamonds",
                28: "2 of Diamonds",
                29: "3 of Diamonds",
                30: "4 of Diamonds",
                31: "5 of Diamonds",
                32: "6 of Diamonds",
                33: "7 of Diamonds",
                34: "8 of Diamonds",
                35: "9 of Diamonds",
                36: "10 of Diamonds",
                37: "Jack of Diamonds",
                38: "Queen of Diamonds",
                39: "King of Diamonds",
                40: "Ace of Clubs",
                41: "2 of Clubs",
                42: "3 of Clubs",
                43: "4 of Clubs",
                44: "5 of Clubs",
                45: "6 of Clubs",
                46: "7 of Clubs",
                47: "8 of Clubs",
                48: "9 of Clubs",
                49: "10 of Clubs",
                50: "Jack of Clubs",
                51: "Queen of Clubs",
                52: "King of Clubs"
            }
            card_value = {
                "2 of Spades": 2,
                "3 of Spades": 3,
                "4 of Spades": 4,
                "5 of Spades": 5,
                "6 of Spades": 6,
                "7 of Spades": 7,
                "8 of Spades": 8,
                "9 of Spades": 9,
                "10 of Spades": 10,
                "Jack of Spades": 10,
                "Queen of Spades": 10,
                "King of Spades": 10,
                "2 of Hearts": 2,
                "3 of Hearts": 3,
                "4 of Hearts": 4,
                "5 of Hearts": 5,
                "6 of Hearts": 6,
                "7 of Hearts": 7,
                "8 of Hearts": 8,
                "9 of Hearts": 9,
                "10 of Hearts": 10,
                "Jack of Hearts": 10,
                "Queen of Hearts": 10,
                "King of Hearts": 10,
                "2 of Diamonds": 2,
                "3 of Diamonds": 3,
                "4 of Diamonds": 4,
                "5 of Diamonds": 5,
                "6 of Diamonds": 6,
                "7 of Diamonds": 7,
                "8 of Diamonds": 8,
                "9 of Diamonds": 9,
                "10 of Diamonds": 10,
                "Jack of Diamonds": 10,
                "Queen of Diamonds": 10,
                "King of Diamonds": 10,
                "2 of Clubs": 2,
                "3 of Clubs": 3,
                "4 of Clubs": 4,
                "5 of Clubs": 5,
                "6 of Clubs": 6,
                "7 of Clubs": 7,
                "8 of Clubs": 8,
                "9 of Clubs": 9,
                "10 of Clubs": 10,
                "Jack of Clubs": 10,
                "Queen of Clubs": 10,
                "King of Clubs": 10
            }
            bust1 = False
            cards2 = []
            cards2.append(random.randint(1, 52))
            cards2.append(random.randint(1, 52))
            a = 0
            card1 = cards2[a]
            card2 = cards2[a + 1]
            while a < len(cards2):
                if card1 == card2:
                    del (cards2[a])
                    cards2.append(random.randint(1, 52))
                else:
                    a += 1

            b = 0
            cardname1 = deck.get(cards2[b])
            cardname2 = deck.get(cards2[b + 1])
            card_val1 = card_value.get(cardname1)
            card_val2 = card_value.get(cardname2)

            total1 = 0
            while total1 <= 21:
                if str(card1) == "1":
                    if str(card2) == "14":
                        total1 = 12
                        break
                    elif str(card2) == "27":
                        total1 = 12
                        break
                    elif str(card2) == "40":
                        total1 = 12
                        break
                    else:
                        card_val1 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                elif str(card1) == "14":
                    if str(card2) == "1":
                        total1 = 12
                        break
                    elif str(card2) == "27":
                        total1 = 12
                        break
                    elif str(card2) == "40":
                        total1 = 12
                        break
                    else:
                        card_val1 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                elif str(card1) == "27":
                    if str(card2) == "1":
                        total1 = 12
                        break
                    elif str(card2) == "14":
                        total1 = 12
                        break
                    elif str(card2) == "40":
                        total1 = 12
                        break
                    else:
                        card_val1 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                elif str(card1) == "40":
                    if str(card2) == "1":
                        total1 = 12
                        break
                    elif str(card2) == "14":
                        total1 = 12
                        break
                    elif str(card2) == "27":
                        total1 = 12
                        break
                    else:
                        card_val1 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                elif str(card2) == "1":
                    if str(card1) == "14":
                        total1 = 12
                        break
                    elif str(card1) == "27":
                        total1 = 12
                        break
                    elif str(card1) == "40":
                        total1 = 12
                        break
                    else:
                        card_val2 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                elif str(card2) == "14":
                    if str(card1) == "1":
                        total1 = 12
                        break
                    elif str(card1) == "27":
                        total1 = 12
                        break
                    elif str(card1) == "40":
                        total1 = 12
                        break
                    else:
                        card_val2 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                elif str(card2) == "27":
                    if str(card1) == "1":
                        total1 = 12
                        break
                    elif str(card1) == "14":
                        total1 = 12
                        break
                    elif str(card1) == "40":
                        total1 = 12
                        break
                    else:
                        card_val2 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                elif str(card2) == "40":
                    if str(card1) == "14":
                        total1 = 12
                        break
                    elif str(card1) == "27":
                        total1 = 12
                        break
                    elif str(card1) == "40":
                        total1 = 12
                        break
                    else:
                        card_val2 = 11
                        total1 = int(card_val1 + card_val2)
                        break
                else:
                    total1 = int(card_val1 + card_val2)
                    break
            Spades = [1, 14, 27, 40]

            cc = 2
            bb = 0
            while total1 <= 21:
                if total1 <= 15:
                    action = "hit"
                else:
                    action = "stay"
                if action == "1":
                    cards2.append(random.randint(1, 52))
                    card3 = cards2[cc]
                    while bb < len(cards2):
                        if card3 == cards2[bb]:
                            del (cards2[cc])
                            cards2.append(random.randint(1, 52))
                        else:
                            bb += 1
                    card3 = cards2[cc]
                elif action == "hit":
                    cards2.append(random.randint(1, 52))
                    card3 = cards2[cc]
                    while bb < len(cards2):
                        if card3 == cards2[bb]:
                            del (cards2[cc])
                            cards2.append(random.randint(1, 52))
                        else:
                            bb += 1
                    card3 = cards2[cc]
                    if cards2[cc] == 1:
                        if int(total1) + 11 <= 21:
                            total1 = total1 + 11
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                        else:
                            total1 = total1 + 1
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                    elif cards2[cc] == 14:
                        if int(total1) + 11 <= 21:
                            total1 = total1 + 11
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                        else:
                            total1 = total1 + 1
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                    elif cards2[cc] == 27:
                        if int(total1) + 11 <= 21:
                            total1 = total1 + 11
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                        else:
                            total1 = total1 + 1
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                    elif cards2[cc] == 40:
                        if int(total1) + 11 <= 21:
                            total1 = total1 + 11
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                        else:
                            total1 = total1 + 1
                            if total1 > 21:
                                deviation2 = total1 - 21
                                bust1 = True
                    else:
                        cvalnew = card_value.get(str(deck.get(card3)))
                        total1 = (total1 + cvalnew)
                        if total1 > 21:
                            deviation2 = total1 - 21
                            bust1 = True
                    cc += 1
                elif action == "stay":
                    deviation2 = 21 - total1
                    break

        if Bust3 == True:
            if bust1 == True:
                time.sleep(1.25)
                cards7 = []
                print("\nThe House Had A Score Of " + str(total1))
                rr = 0
                while rr < len(cards2):
                    cards7.append(deck.get(cards2[rr]))
                    rr += 1
                print("With: The ", end="")
                print(*cards7, sep=(", The "))
                cards9 = []
                yy = 0
                while yy < len(cards):
                    cards9.append(deck.get(cards[yy]))
                    yy += 1
                print("\nTo Your: ", end="")
                print(*cards9, sep=(", "))
                time.sleep(1.25)
                print("\n\nBoth You And The House Have Busted, It Is A Tie")
                Win1 = "Tie"
                return Win1
            if bust1 == False:
                time.sleep(1.25)
                cards7 = []
                print("\nThe House Had A Score Of " + str(total1))
                rr = 0
                while rr < len(cards2):
                    cards7.append(deck.get(cards2[rr]))
                    rr += 1
                print("With: The ", end="")
                print(*cards7, sep=(", The "))
                cards9 = []
                yy = 0
                while yy < len(cards):
                    cards9.append(deck.get(cards[yy]))
                    yy += 1
                print("\nTo Your: ", end="")
                print(*cards9, sep=(", "))
                time.sleep(1.25)
                print("\n\nYou Have Busted But The House Has Not, Thus The House Wins By Default")
                Win1 = "Loss"
                return Win1
        if Bust3 == False:
            if bust1 == True:
                time.sleep(1.25)
                cards7 = []
                print("\nThe House Had A Score Of " + str(total1))
                rr = 0
                while rr < len(cards2):
                    cards7.append(deck.get(cards2[rr]))
                    rr += 1
                print("With: The ", end="")
                print(*cards7, sep=(", The "))
                cards9 = []
                yy = 0
                while yy < len(cards):
                    cards9.append(deck.get(cards[yy]))
                    yy += 1
                print("\nTo Your: ", end="")
                print(*cards9, sep=(", "))
                winnings = total1 - total
                time.sleep(1.25)
                print("\n\nThe House Has Busted, You Win By Default")
                Win1 = "Win"
                return Win1
            elif bust1 == False:
                if total > total1:
                    time.sleep(1.25)
                    cards7 = []
                    print("\nThe House Had A Score Of " + str(total1))
                    rr = 0
                    while rr < len(cards2):
                        cards7.append(deck.get(cards2[rr]))
                        rr += 1
                    print("With: The ", end="")
                    print(*cards7, sep=(", The "))
                    cards9 = []
                    yy = 0
                    while yy < len(cards):
                        cards9.append(deck.get(cards[yy]))
                        yy += 1
                    print("\nTo Your: ", end="")
                    print(*cards9, sep=(", "))
                    winnings = total - total1
                    time.sleep(1.25)
                    print("\n\nYou Have Beaten The House By " + str(winnings))
                    Win1 = "Win"
                    return Win1
                elif total1 > total:
                    time.sleep(1.25)
                    cards7 = []
                    print("\nThe House Had A Score Of " + str(total1))
                    rr = 0
                    while rr < len(cards2):
                        cards7.append(deck.get(cards2[rr]))
                        rr += 1
                    print("With: The ", end="")
                    print(*cards7, sep=(", The "))
                    cards9 = []
                    yy = 0
                    while yy < len(cards):
                        cards9.append(deck.get(cards[yy]))
                        yy += 1
                    print("\nTo Your: ", end="")
                    print(*cards9, sep=(", "))
                    winnings = total1 - total
                    time.sleep(1.25)
                    print("\n\nYou Have Lost To The House By " + str(winnings))
                    Win1 = "Loss"
                    return Win1
                elif total == total1:
                    time.sleep(1.25)
                    cards7 = []
                    print("\nThe House Had A Score Of " + str(total1))
                    rr = 0
                    while rr < len(cards2):
                        cards7.append(deck.get(cards2[rr]))
                        rr += 1
                    print("With: The ", end="")
                    print(*cards7, sep=(", The "))
                    cards9 = []
                    yy = 0
                    while yy < len(cards):
                        cards9.append(deck.get(cards[yy]))
                        yy += 1
                    print("\nTo Your: ", end="")
                    print(*cards9, sep=(", "))
                    time.sleep(1.25)
                    print("\n\nYou Have Tied The House With A Score Of " + str(total))
                    Win1 = "Tie"
                    return Win1

    def house_rules2():
        def player1():
            print("Player 1's Turn")
            import time
            time.sleep(1.15)
            ready1 = input("Hit Enter When Ready")
            Win1 = False
            Loss1 = False
            Tie1 = False
            shuffle = True
            if shuffle == True:
                deck = {
                    1: "Ace of Spades",
                    2: "2 of Spades",
                    3: "3 of Spades",
                    4: "4 of Spades",
                    5: "5 of Spades",
                    6: "6 of Spades",
                    7: "7 of Spades",
                    8: "8 of Spades",
                    9: "9 of Spades",
                    10: "10 of Spades",
                    11: "Jack of Spades",
                    12: "Queen of Spades",
                    13: "King of Spades",
                    14: "Ace of Hearts",
                    15: "2 of Hearts",
                    16: "3 of Hearts",
                    17: "4 of Hearts",
                    18: "5 of Hearts",
                    19: "6 of Hearts",
                    20: "7 of Hearts",
                    21: "8 of Hearts",
                    22: "9 of Hearts",
                    23: "10 of Hearts",
                    24: "Jack of Hearts",
                    25: "Queen of Hearts",
                    26: "King of Hearts",
                    27: "Ace of Diamonds",
                    28: "2 of Diamonds",
                    29: "3 of Diamonds",
                    30: "4 of Diamonds",
                    31: "5 of Diamonds",
                    32: "6 of Diamonds",
                    33: "7 of Diamonds",
                    34: "8 of Diamonds",
                    35: "9 of Diamonds",
                    36: "10 of Diamonds",
                    37: "Jack of Diamonds",
                    38: "Queen of Diamonds",
                    39: "King of Diamonds",
                    40: "Ace of Clubs",
                    41: "2 of Clubs",
                    42: "3 of Clubs",
                    43: "4 of Clubs",
                    44: "5 of Clubs",
                    45: "6 of Clubs",
                    46: "7 of Clubs",
                    47: "8 of Clubs",
                    48: "9 of Clubs",
                    49: "10 of Clubs",
                    50: "Jack of Clubs",
                    51: "Queen of Clubs",
                    52: "King of Clubs"
                }
                card_value = {
                    "2 of Spades": 2,
                    "3 of Spades": 3,
                    "4 of Spades": 4,
                    "5 of Spades": 5,
                    "6 of Spades": 6,
                    "7 of Spades": 7,
                    "8 of Spades": 8,
                    "9 of Spades": 9,
                    "10 of Spades": 10,
                    "Jack of Spades": 10,
                    "Queen of Spades": 10,
                    "King of Spades": 10,
                    "2 of Hearts": 2,
                    "3 of Hearts": 3,
                    "4 of Hearts": 4,
                    "5 of Hearts": 5,
                    "6 of Hearts": 6,
                    "7 of Hearts": 7,
                    "8 of Hearts": 8,
                    "9 of Hearts": 9,
                    "10 of Hearts": 10,
                    "Jack of Hearts": 10,
                    "Queen of Hearts": 10,
                    "King of Hearts": 10,
                    "2 of Diamonds": 2,
                    "3 of Diamonds": 3,
                    "4 of Diamonds": 4,
                    "5 of Diamonds": 5,
                    "6 of Diamonds": 6,
                    "7 of Diamonds": 7,
                    "8 of Diamonds": 8,
                    "9 of Diamonds": 9,
                    "10 of Diamonds": 10,
                    "Jack of Diamonds": 10,
                    "Queen of Diamonds": 10,
                    "King of Diamonds": 10,
                    "2 of Clubs": 2,
                    "3 of Clubs": 3,
                    "4 of Clubs": 4,
                    "5 of Clubs": 5,
                    "6 of Clubs": 6,
                    "7 of Clubs": 7,
                    "8 of Clubs": 8,
                    "9 of Clubs": 9,
                    "10 of Clubs": 10,
                    "Jack of Clubs": 10,
                    "Queen of Clubs": 10,
                    "King of Clubs": 10
                }
                Bust3 = False
                cards = []
                cards.append(random.randint(1, 52))
                cards.append(random.randint(1, 52))
                a = 0
                card1 = cards[a]
                card2 = cards[a + 1]
                while a < len(cards):
                    if card1 == card2:
                        del (cards[a])
                        cards.append(random.randint(1, 52))
                    else:
                        a += 1

                b = 0
                print("\nyour cards are the " + deck.get(cards[b]) + " and the " + deck.get(cards[b + 1]))
                print("")

                cardname1 = deck.get(cards[b])
                cardname2 = deck.get(cards[b + 1])
                card_val1 = card_value.get(cardname1)
                card_val2 = card_value.get(cardname2)

                total = 0
                while total <= 21:
                    if str(card1) == "1":
                        if str(card2) == "14":
                            total = 12
                            break
                        elif str(card2) == "27":
                            total = 12
                            break
                        elif str(card2) == "40":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card1) == "14":
                        if str(card2) == "1":
                            total = 12
                            break
                        elif str(card2) == "27":
                            total = 12
                            break
                        elif str(card2) == "40":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card1) == "27":
                        if str(card2) == "1":
                            total = 12
                            break
                        elif str(card2) == "14":
                            total = 12
                            break
                        elif str(card2) == "40":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card1) == "40":
                        if str(card2) == "1":
                            total = 12
                            break
                        elif str(card2) == "14":
                            total = 12
                            break
                        elif str(card2) == "27":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "1":
                        if str(card1) == "14":
                            total = 12
                            break
                        elif str(card1) == "27":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "14":
                        if str(card1) == "1":
                            total = 12
                            break
                        elif str(card1) == "27":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "27":
                        if str(card1) == "1":
                            total = 12
                            break
                        elif str(card1) == "14":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "40":
                        if str(card1) == "14":
                            total = 12
                            break
                        elif str(card1) == "27":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    else:
                        total = int(card_val1 + card_val2)
                        break
                Spades = [1, 14, 27, 40]

                print("Your Total Is " + str(total))

                cc = 2
                bb = 0
                while total <= 21:
                    print("\nDo You Want To Hit or Stay?")
                    print("1: Hit")
                    print("2: Stay")
                    action = input()
                    if action == "1":
                        cards.append(random.randint(1, 52))
                        card3 = cards[cc]
                        while bb < len(cards):
                            if card3 == cards[bb]:
                                del (cards[cc])
                                cards.append(random.randint(1, 52))
                            else:
                                bb += 1
                        card3 = cards[cc]
                        print("\nYou Drew The " + str(deck.get(card3)))
                        if cards[cc] == 1:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 14:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 27:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 40:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        else:
                            cvalnew = card_value.get(str(deck.get(card3)))
                            total = (total + cvalnew)
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                return total, deviation1
                        cc += 1
                    elif action == "hit":
                        cards.append(random.randint(1, 52))
                        card3 = cards[cc]
                        while bb < len(cards):
                            if card3 == cards[bb]:
                                del (cards[cc])
                                cards.append(random.randint(1, 52))
                            else:
                                bb += 1
                        card3 = cards[cc]
                        print("\nYou Drew The " + str(deck.get(card3)))
                        if cards[cc] == 1:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 14:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 27:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 40:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        else:
                            cvalnew = card_value.get(str(deck.get(card3)))
                            total = (total + cvalnew)
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                return total, deviation1
                        cc += 1
                    elif action == "2":
                        deviation1 = 21 - total
                        print("\nYour Score Was " + str(deviation1) + " Off of 21")
                        return total, deviation1
                        break
                    elif action == "stay":
                        deviation1 = 21 - total
                        print("\nYour Score Was " + str(deviation1) + " Off of 21")
                        return total, deviation1
                        break

        def player2():
            print("Player 2's Turn")
            import time
            time.sleep(1.15)
            ready1 = input("Hit Enter When Ready")
            Win1 = False
            Loss1 = False
            Tie1 = False
            shuffle = True
            if shuffle == True:
                deck = {
                    1: "Ace of Spades",
                    2: "2 of Spades",
                    3: "3 of Spades",
                    4: "4 of Spades",
                    5: "5 of Spades",
                    6: "6 of Spades",
                    7: "7 of Spades",
                    8: "8 of Spades",
                    9: "9 of Spades",
                    10: "10 of Spades",
                    11: "Jack of Spades",
                    12: "Queen of Spades",
                    13: "King of Spades",
                    14: "Ace of Hearts",
                    15: "2 of Hearts",
                    16: "3 of Hearts",
                    17: "4 of Hearts",
                    18: "5 of Hearts",
                    19: "6 of Hearts",
                    20: "7 of Hearts",
                    21: "8 of Hearts",
                    22: "9 of Hearts",
                    23: "10 of Hearts",
                    24: "Jack of Hearts",
                    25: "Queen of Hearts",
                    26: "King of Hearts",
                    27: "Ace of Diamonds",
                    28: "2 of Diamonds",
                    29: "3 of Diamonds",
                    30: "4 of Diamonds",
                    31: "5 of Diamonds",
                    32: "6 of Diamonds",
                    33: "7 of Diamonds",
                    34: "8 of Diamonds",
                    35: "9 of Diamonds",
                    36: "10 of Diamonds",
                    37: "Jack of Diamonds",
                    38: "Queen of Diamonds",
                    39: "King of Diamonds",
                    40: "Ace of Clubs",
                    41: "2 of Clubs",
                    42: "3 of Clubs",
                    43: "4 of Clubs",
                    44: "5 of Clubs",
                    45: "6 of Clubs",
                    46: "7 of Clubs",
                    47: "8 of Clubs",
                    48: "9 of Clubs",
                    49: "10 of Clubs",
                    50: "Jack of Clubs",
                    51: "Queen of Clubs",
                    52: "King of Clubs"
                }
                card_value = {
                    "2 of Spades": 2,
                    "3 of Spades": 3,
                    "4 of Spades": 4,
                    "5 of Spades": 5,
                    "6 of Spades": 6,
                    "7 of Spades": 7,
                    "8 of Spades": 8,
                    "9 of Spades": 9,
                    "10 of Spades": 10,
                    "Jack of Spades": 10,
                    "Queen of Spades": 10,
                    "King of Spades": 10,
                    "2 of Hearts": 2,
                    "3 of Hearts": 3,
                    "4 of Hearts": 4,
                    "5 of Hearts": 5,
                    "6 of Hearts": 6,
                    "7 of Hearts": 7,
                    "8 of Hearts": 8,
                    "9 of Hearts": 9,
                    "10 of Hearts": 10,
                    "Jack of Hearts": 10,
                    "Queen of Hearts": 10,
                    "King of Hearts": 10,
                    "2 of Diamonds": 2,
                    "3 of Diamonds": 3,
                    "4 of Diamonds": 4,
                    "5 of Diamonds": 5,
                    "6 of Diamonds": 6,
                    "7 of Diamonds": 7,
                    "8 of Diamonds": 8,
                    "9 of Diamonds": 9,
                    "10 of Diamonds": 10,
                    "Jack of Diamonds": 10,
                    "Queen of Diamonds": 10,
                    "King of Diamonds": 10,
                    "2 of Clubs": 2,
                    "3 of Clubs": 3,
                    "4 of Clubs": 4,
                    "5 of Clubs": 5,
                    "6 of Clubs": 6,
                    "7 of Clubs": 7,
                    "8 of Clubs": 8,
                    "9 of Clubs": 9,
                    "10 of Clubs": 10,
                    "Jack of Clubs": 10,
                    "Queen of Clubs": 10,
                    "King of Clubs": 10
                }
                Bust3 = False
                cards = []
                cards.append(random.randint(1, 52))
                cards.append(random.randint(1, 52))
                a = 0
                card1 = cards[a]
                card2 = cards[a + 1]
                while a < len(cards):
                    if card1 == card2:
                        del (cards[a])
                        cards.append(random.randint(1, 52))
                    else:
                        a += 1

                b = 0
                print("\nyour cards are the " + deck.get(cards[b]) + " and the " + deck.get(cards[b + 1]))
                print("")

                cardname1 = deck.get(cards[b])
                cardname2 = deck.get(cards[b + 1])
                card_val1 = card_value.get(cardname1)
                card_val2 = card_value.get(cardname2)

                total = 0
                while total <= 21:
                    if str(card1) == "1":
                        if str(card2) == "14":
                            total = 12
                            break
                        elif str(card2) == "27":
                            total = 12
                            break
                        elif str(card2) == "40":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card1) == "14":
                        if str(card2) == "1":
                            total = 12
                            break
                        elif str(card2) == "27":
                            total = 12
                            break
                        elif str(card2) == "40":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card1) == "27":
                        if str(card2) == "1":
                            total = 12
                            break
                        elif str(card2) == "14":
                            total = 12
                            break
                        elif str(card2) == "40":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card1) == "40":
                        if str(card2) == "1":
                            total = 12
                            break
                        elif str(card2) == "14":
                            total = 12
                            break
                        elif str(card2) == "27":
                            total = 12
                            break
                        else:
                            card_val1 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "1":
                        if str(card1) == "14":
                            total = 12
                            break
                        elif str(card1) == "27":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "14":
                        if str(card1) == "1":
                            total = 12
                            break
                        elif str(card1) == "27":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "27":
                        if str(card1) == "1":
                            total = 12
                            break
                        elif str(card1) == "14":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    elif str(card2) == "40":
                        if str(card1) == "14":
                            total = 12
                            break
                        elif str(card1) == "27":
                            total = 12
                            break
                        elif str(card1) == "40":
                            total = 12
                            break
                        else:
                            card_val2 = 11
                            total = int(card_val1 + card_val2)
                            break
                    else:
                        total = int(card_val1 + card_val2)
                        break
                Spades = [1, 14, 27, 40]

                print("Your Total Is " + str(total))

                cc = 2
                bb = 0
                while total <= 21:
                    print("\nDo You Want To Hit or Stay?")
                    print("1: Hit")
                    print("2: Stay")
                    action = input()
                    if action == "1":
                        cards.append(random.randint(1, 52))
                        card3 = cards[cc]
                        while bb < len(cards):
                            if card3 == cards[bb]:
                                del (cards[cc])
                                cards.append(random.randint(1, 52))
                            else:
                                bb += 1
                        card3 = cards[cc]
                        print("\nYou Drew The " + str(deck.get(card3)))
                        if cards[cc] == 1:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 14:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 27:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 40:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        else:
                            cvalnew = card_value.get(str(deck.get(card3)))
                            total = (total + cvalnew)
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                return total, deviation1
                        cc += 1
                    elif action == "hit":
                        cards.append(random.randint(1, 52))
                        card3 = cards[cc]
                        while bb < len(cards):
                            if card3 == cards[bb]:
                                del (cards[cc])
                                cards.append(random.randint(1, 52))
                            else:
                                bb += 1
                        card3 = cards[cc]
                        print("\nYou Drew The " + str(deck.get(card3)))
                        if cards[cc] == 1:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 14:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 27:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        elif cards[cc] == 40:
                            if int(total) + 11 <= 21:
                                total = total + 11
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                            else:
                                total = total + 1
                                print("\nYour New Total Is " + str(total))
                                if total > 21:
                                    deviation1 = total - 21
                                    Bust3 = True
                                    print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                    return total, deviation1
                        else:
                            cvalnew = card_value.get(str(deck.get(card3)))
                            total = (total + cvalnew)
                            print("\nYour New Total Is " + str(total))
                            if total > 21:
                                deviation1 = total - 21
                                Bust3 = True
                                print("\nBust. Your Score Was " + str(deviation1) + " Over 21")
                                return total, deviation1
                        cc += 1
                    elif action == "2":
                        deviation1 = 21 - total
                        print("\nYour Score Was " + str(deviation1) + " Off of 21")
                        return total, deviation1
                        break
                    elif action == "stay":
                        deviation1 = 21 - total
                        print("\nYour Score Was " + str(deviation1) + " Off of 21")
                        return total, deviation1
                        break

        print("")
        player11 = player1()
        total11 = player11[0]
        deviation11 = player11[1]
        import time
        time.sleep(1.75)
        spaces1 = 0
        while spaces1 <= 50:
            print("")
            spaces1 += 1
        player22 = player2()
        print("\n\n")
        total22 = player22[0]
        deviation22 = player22[1]
        if total11 > 21:
            Bust3 = True
        elif total11 <= 21:
            Bust3 = False

        if total22 > 21:
            bust1 = True
        elif total22 <= 21:
            bust1 = False

        if Bust3 == True:
            if bust1 == True:
                time.sleep(1.25)
                print("Player 1 had a score of " + str(total11))
                print("\nPlayer 2 had a score of " + str(total22))
                time.sleep(.75)
                print("\nPlayer 1 was " + str(deviation11) + " over 21, and")
                print("\nPlayer 2 was " + str(deviation22) + " over 21")
                time.sleep(1)
                print("\n\nBoth You And The House Have Busted, It Is A Tie")
                Win1 = "Tie"
                return Win1
            if bust1 == False:
                time.sleep(1.25)
                print("Player 1 had a score of " + str(total11))
                print("\nPlayer 2 had a score of " + str(total22))
                time.sleep(.75)
                print("\nPlayer 1 was " + str(deviation11) + " over 21, and")
                print("\nPlayer 2 was " + str(deviation22) + " under 21")
                time.sleep(1)
                print("\n\nPlayer 1 Has Busted But Player 2 Has Not, Thus Player 2 Wins By Default")
                Win1 = "Loss"
                return Win1
        if Bust3 == False:
            if bust1 == True:
                time.sleep(1.25)
                print("Player 1 had a score of " + str(total11))
                print("\nPlayer 2 had a score of " + str(total22))
                time.sleep(.75)
                print("\nPlayer 1 was " + str(deviation11) + " under 21, and")
                print("\nPlayer 2 was " + str(deviation22) + " over 21")
                time.sleep(1)
                print("\n\nPlayer 2 Has Busted But Player 1 Has Not, Thus Player 1 Wins By Default")
                Win1 = "Win"
                return Win1
            elif bust1 == False:
                if total11 > total22:
                    time.sleep(1.25)
                    print("Player 1 had a score of " + str(total11))
                    print("\nPlayer 2 had a score of " + str(total22))
                    time.sleep(.75)
                    print("\nPlayer 1 was " + str(deviation11) + " under 21, and")
                    print("\nPlayer 2 was " + str(deviation22) + " under 21")
                    time.sleep(1)
                    winnings = int(total11) - int(total22)
                    print("\n\nPlayer 1 Has Beaten Player 2 By " + str(winnings))
                    Win1 = "Win"
                    return Win1
                elif total22 > total11:
                    time.sleep(1.25)
                    print("Player 1 had a score of " + str(total11))
                    print("\nPlayer 2 had a score of " + str(total22))
                    time.sleep(.75)
                    print("\nPlayer 1 was " + str(deviation11) + " under 21, and")
                    print("\nPlayer 2 was " + str(deviation22) + " under 21")
                    time.sleep(1)
                    winnings = int(total22) - int(total11)
                    print("\n\nPlayer 2 Has Beaten Player 1 By " + str(winnings))
                    Win1 = "Loss"
                    return Win1
                elif total11 == total22:
                    time.sleep(1.25)
                    print("Player 1 had a score of " + str(total11))
                    print("\nPlayer 2 had a score of " + str(total22))
                    time.sleep(.75)
                    print("\nPlayer 1 was " + str(deviation11) + " under 21, and")
                    print("\nPlayer 2 was " + str(deviation22) + " under 21")
                    time.sleep(1)
                    print("\n\nPlayer 1 Has Tied Player 1 With A Score Of " + str(total11))
                    Win1 = "Tie"
                    return Win1

    def rulebook():
        print("\n\nThe object of the game is to score the closest to 21 without going over.\n")
        print("You win the game by getting a score that is higher than your opponent's score,\n")
        print("but is not higher than the number 21.\n")
        print("You lose the game if your opponent scores a number higher than yours without going over 21,\n")
        print("or if your score is over 21.\n")
        print("If your score and the score of your opponent is the same, the game is declared a tie.\n")
        print("Cards with numbers (3's, 7's, etc.) represent their face value.\n")
        print("Face cards (kings, queens, and jacks) are given the value of 10.\n")
        print("Aces are trickier, representing either an 11,\n")
        print("or a 1 if 11 would cause your score to go over the total value of 21.\n")
        print("You will be playing against the house, and your wins and losses will be recorded.\n")
        print("Your cards will be randomly dealt to you.\n")
        print("Once you recieve your cards you may either hit (meaning you request another card),\n")
        print(
            "or you may pass (meaning you are satisfied with your score and you are ready to compare with the house).\n")
        print("You may of course quit the game whenever you would like.\n")
        print("Although, be warned, it is quite fun and may be addicting without moderation.\n")
        print("Good luck to you!\n")
        print("And in the words of Effie Trinket,\n")
        print("\"May the odds be ever in your favor\"\n")

    print("\nHello There And Welcome To Bored Co. Black Jack")
    time.sleep(1.05)
    end = 0
    rounds = 0
    valid = 0
    while end < 1:
        if rounds < 1:
            if valid < 1:
                print("\nWould You Like To Play A Hand?")
                print("1: Yes")
                print("2: No")
                print("3: Rules")
                trial = input()
            else:
                print("\nInput Invalid")
                time.sleep(1)
                print("\nWould You Like To Play A Hand?")
                print("1: Yes")
                print("2: No")
                print("3: Rules")
                trial = input()
                valid += 1
        else:
            time.sleep(1)
            print("\n\nWould You Like To Play Again?")
            print("1: Yes")
            print("2: No")
            trial = input()
        if trial == "1":
            valid1 = False
            while valid1 == False:
                print("\nSingle Player or Dual Player?")
                print("1: Single Player")
                print("2: Dual Player")
                players = input()
                if players == "single":
                    Win1 = house_rules()
                elif players == "1":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "Single":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "single player":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "one":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "2":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "dual":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "Double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                else:
                    print("\nInvalid Player Choice, Select Again Please\n")
            rounds += 1
            if Win1 == "Win":
                Win += 1
            elif Win1 == "Loss":
                Loss += 1
            elif Win1 == "Tie":
                Tie += 1
        elif trial == "yes":
            valid1 = False
            while valid1 == False:
                print("\nSingle Player or Dual Player?")
                print("1: Single Player")
                print("2: Dual Player")
                players = input()
                if players == "single":
                    Win1 = house_rules()
                elif players == "1":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "Single":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "single player":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "one":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "2":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "dual":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "Double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                else:
                    print("\nInvalid Player Choice, Select Again Please\n")
            rounds += 1
            if Win1 == "Win":
                Win += 1
            elif Win1 == "Loss":
                Loss += 1
            elif Win1 == "Tie":
                Tie += 1
        elif trial == "Yes":
            valid1 = False
            while valid1 == False:
                print("\nSingle Player or Dual Player?")
                print("1: Single Player")
                print("2: Dual Player")
                players = input()
                if players == "single":
                    Win1 = house_rules()
                elif players == "1":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "Single":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "single player":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "one":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "2":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "dual":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "Double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                else:
                    print("\nInvalid Player Choice, Select Again Please\n")
            rounds += 1
            if Win1 == "Win":
                Win += 1
            elif Win1 == "Loss":
                Loss += 1
            elif Win1 == "Tie":
                Tie += 1
        elif trial == "start":
            valid1 = False
            while valid1 == False:
                print("\nSingle Player or Dual Player?")
                print("1: Single Player")
                print("2: Dual Player")
                players = input()
                if players == "single":
                    Win1 = house_rules()
                elif players == "1":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "Single":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "single player":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "one":
                    numplay = "1"
                    Win1 = house_rules()
                    valid1 = True
                elif players == "2":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "dual":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                elif players == "Double":
                    numplay = "2"
                    Win1 = house_rules2()
                    valid1 = True
                else:
                    print("\nInvalid Player Choice, Select Again Please\n")
            rounds += 1
            if Win1 == "Win":
                Win += 1
            elif Win1 == "Loss":
                Loss += 1
            elif Win1 == "Tie":
                Tie += 1
        elif trial == "2":
            if numplay == "0":
                print("\nThen what are you doing still hanging around here for?")
                print("\nAnyway, have a nice day!")
                break
            if numplay == "1":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nYou Won 1 Hand, There Were No Losses Or Ties")
                    if Win1 == "Loss":
                        print("\nYou Lost 1 Hand, There Were No Wins Or Ties")
                    if Win1 == "Tie":
                        print("\nYou Tied 1 Hand, There Were No Wins Or Losses")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nYou Won " + str(Win))
                    print("You Lost " + str(Loss))
                    print("You Tied " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
            if numplay == "2":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nPlayer 1:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                    if Win1 == "Loss":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                    if Win1 == "Tie":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nPlayer 1:")
                    print(" Won:  " + str(Win))
                    print(" Lost: " + str(Loss))
                    print(" Tied: " + str(Tie))
                    print("\nPlayer 2:")
                    print(" Won:  " + str(Loss))
                    print(" Lost: " + str(Win))
                    print(" Tied: " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
        elif trial == "no":
            if numplay == "0":
                print("\nThen what are you doing still hanging around here for?")
                print("\nAnyway, have a nice day!")
                break
            if numplay == "1":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nYou Won 1 Hand, There Were No Losses Or Ties")
                    if Win1 == "Loss":
                        print("\nYou Lost 1 Hand, There Were No Wins Or Ties")
                    if Win1 == "Tie":
                        print("\nYou Tied 1 Hand, There Were No Wins Or Losses")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nYou Won " + str(Win))
                    print("You Lost " + str(Loss))
                    print("You Tied " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
            if numplay == "2":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nPlayer 1:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                    if Win1 == "Loss":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                    if Win1 == "Tie":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nPlayer 1:")
                    print(" Won:  " + str(Win))
                    print(" Lost: " + str(Loss))
                    print(" Tied: " + str(Tie))
                    print("\nPlayer 2:")
                    print(" Won:  " + str(Loss))
                    print(" Lost: " + str(Win))
                    print(" Tied: " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
        elif trial == "No":
            if numplay == "0":
                print("\nThen what are you doing still hanging around here for?")
                print("\nAnyway, have a nice day!")
                break
            if numplay == "1":
                if rounds == True:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nYou Won 1 Hand, There Were No Losses Or Ties")
                    if Win1 == "Loss":
                        print("\nYou Lost 1 Hand, There Were No Wins Or Ties")
                    if Win1 == "Tie":
                        print("\nYou Tied 1 Hand, There Were No Wins Or Losses")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nYou Won " + str(Win))
                    print("You Lost " + str(Loss))
                    print("You Tied " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
            if numplay == "2":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nPlayer 1:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                    if Win1 == "Loss":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                    if Win1 == "Tie":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nPlayer 1:")
                    print(" Won:  " + str(Win))
                    print(" Lost: " + str(Loss))
                    print(" Tied: " + str(Tie))
                    print("\nPlayer 2:")
                    print(" Won:  " + str(Loss))
                    print(" Lost: " + str(Win))
                    print(" Tied: " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
        elif trial == "End":
            if numplay == "1":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nYou Won 1 Hand, There Were No Losses Or Ties")
                    if Win1 == "Loss":
                        print("\nYou Lost 1 Hand, There Were No Wins Or Ties")
                    if Win1 == "Tie":
                        print("\nYou Tied 1 Hand, There Were No Wins Or Losses")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nYou Won " + str(Win))
                    print("You Lost " + str(Loss))
                    print("You Tied " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
            if numplay == "2":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nPlayer 1:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                    if Win1 == "Loss":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                    if Win1 == "Tie":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nPlayer 1:")
                    print(" Won:  " + str(Win))
                    print(" Lost: " + str(Loss))
                    print(" Tied: " + str(Tie))
                    print("\nPlayer 2:")
                    print(" Won:  " + str(Loss))
                    print(" Lost: " + str(Win))
                    print(" Tied: " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
        elif trial == "Stop":
            if numplay == "1":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nYou Won 1 Hand, There Were No Losses Or Ties")
                    if Win1 == "Loss":
                        print("\nYou Lost 1 Hand, There Were No Wins Or Ties")
                    if Win1 == "Tie":
                        print("\nYou Tied 1 Hand, There Were No Wins Or Losses")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nYou Won " + str(Win))
                    print("You Lost " + str(Loss))
                    print("You Tied " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
            if numplay == "2":
                if rounds == 1:
                    print("\nYou Played 1 Hand")
                    if Win1 == "Win":
                        print("\nPlayer 1:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                    if Win1 == "Loss":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 1")
                        print(" Tied: 0")
                        print("\nPlayer 2:")
                        print(" Won:  1")
                        print(" Lost: 0")
                        print(" Tied: 0")
                    if Win1 == "Tie":
                        print("\nPlayer 1:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                        print("\nPlayer 2:")
                        print(" Won:  0")
                        print(" Lost: 0")
                        print(" Tied: 1")
                    import time
                    time.sleep(1.5)
                    print("\nI Hope You Had Fun, Have A Nice Day!")
                    end += 1
                    break
                else:
                    print("\nYou Played " + str(rounds) + " Hands")
                    print("\nPlayer 1:")
                    print(" Won:  " + str(Win))
                    print(" Lost: " + str(Loss))
                    print(" Tied: " + str(Tie))
                    print("\nPlayer 2:")
                    print(" Won:  " + str(Loss))
                    print(" Lost: " + str(Win))
                    print(" Tied: " + str(Tie))
                import time
                time.sleep(1.5)
                print("\nI Hope You Had Fun, Have A Nice Day!")
                end += 1
                break
        elif trial == "3":
            rulebook()
        elif trial == "rules":
            rulebook()
        elif trial == "Rules":
            rulebook()
        else:
            print("\nInvalid Input\n")

def mission_statement():
    import time
    message12 = ['T', 'h', 'e', ' ', 'o', 'b', 'j', 'e', 'c', 't', 'i', 'v', 'e', ' ', 'o', 'f', ' ', 't', 'h', 'e',
                 ' ', 'e', 'n', 'c', 'r', 'y', 'p', 't', 'o', 'r', ' ', 'i', 's', ' ', 't', 'o', ' ', 'c', 'r', 'e',
                 'a', 't', 'e', ' ', 'a', ' ', 's', 'a', 'f', 'e', ' ', 'w', 'a', 'y', ' ', 't', 'o', ' ', 'c', 'o',
                 'm', 'm', 'u', 'n', 'i', 'c', 'a', 't', 'e']
    message13 = ['a', 'n', 'd', ' ', 's', 't', 'o', 'r', 'e', ' ', 's', 'e', 'n', 's', 'i', 't', 'i', 'v', 'e', ' ',
                 'd', 'a', 't', 'a', ' ', 'w', 'i', 't', 'h', 'o', 'u', 't', ' ', 'b', 'e', 'i', 'n', 'g', ' ', 'i',
                 'n', 't', 'e', 'r', 'c', 'e', 'p', 't', 'e', 'd', ' ', 'b', 'y', ' ', 'u', 'n', 'w', 'a', 'n', 't',
                 'e', 'd', ' ', 's', 'o', 'u', 'r', 'c', 'e', 's', '.']
    message14 = ['I', 't', ' ', 'a', 'l', 'l', 'o', 'w', 's', ' ', 't', 'h', 'e', ' ', 'u', 's', 'e', 'r', ' ', 't',
                 'o', ' ', 't', 'o', ' ', 'e', 'n', 'c', 'o', 'd', 'e', ' ', 'a', 'n', 'd', ' ', 'd', 'e', 'c', 'o',
                 'd', 'e', ' ', 'a', 'n', 'y', ' ', 't', 'e', 'x', 't', ' ', 'w', 'i', 't', 'h', 'i', 'n', ' ', 't',
                 'h', 'e', ' ', 'c', 'o', 'n', 'f', 'i', 'n', 'e', 's', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'r',
                 'o', 'm', 'a', 'n', ' ', 'a', 'l', 'p', 'h', 'a', 'b', 'e', 't']
    message15 = ['(', 'w', 'i', 't', 'h', ' ', 't', 'h', 'e', ' ', 'e', 'x', 'c', 'l', 'u', 's', 'i', 'o', 'n', ' ',
                 'o', 'f', ' ', 'c', 'e', 'r', 't', 'a', 'i', 'n', ' ', 'a', 'c', 'c', 'e', 'n', 't', ' ', 'm', 'a',
                 'r', 'k', 's', ' ', 'a', 'n', 'd', ' ', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's', ' ', 'o',
                 'u', 't', 's', 'i', 'd', 'e', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'E', 'n', 'g', 'l', 'i', 's',
                 'h', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', ')', '.']
    message16 = ['T', 'h', 'e', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', 'i', 's', ' ', 'l', 'i', 'm', 'i', 't',
                 'e', 'd', ' ', 'b', 'y', ' ', 'p', 'r', 'o', 'c', 'e', 's', 's', 'i', 'n', 'g', ' ', 'c', 'a', 'p',
                 'a', 'c', 'i', 't', 'y', ',']
    message17 = ['b', 'u', 't', ' ', 't', 'h', 'e', ' ', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n', ' ', 'o', 'p', 'e',
                 'r', 'a', 't', 'e', 's', ' ', 'f', 'u', 'l', 'l', 'y', ' ', 'o', 'n', ' ', 't', 'e', 'x', 't', ' ',
                 'b', 'a', 's', 'e', 'd', ' ', 'm', 'e', 's', 's', 'a', 'g', 'e', 's']
    message18 = ['(', 'l', 'i', 'm', 'i', 't', ' ', 'i', 's', ' ', 'c', 'u', 'r', 'r', 'e', 'n', 't', 'l', 'y', ' ',
                 's', 'e', 't', ' ', 'a', 't', ' ', 'a', 'b', 'o', 'u', 't', ' ', 'a', ' ', 'p', 'a', 'g', 'e', ' ',
                 'w', 'o', 'r', 't', 'h', ' ', 'o', 'f', ' ', 'w', 'r', 'i', 't', 'i', 'n', 'g', '.']
    message19 = ['i', 'f', ' ', 'e', 'n', 'c', 'r', 'y', 'p', 't', 'i', 'o', 'n', ' ', 'p', 'r', 'o', 'c', 'e', 's',
                 's', ' ', 'i', 's', ' ', 'f', 'a', 'i', 'l', 'i', 'n', 'g', ',', ' ', 't', 'r', 'y', ' ', 'e', 'n',
                 'c', 'r', 'y', 'p', 't', 'i', 'n', 'g', ' ', 't', 'h', 'e', ' ', 't', 'e', 'x', 't', ' ', 'i', 'n',
                 ' ', 's', 'm', 'a', 'l', 'l', 'e', 'r', ' ', 'p', 'o', 'r', 't', 'i', 'o', 'n', 's', ')', '.']
    message20 = ['T', 'h', 'e', ' ', 'h', 'o', 'p', 'e', ' ', 'i', 's', ' ', 't', 'h', 'a', 't', ' ', 's', 'o', 'm',
                 'e', ' ', 't', 'i', 'm', 'e', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'f', 'u', 't', 'u', 'r', 'e',
                 ',', ' ', 't', 'h', 'i', 's', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', 'w', 'i', 'l', 'l', ' ',
                 'b', 'e', ' ', 'u', 's', 'e', 'f', 'u', 'l']
    message21 = ['f', 'o', 'r', ' ', 's', 't', 'o', 'r', 'i', 'n', 'g', ' ', 'p', 'e', 'r', 's', 'o', 'n', 'a', 'l',
                 ' ', 'f', 'i', 'l', 'e', 's', ' ', 'a', 'n', 'd', ' ', 'p', 'r', 'o', 't', 'e', 'c', 't', 'i', 'n',
                 'g', ' ', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n']
    message22 = ['f', 'r', 'o', 'm', ' ', 'o', 't', 'h', 'e', 'r', 's', ' ', 'o', 'n', ' ', 't', 'h', 'e', ' ', 'i',
                 'n', 't', 'e', 'r', 'n', 'e', 't', ' ', 'a', 'n', 'd', ' ', 'o', 'n', ' ', 't', 'h', 'e', ' ', 's',
                 'a', 'm', 'e', ' ', 'W', 'i', 'F', 'i', '.']
    print("")
    time.sleep(.5)
    wait = "off"
    for i in message12:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message13:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message14:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message15:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    wait = "off"
    for i in message16:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message17:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message18:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message19:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message20:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message21:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"

    print("")
    time.sleep(.5)
    wait = "off"
    for i in message22:
        if wait == "on":
            time.sleep(.015)
            print(i, end="")
            wait = "off"
        else:
            print(i, end="")
            wait = "on"
    print("\n")

dict_of_code = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 11,
    " ": 12,
    "a": 13,
    "b": 14,
    "c": 15,
    "d": 16,
    "e": 17,
    "f": 18,
    "g": 19,
    "h": 21,
    "i": 22,
    "j": 23,
    "k": 24,
    "l": 25,
    "m": 26,
    "n": 27,
    "o": 28,
    "p": 29,
    "q": 31,
    "r": 32,
    "s": 33,
    "t": 34,
    "u": 35,
    "v": 36,
    "w": 37,
    "x": 38,
    "y": 39,
    "z": 41,
    "A": 42,
    "B": 43,
    "C": 44,
    "D": 45,
    "E": 46,
    "F": 47,
    "G": 48,
    "H": 49,
    "I": 51,
    "J": 52,
    "K": 53,
    "L": 54,
    "M": 55,
    "N": 56,
    "O": 57,
    "P": 58,
    "Q": 59,
    "R": 61,
    "S": 62,
    "T": 63,
    "U": 64,
    "V": 65,
    "W": 66,
    "X": 67,
    "Y": 68,
    "Z": 69,
    ".": 71,
    ",": 72,
    "!": 73,
    "?": 74,
    "_": 75,
    "\'": 76,
    "\"": 77,
    "/": 78,
    "^": 79,
    "$": 81,
    "#": 82,
    "@": 83,
    "%": 84,
    "&": 85,
    "*": 86,
    "(": 87,
    ")": 88,
    "{": 89,
    "}": 91,
    "[": 92,
    "]": 93,
    "\n": 94,
    "\t": 95,
    "\\": 96,
    ":": 97,
    ";": 98,
    "<": 99,
    ">": 111,
    "=": 112,
    "+": 113,
    "-": 114,
}

dict_int_code = {
    "1": 9,
    "2": 8,
    "3": 7,
    "4": 6,
    "5": 4,
    "6": 5,
    "7": 3,
    "8": 2,
    "9": 1,
    "0": 42
}

runs = 0
end = False
re_attempt = 1
random_code1 = False
while end == False:
    if random_code1 == True:
        runs = 0
        re_attempt = 0
        time.sleep(1)
        random_code1 = False
    if runs < 1:
        if re_attempt < 1:
            def is_integer_num(code):
                if isinstance(code, int):
                    return True
                if isinstance(code, float):
                    return code.is_integer()
                return False


            code = ()
            attempt = is_integer_num(code)
            while attempt == False:
                print("\n(Encryptor Code Is Determined By User And Can Be Changed Later)")
                code9 = input("\nEnter Encryptor Code: \n")
                if isinstance(code, str) is True:
                    try:
                        int(code9)


                        def spl_it(code9):
                            return [char for char in code9]


                        code7_length = len(code9)
                        code9 = spl_it(code9)
                        trials7 = 1
                        code8 = []
                        code = ""
                        while trials7 <= code7_length:
                            code8.append(dict_int_code.get(code9[trials7 - 1]))
                            code = code + str(code8[trials7 - 1])
                            trials7 += 1
                        code = int(code)
                        break
                    except ValueError:
                        def spl_it(code9):
                            return [char for char in code9]


                        code7_length = len(code9)
                        code9 = spl_it(code9)
                        trials7 = 1
                        code8 = []
                        code = ""
                        while trials7 <= code7_length:
                            code8.append(dict_of_code.get(code9[trials7 - 1]))
                            code = code + str(code8[trials7 - 1])
                            trials7 += 1
                        code = int(code)
                        break
                else:
                    def spl_it(code9):
                        return [char for char in code9]


                    code7_length = len(code9)
                    code9 = spl_it(code9)
                    trials7 = 1
                    code8 = []
                    code = ""
                    while trials7 <= code7_length:
                        code8.append(dict_of_code.get(code9[trials7 - 1]))
                        code = code + str(code8[trials7 - 1])
                        trials7 += 1
                    code = int(code)
                    break
            code = str(code)
            code2 = str(code)

            print("\n1: Encrypt ")
            print("2: Decrypt ")
            print("3: Quit Program ")
            print("4: Re-Enter Encryptor Code ")
            if als == True:
                print("5: Turn Analysis Off")
                dat1 = "1"
            else:
                print("5: Turn Analysis On")
                dat1 = "2"
            print("6: Bored Co. Black Jack")
            print("7: Mission Statement")
            choice = input("Select Action Type: \n")
            runs += 1
            if choice == "1":
                print("")
                encrypt(code)
                re_attempt += 1
                runs += 1
            elif choice == "2":
                print("")
                decrypt(code2)
                runs += 1
                re_attempt += 1
            elif choice == "3":
                runs += 1
                re_attempt += 1
                end = True
                break
            elif choice == "4":
                runs = 0
                re_attempt = 0
            elif choice == "5":
                if dat1 == "1":
                    als = False
                elif dat1 == "2":
                    als = True
                else:
                    "Error In Analysis Activation"
            elif choice == "6":
                BlackJack()
            elif choice == "7":
                mission_statement()
            else:
                print("Invalid Selection\n")
        else:
            print("1: Encrypt ")
            print("2: Decrypt ")
            print("3: Quit Program ")
            print("4: Bored Co. Black Jack")
            print("5: Mission Statement")
            choice = input("Select Action Type: \n")
            runs += 1


            def is_integer_num(code):
                if isinstance(code, int):
                    return True
                if isinstance(code, float):
                    return code.is_integer()
                return False


            code = ()
            attempt = is_integer_num(code)
            while attempt == False:
                if runs == 1:
                    if choice == "3":
                        break
                    if choice == "4" or choice == "5":
                        code9 = "random_code"
                        random_code1 = True
                    else:
                        print("\n(Encryptor Code Is Determined By User And Can Be Changed Later)")
                        code9 = input("\nEnter Encryptor Code: \n")
                else:
                    print("\n(Encryptor Code Is Determined By User And Can Be Changed Later)")
                    code9 = input("\nEnter Encryptor Code: \n")
                if isinstance(code, str) is True:
                    try:
                        int(code9)


                        def spl_it(code9):
                            return [char for char in code9]


                        code7_length = len(code9)
                        code9 = spl_it(code9)
                        trials7 = 1
                        code8 = []
                        code = ""
                        while trials7 <= code7_length:
                            code8.append(dict_int_code.get(code9[trials7 - 1]))
                            code = code + str(code8[trials7 - 1])
                            trials7 += 1
                        code = int(code)
                        break
                    except ValueError:
                        def spl_it(code9):
                            return [char for char in code9]


                        code7_length = len(code9)
                        code9 = spl_it(code9)
                        trials7 = 1
                        code8 = []
                        code = ""
                        while trials7 <= code7_length:
                            code8.append(dict_of_code.get(code9[trials7 - 1]))
                            code = code + str(code8[trials7 - 1])
                            trials7 += 1
                        code = int(code)
                        break
                else:
                    def spl_it(code9):
                        return [char for char in code9]


                    code7_length = len(code9)
                    code9 = spl_it(code9)
                    trials7 = 1
                    code8 = []
                    code = ""
                    while trials7 <= code7_length:
                        code8.append(dict_of_code.get(code9[trials7 - 1]))
                        code = code + str(code8[trials7 - 1])
                        trials7 += 1
                    code = int(code)
                    break
            code = str(code)
            code2 = str(code)
            if choice == "1":
                print("")
                encrypt(code)
            elif choice == "2":
                print("")
                decrypt(code2)
            elif choice == "3":
                end = True
                break
            elif choice == "4":
                BlackJack()
            elif choice == "5":
                mission_statement()
            else:
                print("Invalid Selection\n")
    else:
        print("\n1: Encrypt ")
        print("2: Decrypt ")
        print("3: Quit Program ")
        print("4: Re-Enter Encryptor Code")
        if als == True:
            print("5: Turn Analysis Off")
            dat1 = "1"
        else:
            print("5: Turn Analysis On")
            dat1 = "2"
        print("6: Bored Co. Black Jack")
        print("7: Mission Statement")
        choice = input("Select Action Type: \n")
        runs += 1
        if choice == "1":
            print("")
            encrypt(code)
        elif choice == "2":
            print("")
            decrypt(code2)
        elif choice == "3":
            end = True
            break
        elif choice == "4":
            runs = 0
            re_attempt = 0
        elif choice == "5":
            if dat1 == "1":
                als = False
            elif dat1 == "2":
                als = True
            else:
                print("\nError In Analysis Activation/Deactivation\n")
        elif choice == "6":
            BlackJack()
        elif choice == "7":
            mission_statement()
        else:
            print("Invalid Selection\n")

time13 = time.perf_counter()
def time_elapsed(time13):
    time13 = float(time13)
    days = time13 / 86400
    days = int(days)
    days_sec = 86400 * int(days)
    hours1 = time13 - float(days_sec)
    hours = hours1 / 3600
    hours = int(hours)
    hours_sec = 3600 * int(hours)
    minutes = time13 - (int(days_sec) + int(hours_sec))
    minutes = minutes / 60
    minutes = int(minutes)
    minutes_sec = 60 * int(minutes)
    seconds = time13 - (int(days_sec) + int(hours_sec) + int(minutes_sec))
    seconds = round(seconds, 2)
    return days, hours, minutes, seconds


if float(time13) >= 86400:
    days, hours, minutes, seconds = time_elapsed(time13)
    print("\n Time Elapsed = \n")
    print(" Days: " + str(days) + "  Hours: " + str(hours) + "  Minutes: " + str(minutes) + "  Seconds: " + str(seconds))
elif float(time13) >= 3600:
    days, hours, minutes, seconds = time_elapsed(time13)
    print("\n Time Elapsed = \n")
    print(" Hours: " + str(hours) + "  Minutes: " + str(minutes) + "  Seconds: " + str(seconds) + "\n")
elif float(time13) >= 60:
    days, hours, minutes, seconds = time_elapsed(time13)
    print("\n Time Elapsed: \n")
    print(" " + str(minutes) + ":" + str(seconds) + " (Min:Sec)")
else:
    print("\n Time Elapsed: " + str(time13) + " Seconds")
time.sleep(.5)
print("\n Program Terminated, Have A Nice Day! ")