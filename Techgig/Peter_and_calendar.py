'''
    Problem Statement : Petr and a calendar
    Link : https://www.techgig.com/practice/question/petr-and-a-calendar/QkpZWWdSQk9lWFRNeG1wRFo1Ry9xL2VPd0drRExiSHZFUnJ0b3FiOFFTaHZrMndmdElobTZnWFJSL2FyQWhyVw==/1
    acore : accepted
'''
def main():

    from calendar import monthrange
    m = int(input())
    d = int(input())

    days = monthrange(2017,m)[1]
    weeks = 1
    days = days-((7-d)+1)
    weeks = weeks + (days//7)
    days = days%7
    if days:
        weeks += 1
    print(weeks,end='') 

if __name__ == '__main__':
    main()

