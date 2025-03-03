
def read_line():
    filereademo = open("D:/Python course/Concepts/Basic/operation.py","r")
    for line in filereademo:
        print(line)
    filereademo.close()


def count_words():
    file = open("D:/Python course/Concepts/Basic/operation.py","r")
    count =0
    data = file.read()  # whole data
    words = data.split() # spliting with space=" "

    for word in words:
        count+=1
    print("Total words : ", count)
    file.close()


def upper_and_lower_words():
    file = open("D:/Python course/Concepts/Basic/operation.py","r")
    upCount =0
    lowerCount =0
    data = file.read() # whole data

    for letter in data:
        if letter.isupper():
            upCount+=1
        else:
            if letter.islower():
               lowerCount+=1
            
    print("Total upper case : ", upCount)
    print("Total upper case : ", lowerCount)
    file.close()


read_line()
count_words()
upper_and_lower_words()