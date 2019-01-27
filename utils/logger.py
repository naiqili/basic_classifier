import os

from tensorboardX import SummaryWriter
from .miscs import *

__all__ = ['Logger']

class Logger(object):
    '''Logger based on tensorboard.'''
    def __init__(self, args): 
        #print('Logger initializing...')
        self.dir = os.path.join(args.exp_dir, args.time_str)
        self.filename = args.exp_filename
        mkdir(self.dir)
        fpath = os.path.join(self.dir, self.filename)
        if fpath is not None:
            self.file = open(fpath, 'w')
            
        self.train_writer = SummaryWriter(os.path.join(self.dir, 'train'))
        self.test_writer = SummaryWriter(os.path.join(self.dir, 'test'))
        
    def add_train(self, name, data, niter):
        self.train_writer.add_scalar(name, data, niter)
        
    def add_test(self, name, data, niter):
        self.test_writer.add_scalar(name, data, niter)
        
    def set_names(self, names):
        # initialize numbers as empty list
        self.numbers = {}
        self.names = names
        for _, name in enumerate(self.names):
            self.file.write(name)
            self.file.write('\t')
            self.numbers[name] = []
        self.file.write('\n')
        self.file.flush()
        
    def append(self, numbers):
        assert len(self.names) == len(numbers), 'Numbers do not match names'
        for index, num in enumerate(numbers):
            self.file.write("{0:.6f}".format(num))
            self.file.write('\t')
            self.numbers[self.names[index]].append(num)
        self.file.write('\n')
        self.file.flush()

    def close(self):
        if self.file is not None:
            self.file.close()
        self.train_writer.close()
        self.test_writer.close()