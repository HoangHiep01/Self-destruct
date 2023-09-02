import os
import shutil
from datetime import datetime, timedelta

def remove_dir(path):
	if os.path.isdir(path):
		shutil.rmtree(path)
		print(f'{path} has been deleted.')

def remove_empty_dir(path):
	try:
		if os.path.isdir(path):
			os.rmdir(path)
			print(f'{path} has been deleted.')
	except OSError as error:
		print(error)
	finally:
		print("Try remove the tree.")
		remove_dir(path)

def remove_file(path):
	if os.path.isfile(path):
		os.remove(path)
		print(f'{path} has been deleted.')


def remove_list_dir(list_dir="setting/dirs.txt"):
	with open(list_dir, 'r') as file:
		paths = file.readlines()

	for path in paths:
		remove_dir(path)

def remove_list_file(list_file="setting/files.txt"):
	with open(list_file, 'r') as file:
		paths = file.readlines()

	for path in paths:
		remove_file(path)

def remove_list_empty_dir(list_empty_dir="setting/emptydirs.txt"):
	with open(list_empty_dir, 'r') as file:
		paths = file.readlines()

	for path in paths:
		remove_empty_dir(path)


def remove():
	remove_list_dir()
	remove_list_empty_dir()
	remove_list_file()


def check_time():

	with open('setting/time.txt', 'r') as file:
		pivot = file.readline()

	past = datetime.strptime(pivot, "%H:%M:%S %d/%m/%Y")
	now = datetime.now()
	# print(past+timedelta(days=14), now, sep="\n")

	# Nếu thời gian hiện tại vượt quá 14 ngày kể từ điểm lưu trữ thì xóa
	if now > past + timedelta(days=14):
		# remove()
		print("Out time.")
	else:
		print("In time.")
		with open('setting/time.txt', 'w') as file:
			file.write(now.strftime("%H:%M:%S %d/%m/%Y"))

if __name__ == "__main__":

	# with open('setting/time.txt', 'w') as file:
	# 	file.write(datetime.now().strftime("%H:%M:%S %d/%m/%Y"))
	# print(datetime.now())

	check_time()
