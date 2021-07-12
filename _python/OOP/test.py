def longestCommonPrefix(list_as_argument):
    print(list_as_argument)
    tail = ""
    for i in range(len(list_as_argument[0])):
        for s in list_as_argument[1::]:
            if len(s) <= i:
                return tail
            if s[i] != list_as_argument[0][i]:
                return tail
            else:
                tail += list_as_argument[0][i]
    return tail
longestCommonPrefix(["flower","flow","flight"])