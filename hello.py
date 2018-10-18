'''
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0~100!')
        self._score = value

s = Student()
s.set_score(60)
s.get_score()
s.set_score(999)  
'''
class Student(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration ()
        return self.a 

def now():
	print('2018-10-14')

def log(func):
	def wrapper(*arg, **kw):
		print('call %s()' % func.__name__)
		return func(*arg, **kw)
	return wrapper

def log1(text):
	def decorator(func):
		def wrapper(*arg, **kw):
			print('%s %s():' % (text, func.__name__))
			return func
		return wrapper
	return decorator

@log
def now():
	print('2018-10-14')
@log1
def now1():
	print('2018-10-15')


from functools import reduce

def prod(s2):
    def chengfa(s3, s4):
        return s3 * s4
    return reduce(chengfa, s2)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
