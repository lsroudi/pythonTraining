#!/usr/bin/python

def main():
    a,b = 1,2
    print('valeur de a est {} a et de b est {} et ceci avant swap'.format(a,b))
    
    #swap function
    a,b = b,a
    print('valeur de a est {} a et de b est {} et ceci après swap'.format(a,b))
    
    c = (1,2,3,4,5)
    print('type de {} est {}'.format(c,type(c)))
    d = [1,2,3,4,5]
    print('type de {} est {}'.format(d,type(d)))
    
    for n in d:
        print(n)

if __name__ == "__main__" : main()
