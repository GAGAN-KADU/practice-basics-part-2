def twodlist():
    list_l1 = [[1,2,3],[4,5,6],[7,8,9]]
    list_l2 =[]


    for i in list_l1:
        #print(i)
        #print(type(i))

        for j in i:
            list_l2.append(j)
    print(list_l2)

def sqr():
    Numbers = [1,2,3,4,5]

    new_dict = {}

    for i in Numbers:
        new_dict[i] = i*i

    print(new_dict)
        

        
#sqr()      

def duplicate():
    list1 = [0,0,0,1,1,2,2,3,3,4]
    list2 = []
    print(len(list1))
    cnt1 = 0
    cnt2 = 1

    while cnt1 <= 11:
            print(cnt1)
            if (list1[cnt1] not in list2):
                list2.append(list1[cnt1])
                #cnt1 = cnt2
                cnt1 += 1
            else:
                cnt1 += 1

    print(list2)

#duplicate()

def common_dict():
    dict1 = {"a":1,"b":2,"c":3,"d":4}
    dict2 = {"e":1,"a":6,"g":8,"h":4}
    dict3 = {}
    list1 = []

    for i in dict1:
       if i in dict2:
           list1.append(dict1[i])
           list1.append(dict2[i])
           dict2[i] = list1
        
    a = {**dict1,**dict2}
    print(a)


#common_dict()

def reversestr():
    str1 = "ab-=cd"
    list1 = list(str1)
    print(list1)



    cnt1 = 0
    a = len(str1)

    cnt2 = a-1 # 4

    while cnt1<=cnt2:

        print("cnt1---",cnt1)
        print("cnt2---",cnt2)


        if list1[cnt1].isalpha() and list1[cnt2].isalpha():
            list1[cnt1],list1[cnt2] = list1[cnt2],list1[cnt1]

            cnt1 +=1 
            cnt2 -=1

    print(list1)
#reversestr()




def tuple_dict():
    a  = [(1,2),(2,3)]
    dict1 = {}
    for i,j in a:
        print(i)
        dict1[i] = j
    print(dict1)

#tuple_dict()


def capletcount():
# count of capital letters

    str1 = ['I','AM','GagaN',123]
    cnt = 0
    for i in str1:
        #print(i)
        if isinstance(i,str):
            for j in i:
                if j.isupper():
                    cnt += 1
    print(cnt)

#capletcount()

# list = [12,24,42,12 ,24 ,] -  tell the count of reoccurance of elements
# str = 'aaaabbbaabbaabaab' count of elements 

a = "(2+3-4)"


def practice1():
    # list1 = sorted([24,42,12,12,24,24])
    list1 = [24,42,12,12,24,24]
    list1.sort()
    print(list1)

    cnt = 0
    d1 = {}

    #[12, 12, 24, 24, 24, 42]
    temp = list1[0]
    for i in list1:
        if i==temp:
            cnt+=1
        else:
            temp=i
            cnt=1
        d1[temp]=cnt
    print(d1)
    

#practice1()


def practice2():
    a = "gagannr"
    l1 = list(a)
    l1.sort()
    print(l1)
    i = 0
    cnt = 0
    d1 = {}
    print(a)
    
   # ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'a', 'a', 'b', 'b', 'a', 'a', 'b', 'a', 'a', 'b']
   # len = 17

    temp = l1[0]
    print("initial value of i",i)
    for i in l1:
        print(i)
        if i == temp:
            cnt += 1
            print(cnt)
            d1[i] = cnt

        else:
            temp = i
            cnt = 1

    #print(i)
    print(d1)
#practice2()

def practice3():
    l1 = ['mike','gagan','gaurav','santosh','aman']
    l2 = sorted(l1,key=len)
    print(l2)
#practice3()

def practice4():
    l1 = [12,11,21,22,112,12,11,23,23,43,12,23,43]

    # [11, 11, 12, 12, 12, 21, 22, 23, 23, 23, 43, 43, 112]

    '''
    to find most common element of the string
    1 ) sort all the tntegers
    2 ) arrange them in dict with key as intefer and value as count
    3) find the element with highest count

    '''
    l1.sort()
    print(l1)

    curr_cnt = 0
    prev_cnt = 0
    curr_temp = l1[0]
    prev_temp = l1[0]

    for i in l1:
        print("value of i ",i)
        if prev_cnt <= curr_cnt:
            if curr_temp==i:
                curr_cnt+=1
                print(curr_temp)
                print("current count",curr_cnt)

            else:
                prev_temp = curr_temp
                prev_cnt= curr_cnt
                curr_cnt = 1
        else:
            print(curr_cnt)
#practice4()

def practice5():
    l1 = [('gagan',23),('mike',44),('aman',32)]
    d = sorted(l1, key=lambda x: x[1], reverse=True)
    s = {y:x for x,y in l1}
    print(s[max(s.keys())])
    # print(s)
    # print(d[0])
    # for i,j, in l1:
    #     print (i,j)

#practice5()


def practice6():
    #Write a Python function that takes a list of integers as input and returns
    #the count of negative numbers, zero, and positive numbers in the list as a dictionary.

    l1 = [-1,-3,-2,0,0,1,23,4,5]
    positive_cnt = 0
    negative_cnt = 0
    zero_cnt = 0
    d1= {}
    for i in l1:
        if i<0:
            negative_cnt += 1
        elif i == 0:
            zero_cnt += 1
        else:
            positive_cnt +=1 
        d1['negative'] = negative_cnt
        d1['zero'] = zero_cnt
        d1['positive_cnt'] = positive_cnt
    print(d1)
#practice6()

def practice7():

    l1 = ['mike','gagan','bhola','raj']
    d1 = {}
    for i in l1:
        d1[i]=len(i)
    print(d1)
#practice7()

def practice8():
    l1 = [1,2,23,34,54,21,87]
    d1 = {}
    for i ,item in enumerate(l1):
        d1[item]=i
    print(d1)
        
#practice8()

def practice9():

    l1 =[("abc",11),("gfg",23),("pqr",5),("cd",2),("ab",22)]
    d2 ={}
    l2 = [] 
    l3 = []
    l4 = []

    for i,j in l1:
        if j>=0 and j<= 10:
            print(i)
            l2.append(i)
            d2["0-10"] = l2
        elif j>=11 and j<= 20:
            l3.append(i)
            d2["11-20"] = l3
        else :
            l4.append(i)
            d2["21-30"] = l4

    print(d2)


#practice9()

def practice10():

    l1 = ['abcd','pqre','stuv','ahgd','khha','ejvyvu','out','uspe']
    a1 = []
    e = []
    i = []
    o = []
    u = []
    d1 = {}

    for i in l1:
        #print(i)
        if i[0] == 'a':
            a1.append(i)
            d1["a"]=a1
        elif i[0] == 'e':
            e.append(i)
            d1["e"]=e
        elif i[0] == 'i':
            i.append(i)
            d1["i"]=i
        elif i[0] == 'o':
            o.append(i)
            d1["o"]=o
        elif i[0] == 'u':
            u.append(i)
            d1["u"]=u
        else:
            print("no vowels ",i)

    print(d1)
#practice10()

def practice11():

    l1 = ['abcd','pqre','stuv','ahgd','khha','ejvyvu','out','uspe']
    l2 = []
    for i in l1:
        x = len(i)
        l2.append(x)
    l2.sort()

    print(l2)
#practice11()

def practice12():

    l1 = [10,10,12,23,24,35,23,54,46,67,44,90,44,90]
    l1.sort()
    d1 = {}
    cnt = 0
    temp=l1[0]


    for i in l1:
        if i % 2 == 0:
            if i == temp:
                cnt += 1
            else:
                temp = i
                cnt = 1
            d1[i] = cnt
        else:
            continue

    print(d1) 
#practice12()

def practice13():

    s = "abcba"
    cnt = 0
    rev_cnt = len(s)-1

    while True:
        print(cnt, rev_cnt)
        if s[cnt] == s[rev_cnt]:
            cnt += 1
            rev_cnt -= 1
            if cnt==rev_cnt:
                print("string is palindrome")
                break
        elif s[cnt] != s[rev_cnt]:
            print("string is not palindrome")
            break
#practice13()
            

def practice14():
    s = "asdfgh"
    b = "hdfsgaq"

    l1= [i for i in s]
    for i in b:
        if i in l1:
            print("i present in s")
        else:
            print("not a anagram")
            break
    #print(l1)

#practice14()

def practice15():
    s1 = "6573"
    s2 = " "
    s3 = ""

    for ele in s1:
        s3 = ele + s2 +s3
    print(s3)
#practice15()

def practice16():
    l1= [2,3,5,7]
    for num in range(3,50):
        if ((num % 2 == 0 ) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0) or (num % 11 == 0)):
            print("number is not prime")
        else:
            l1.append(num)
    print(l1)
practice16()

    












    














            

            




       