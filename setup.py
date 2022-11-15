from setuptools import setup, find_packages

setup(
    name='LiveCaptionLinux',
    version='1.0',
    description='Live Captions in Linux for Discord, Telegram, Google Meet, Slack, Skype etc.',
    url='https://github.com/RonyMacfly/LiveCaptionLinux',
    author='Rony Macfly',
    author_email='rony.macfly@gmail.com',
    packages=find_packages(),
    package_data = {
        '': ['*'],
    },
    include_package_data=True,
    install_requires=['pyaudio',],
    entry_points={
        'console_scripts': [
            'LiveCaptionLinux = LiveCaptionLinux.__main__:init',
        ],
    },
)
