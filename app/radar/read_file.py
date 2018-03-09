
import csv,json
from collections import defaultdict

def read_file_main(fname):
	fdata = {}
	with open(fname,"r") as f:
		fheader = f.readline().lower().strip().split('\t')
		for line in f.readlines():
			line = line.strip().split('\t')
			# print(line)
			fdata[line[0]] = tuple(line[1:])
	return fheader, fdata

def get_list(fname):
	json_name = 'radar_temp.json'
	fheader, fdata = read_file_main(fname)
	final_list = {}
	temp_list = []
	fheader.remove('labels')
	final_list['legend']= fheader
	for i, fh in enumerate(fheader):
		inner_list = []
		for k in fdata.keys():
			inner_list.append({'axis': k, 'value': float(fdata[k][i])})
		temp_list.append(inner_list)
	final_list['data'] = temp_list
	return final_list
