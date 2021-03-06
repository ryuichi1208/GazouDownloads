# coding: utf-8
#!/usr/bin/env python

import commands
import datetime
import sys, os
import shutil

git_url = 'https://github.com/take-iwiw/AutoBuild.git'
scripts = [
	['scripts/build_pj1.sh', 'Project 1'],
	['scripts/build_pj2.sh', 'Project 2']
]
log_dir = ''
code_dir = ''

def get_source_code():
	global code_dir
	code_dir = './work'
	if len(sys.argv) > 1:
		code_dir = sys.argv[1]
	if os.path.exists(code_dir):
		shutil.rmtree(code_dir)
	commands.getoutput('git clone ' + git_url + ' ' + code_dir)

def create_log_dir():
	global log_dir
	log_dir = 'log_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	commands.getoutput('mkdir ' + log_dir)

def treat_result(result_message):
	print(result_message)
	# todo: send slack message

def run_all_build():
		if ret.count('[100%] Built'):
			print("  OK")
			result_message += script[1] + ': OK\n'
		else:
			print("  ERROR")
			result_message += script[1] + ': ERROR\n'
			result_message += '--- build log ---\n'
			result_message += ret
			result_message += '\n---------------\n\n'
	treat_result(result_message)

def main():
	global code_dir
	if len(sys.argv) > 2:
		code_dir = sys.argv[2]
	else:
		get_source_code()
	create_log_dir()
	run_all_build()
	if os.path.exists(code_dir):
		shutil.rmtree(code_dir)

if __name__ == '__main__':
	main()
