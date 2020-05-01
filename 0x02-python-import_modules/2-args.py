#!/usr/bin/python3
def main():
    numberarguments = len(sys.argv)
    if numberarguments == 2:
        argum_word = 'argument:'
    elif numberarguments == 1:
        argum_word = 'arguments.'
    else:
        argum_word = 'arguments:'
    print('{} {}'.format(numberarguments - 1, argum_word))
    for i in range(1, numberarguments):
        print('{}: {}'.format(i, sys.argv[i]))

if __name__ == '__main__':
    import sys
    main()
