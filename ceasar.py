#!/usr/bin/env python

from string import maketrans
import sys

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def Ceasar(s, iters):
	translats = []
	for i in iters:
		intab = 'abcdefghijklmnopqrstuvwxyz'
		outtab = intab[i:] + intab[0:i]
		transtab = maketrans(intab, outtab)
		string = ' '.join(s)
		translats.append(string.translate(transtab))
	return translats

if __name__ == '__main__':

	if RepresentsInt(sys.argv[-1]):
		iters = range(1,((int(sys.argv[-1])+1) % 26))
		print Ceasar(sys.argv[1:-1], iters)[-1]
	else:
		iters = range(26)
		print ', '.join(Ceasar(sys.argv[1:], iters))