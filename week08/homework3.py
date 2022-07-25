import time
'''
time.process_time()-->float
作用：返回性能计数器的值(以小数秒为单位)，
即具有最高可用分辨率来测量短时间的时钟。
它确实包括在睡眠期间所花费的时间，并且是全系统的。
'''
def timer(func):

	def wrapper():
        
		start_time = time.perf_counter()
		func()
		end_time = time.perf_counter()
		used_time = end_time - start_time
		print(f"用时：{used_time}秒")

	return wrapper

@timer
def test():
    print("hello")
    time.sleep(0.5)

test()