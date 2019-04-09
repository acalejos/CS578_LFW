#!/usr/bin/env python
import sys
from split_pairs_XZ import split, format_filename


def main():
	train_file="../pairsDevTrain.txt"
	test_file= "../pairsDevTest.txt"
	(train_same, train_diff, vali_same, vali_diff, test_same, test_diff) = split(train_file, test_file)

if __name__ == '__main__':
	main()
