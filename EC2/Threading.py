import threading
import time
import math

__author__ = "Chinmay Rakshit"
__date__ = "2017-03-03"
__email__ = "chinmay.rakshit@gmail.com"


class CountdownTask(threading.Thread):
    def __init__(self,target):
        self._target=target
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._running = True

    def terminate(self):
        self._stopevent.set()

    def run(self):
        self._target()


class Threading(object):
	"""docstring for Threading"""

	def __init__(self,count):
		super(Threading, self).__init__()
		self.thread_dict = {}
		self.count = count
		self.thread_dict_size = 0

	"""
	function to decide the number of threads, return the instance of the class for function chaining
	"""
	def distribute_task(self,target, chunk_size):
		x = int(math.ceil((1.0 * self.count)/ chunk_size))
		self.thread_dict_size = x
		for i in range(0,x):
			self.thread_dict[i] = CountdownTask(target = target)	
			pass
		return self

	"""
	start all the threads, return the instance of the class for function chaining
	"""
	def start_thread(self):
		for i,value in self.thread_dict.iteritems():
			value.setDaemon(True)
			value.start()
			time.sleep(1)
			pass
		return self

	"""
	stop all the threads, return the instance of the class for function chaining
	"""
	def stop_thread(self):
		for i,value in self.thread_dict.iteritems():
			if value.isAlive():
				value.terminate()
				pass
			pass
		return self


"""
This class is specifically meant to test the Thread class and will be improved later
"""
class checking(object):

	def __init__(self):
		self.count = 100
		pass

	def check(self):
		
		x = self.count - 30 if self.count - 30 >= 0 else 0
		self.count -=30
		with open('temp.txt', 'a') as f:
			f.write(str(x)+"hooollllooooo"*1000+"end\n")
		pass

	def call(self):
		c = Threading(100).distribute_task(target = self.check, chunk_size = 30).start_thread()
		#print c.thread_dict_size
		time.sleep(10)
		c.stop_thread()

