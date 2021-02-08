class FunctionFind:
	def __init__(self, module, search): 
		self.search = search 
		self.module = module 

	def find(self): 
		counter = 0 
		print('='*50)
		print("SEARCH:\t", self.search)
		print("MODULE:\t", str(self.module.__name__))
		print('='*50)
		for x in dir(self.module):
			if x.find(self.search) != -1:
				counter +=1
				print(str(self.module.__name__)+'.'+x)
		print('='*50)
		print(f'{counter} function found!')
		print('='*50)

if __name__ == '__main__':
	from selenium import webdriver
	module = webdriver.chrome.options
	search = ''

	myClass = FunctionFind(module, search)
	myClass.find()
