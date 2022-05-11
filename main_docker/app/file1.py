from file2 import fake_data
import time,argparse


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--data')
	args = parser.parse_args()
	print('--Data: ',args.data)
	for i in range(5):
		print(f'Data: {fake_data()}')
		time.sleep(5)
