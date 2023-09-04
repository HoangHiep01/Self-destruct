import os
import shutil
import re
from datetime import datetime, timedelta

SETTING_PATH = "setting"
SCRIPT_PATH = ""

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


def remove_list_dir(list_dir=f"{SETTING_PATH}/dirs.txt"):
	with open(list_dir, 'r') as file:
		paths = file.readlines()

	for path in paths:
		print(path)
		remove_dir(path)

def remove_list_file(list_file=f"{SETTING_PATH}/files.txt"):
	with open(list_file, 'r') as file:
		paths = file.readlines()

	for path in paths:
		remove_file(path)

def remove_list_empty_dir(list_empty_dir=f"{SETTING_PATH}/emptydirs.txt"):
	with open(list_empty_dir, 'r') as file:
		paths = file.readlines()

	for path in paths:
		remove_empty_dir(path)

def handle_time_file(path, now=datetime.now()):
	# Nếu file không tồn tại
	if not os.path.exists(path):
		with open(path, 'w') as file:
			file.write(now.strftime("%H:%M:%S %d/%m/%Y"))
		return True
	else:
		# Nếu file tồn tại nhưng nội dung có vấn đề
		with open(path, 'r') as file:
			content = file.readline()
		pattern = "^[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1} [0-3]{1}[0-9]{1}/[0-1]{1}[0-9]{1}/[0-9]{4}$"
		if not re.match(pattern=pattern, string=content):
			with open(path, 'w') as file:
				file.write(now.strftime("%H:%M:%S %d/%m/%Y"))
			return True

	return False


def remove(self_destruct=True):
	remove_list_dir()
	remove_list_empty_dir()
	remove_list_file()

	if self_destruct is True:
		remove_dir(SETTING_PATH)
		remove_file(SCRIPT_PATH)



def check_time():

	now = datetime.now()
	time_path = f"{SETTING_PATH}/time.txt"
	# Nếu phải xử lý lại nội dung file time.txt thì không cần làm gì nữa

	if handle_time_file(path=time_path, now=now):
		return False


	with open(time_path, 'r') as file:
		pivot = file.readline()
	past = datetime.strptime(pivot, "%H:%M:%S %d/%m/%Y")
	# print(past+timedelta(days=14), now, sep="\n")

	# Nếu thời gian hiện tại vượt quá 14 ngày kể từ điểm lưu trữ thì xóa
	if now > past + timedelta(days=14):
		
		return True
	else:
		print(past + timedelta(days=14))
		with open(time_path, 'w') as file:
			file.write(now.strftime("%H:%M:%S %d/%m/%Y"))
		return False


if __name__ == "__main__":

	if check_time():
		remove(self_destruct=False)
	
