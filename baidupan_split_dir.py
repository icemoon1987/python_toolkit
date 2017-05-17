import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import shutil
import time
from datetime import datetime, timedelta

def print_help():
	print "USAGE: python baidupan_split_dir.py SRC_DIR DST_DIR"
	return

def load_src_dir(dir_path):
	dir_list = os.listdir(dir_path)

	result = {}

	for dir_name in dir_list:
		try:
			src_dir = os.listdir(dir_path + "/" + dir_name)[0]
			file_list = os.listdir(dir_path + "/" + dir_name + "/" + src_dir)

			result[dir_name] = []
			for file_name in file_list:
				result[dir_name].append(dir_path + "/" + dir_name + "/" + src_dir + "/" + file_name)

			result[dir_name].sort()

			#for sub_dir in sub_dirs:
				#print sub_dir
		except Exception, ex:
			print ex
			pass

	return result


def save_dst_dir(file_map, dst_path, file_num_per_dir):

	if os.path.exists(dst_path):
		shutil.rmtree(dst_path)
	os.mkdir(dst_path)

	for dir_name in file_map:

		i = 0
		for src_file in file_map[dir_name]:
			dir_name_new = dir_name + "_" + str( i / file_num_per_dir )

			if not os.path.exists(dst_path + "/" + dir_name_new):
				os.mkdir(dst_path + "/" + dir_name_new)

			file_name = src_file.split("/")[-1]

			shutil.copy(src_file, dst_path + "/" + dir_name_new + "/" + file_name)

			i += 1
	return


def main():

	if len(sys.argv) < 3:
		print_help()
		return

	src_dir = sys.argv[1]
	dst_dir = sys.argv[2]

	file_map = load_src_dir(src_dir)

	save_dst_dir(file_map, dst_dir, 400)

	return

if __name__ == "__main__":
	main()

