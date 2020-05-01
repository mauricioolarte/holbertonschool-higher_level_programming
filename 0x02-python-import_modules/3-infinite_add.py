#!/usr/bin/python3
def main():
    sum = 0
    numberarguments = len(sys.argv)
    for i in range(1, numberarguments):
        sum += int(sys.argv[i])
    print('{}'.format(sum))

if __name__ == '__main__':
    import sys
    main()
