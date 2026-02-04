
class Counter:
	
	def __init__(self):
		self.i_counter = 0
	
	def add(self,value):
		if isinstance(value,int):
			self.i_counter += value
			
	def get(self):
		return self.i_counter
		

c = Counter()
c.add(10)
c.add("abc")
c.add(5)
c.add(2.5)

print(c.get())   # 15

