# Modify the kebabize function so that it converts a camel case string into a kebab case.

# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-humps

# Notes:

#     the returned string should only contain lowercase letters



def kebabize(string):
    res = ''
    for i in string:
        if i.isupper():
            if res != '':
                res += '-'
        if i.isdigit() == False:
            res += i.lower()
        print(res)
    return res