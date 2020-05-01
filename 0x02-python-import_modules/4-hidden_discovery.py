#!/usr/bin/python3
def main():
    hiden_names = dir(hidden_4)
    for i in range(0, len(hiden_names)):
        if hiden_names[i][0] != '_':
            print(hiden_names[i])
if __name__ == '__main__':
    import sys
    import hidden_4
    main()
