import numpy as np
import cv2, argparse

def convert(vid_path, target_folder):
	if not target_folder.endswith('/'):
		target_folder += '/'

	i = 1
	cap = cv2.VideoCapture(vid_path)
	while cap.isOpened():
		ret, frame = cap.read()
		if ret is True:
			cv2.imwrite('{}frame_{}.png'.format(target_folder, i), frame)
			i += 1

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--src_file', help="video path", type=str, default='')
	parser.add_argument('--target_folder', help="target folder to store images", type=str, default='')
	
	args = parser.parse_args()
	src_file = args.src_file
	target_folder = args.target_folder

	convert(src_file, target_folder)