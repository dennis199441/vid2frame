from setuptools import setup, find_packages

setup(
	name='vid2img',
	packages=find_packages(),
	description='Video-to-Images converter',
	version='0.0.1',
	url='https://github.com/dennis199441/pytalib',
	author='Dennis Cheung',
	author_email='dennis199441@gmail.com',
	install_requires=[
		'opencv-python',
		'numpy'
    ],
	keywords=['pip','dennis','vid2img']
)