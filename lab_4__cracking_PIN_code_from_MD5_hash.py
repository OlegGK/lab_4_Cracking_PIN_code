# lab 4 - cracking PIN code with MD5 hashes
import hashlib
import time

# test_password = "password123" - password that we don't known

# we know only MD5 hash string
test_pass_md5_hash = "482c811da5d5b4bc6d497ffa98491e38"  

def get_md5_hash(string = 'test'):
	md5_hash = hashlib.md5(string.encode())
	return md5_hash.hexdigest()

def change_digit_in_number(list_of_numbers = [0], min_num = 0, max_num = 1):
	for i in range(len(list_of_numbers)):
		if list_of_numbers[i:] == [max_num for _ in range(len(list_of_numbers[i:]))]:
			list_of_numbers[i - 1] += 1
			list_of_numbers[i:] = [min_num for _ in range(len(list_of_numbers[i:]))]
			return list_of_numbers

def all_digit_max(list_of_numbers = [0], max_num = 1):
	for number in list_of_numbers:
		if number != max_num:
			return False

	# answer = input("All digit is max, continue?")
	# if answer == 'y':
	return True

def set_all_min_digit_in_number(list_of_numbers = [0], min_num = 0):
	return [min_num for num in range(len(list_of_numbers))]


# ASCII codes range - [32, 126]
def crack_PIN_code(pass_md5_hash = 'a'):
	temp_symbols_combination = [0]
	temp_str = ''
	while True:
		if all_digit_max(temp_symbols_combination, 119):
			# answer = input("All digit is max, continue?")
			temp_symbols_combination = set_all_min_digit_in_number(temp_symbols_combination, 97)
			temp_symbols_combination.append(0)  # збільшуємо порядок числа
			print('Length of password:', len(temp_symbols_combination))
		
		for code in range(97, 119 + 1):
			temp_symbols_combination[-1] = code
			temp_str = ''.join([chr(number) for number in temp_symbols_combination])
			if len(temp_str) == 5:
				print(temp_str)
			if get_md5_hash(temp_str) == pass_md5_hash:
				return temp_str

		if not all_digit_max(temp_symbols_combination, 119):
			change_digit_in_number(temp_symbols_combination, 97, 119)


# test_word_easy = 'passw'
# md5_hash = get_md5_hash(test_word_easy)
# print(md5_hash)

# md5_hash_str_easy = 'cd0acfe085eeb0f874391fb9b8009bed' # for password - 'pas' - 1.5s
md5_hash_str_easy = '1a1dc91c907325c69271ddf0c944bc72' # for password - 'pass' - 140s

start_time = time.time()
# print('Start execution time:', start_time)

clear_password = crack_PIN_code(md5_hash_str_easy)
print('Crack password is:', clear_password)

end_time = time.time()
# print('End execution time:', end_time)

execution_time = round(end_time - start_time, 3)
print('Time of program execution: {0}s'.format(execution_time))











