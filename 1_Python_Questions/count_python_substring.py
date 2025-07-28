def count_substring(string, sub_string):
    occurence_lst = 0
    for i in range(0, len(string)):
        if sub_string == string[i:i + len(sub_string)]:
            occurence_lst += 1
    return occurence_lst


if __name__ == '__main__':
    string = "ThIsisCoNfUsInG"
    sub_string = "is"

    count = count_substring(string, sub_string)
    print(count)

# divide string into substring of length 3
lst = []
count = 0
string = "ABCDCDC"
for i in range(0, len(string), 3):
    lst.append(string[i:i + 3])
print(lst)
