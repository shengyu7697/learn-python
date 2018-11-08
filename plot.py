#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from scipy import signal
import matplotlib.pyplot as plt

def main():
	time = [1, 2, 3, 4]
	data = [1, 4, 9, 16]
	plt.plot(time, data, label='x')
	plt.xlabel('time [second]')
	plt.grid()
	plt.legend()
	plt.show()

	pass

if __name__ == '__main__':
    main()