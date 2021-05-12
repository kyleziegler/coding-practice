# Kyle Ziegler 2021
# Prints all string permutations


def main(s:str, index:int) -> list:
    if (index == len(s)):
        # End case
        print ("".join(s))

    copy = list(s)
    for i in range(index, len(s)):
        print("Loop index",i,"function index",index)
        

        # Swap characters, and increase the index
        copy[index], copy[i] = copy[i], copy[index]
        # print("main(",copy,index+1,")")
        main(copy,index+1)

main("abc",0)
