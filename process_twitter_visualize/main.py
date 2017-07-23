#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import argparse


def parse_args():
	"""
	Parse arguments Method
	:return: 
	"""
	parser = argparse.ArgumentParser(description='<usage> python main.py -k <KEYWORD>')
	parser.add_argument('--keyword', '-k', action='store', default='pyspark',
						help='<usage> python main.py -k <KEYWORD>')
	arguments, _ = parser.parse_known_args()
	return arguments


if __name__ == '__main__':
	args = parse_args()
	keyword = args.keyword
	print(keyword)
