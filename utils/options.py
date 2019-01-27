import argparse
import os
import socket
import time

com_name = socket.gethostname()
#print(com_name)

if com_name == 'Lenovo-PC':
    data_root = 'D:\\Lab\\dataset'
elif com_name == 'h404f-gpu02':
    data_root = "/home/naiqi/dataset/"
else:
    data_root = '~/dataset/'

parser = argparse.ArgumentParser(description='Basic classfier')

parser.add_argument('--data_root', type=str, default=data_root,
                    help='dataset directory')
                    

time_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) 
parser.add_argument('--time_str', type=str, default=time_str,
                    help='dataset directory')