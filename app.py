# imports from moduls
from tools.numbers.simp import add , subtract 
from tools.numbers.comp import sumofdigits , ispal
from tools.col import myzip
from icecream import ic

# TEST page to all functions

# lists to myzip 
it1 = ['a' , 'b' , 'c']
it2 = [1 , 2 , 3]


# main function
def main():
    # add
    print(add(2,3))
    # subtract
    print(subtract(8,1))
    # sum
    print(sumofdigits(245))
    # ispal true
    print(ispal(15251))
    # ispal false
    print(ispal(1234))
    # myzip
    ic(myzip(it1 , it2))
    
    
if __name__ == '__main__':
    main()