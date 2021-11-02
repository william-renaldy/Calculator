import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from math import *

x=1
y=1

class mygrid(GridLayout):
	def __init__(self,**kwargs):
		super(mygrid,self).__init__(**kwargs)
		
		self.cols=1
		self.input=TextInput(text=' ',halign='right',font_size=102)
		self.add_widget(self.input)
		self.keypad=GridLayout(cols=6)
		self.add_widget(self.keypad)
		self.clear=Button(text='C')
		self.open_paranthesis=Button(text='(')
		self.close_paranthesis=Button(text=')')
		self.divide=Button(text='/')
		self.multiply=Button(text='×')
		self.add=Button(text='+')
		self.subtract=Button(text='-')
		self.dot=Button(text='.')
		self.equal=Button(text='=')
		self.power=Button(text='^')
		self.sqrt=Button(text='√')
		self.delete=Button(text='<--')
		self.sin=Button(text='sin')
		self.cos=Button(text='cos')
		self.tan=Button(text='tan')
		self.swap=Button(text='->\n<-')
		self.log=Button(text='log')
		self.ln=Button(text='ln')
		self.deg=Button(text='°')
		self.sinh=Button(text='sinh')
		self.cosh=Button(text='cosh')
		self.tanh=Button(text='tanh')
		self.floor=Button(text='|_  _|')
		self.percentage=Button(text='%')
		
		self.pi=Button(text='π')
		self.e=Button(text='e')
		
		
		self.num1=Button(text='1')
		self.num2=Button(text='2')
		self.num3=Button(text='3')
		self.num4=Button(text='4')
		self.num5=Button(text='5')
		self.num6=Button(text='6')
		self.num7=Button(text='7')
		self.num8=Button(text='8')
		self.num9=Button(text='9')
		self.num0=Button(text='0')
		
		self.clear.bind(on_press=self.clear_function)
		self.open_paranthesis.bind(on_press=lambda *args:self.calc(*args,'('))
		self.close_paranthesis.bind(on_press=lambda *args:self.calc(*args,')'))
		self.divide.bind(on_press=lambda *args:self.calc(*args,' / '))
		self.multiply.bind(on_press=lambda *args:self.calc(*args,' × '))
		self.subtract.bind(on_press=lambda *args:self.calc(*args,' - '))
		self.add.bind(on_press=lambda *args:self.calc(*args,' + '))
		self.power.bind(on_press=lambda *args:self.calc(*args,' ^ '))
		self.dot.bind(on_press=lambda *args:self.calc(*args,'.'))
		self.equal.bind(on_press=self.calculate)
		self.sqrt.bind(on_press=lambda *args: self.calc(*args,'√('))
		self.delete.bind(on_press=self.delete_last)
		
		self.sin.bind(on_press=lambda *args: self.calc(*args,self.sin.text+'('))
		self.cos.bind(on_press=lambda *args: self.calc(*args,self.cos.text+'('))
		self.tan.bind(on_press=lambda *args: self.calc(*args,self.tan.text+'('))
		self.sinh.bind(on_press=lambda *args: self.calc(*args,self.sinh.text+'('))
		self.cosh.bind(on_press=lambda *args: self.calc(*args,self.cosh.text+'('))
		self.tanh.bind(on_press=lambda *args: self.calc(*args,self.tanh.text+'('))
		
		
		self.ln.bind(on_press= lambda *args : self.calc(*args,self.ln.text+'('))
		self.log.bind(on_press=lambda *args :self.calc(*args,self.log.text+'('))
		
		self.floor.bind(on_press=lambda *args:self.calc(*args,'floor('))
		self.percentage.bind(on_press=lambda *args:self.calc(*args,'%'))
		self.deg.bind(on_press=lambda *args:self.calc(*args,'°'))
		
		
		self.pi.bind(on_press=lambda *args:self.calc(*args,'π'))
		self.e.bind(on_press=lambda *args:self.calc(*args,'e'))
		self.num1.bind(on_press=lambda *args : self.calc(*args,1))
		self.num2.bind(on_press=lambda *args:self.calc(*args,2))
		self.num3.bind(on_press=lambda *args:self.calc(*args,3))
		self.num4.bind(on_press=lambda *args:self.calc(*args,4))
		self.num5.bind(on_press=lambda *args:self.calc(*args,5))
		self.num6.bind(on_press=lambda *args:self.calc(*args,6))
		self.num7.bind(on_press=lambda *args:self.calc(*args,7))
		self.num8.bind(on_press=lambda *args:self.calc(*args,8))
		self.num9.bind(on_press=lambda *args:self.calc(*args,9))
		self.num0.bind(on_press=lambda *args:self.calc(*args,0))
		
		
		self.swap.bind(on_press=self.swapfun)
		
		
		self.keypad.add_widget(self.clear)
		self.keypad.add_widget(self.swap)
		self.keypad.add_widget(self.deg)
		self.keypad.add_widget(self.open_paranthesis)
		self.keypad.add_widget(self.close_paranthesis)
		self.keypad.add_widget(self.delete)
		self.keypad.add_widget(self.sinh)
		self.keypad.add_widget(self.sin)
		self.keypad.add_widget(self.sqrt)
		self.keypad.add_widget(self.pi)
		self.keypad.add_widget(self.e)
		self.keypad.add_widget(self.divide)
		self.keypad.add_widget(self.cosh)
		self.keypad.add_widget(self.cos)
		self.keypad.add_widget(self.num7)
		self.keypad.add_widget(self.num8)
		self.keypad.add_widget(self.num9)
		self.keypad.add_widget(self.multiply)
		self.keypad.add_widget(self.tanh)
		self.keypad.add_widget(self.tan)
		self.keypad.add_widget(self.num4)
		self.keypad.add_widget(self.num5)
		self.keypad.add_widget(self.num6)
		self.keypad.add_widget(self.subtract)
		self.keypad.add_widget(self.ln)
		self.keypad.add_widget(self.log)
		self.keypad.add_widget(self.num1)
		self.keypad.add_widget(self.num2)
		self.keypad.add_widget(self.num3)
		self.keypad.add_widget(self.add)
		self.keypad.add_widget(self.floor)
		self.keypad.add_widget(self.percentage)
		self.keypad.add_widget(self.power)
		self.keypad.add_widget(self.num0)
		self.keypad.add_widget(self.dot)
		self.keypad.add_widget(self.equal)
		
		
	def swapfun(self,instance):
		global y
		if y==1:
			self.sin.text='arcsin'
			self.cos.text='arccos'
			self.tan.text='arctan'
			self.sinh.text='arcsinh'
			self.cosh.text='arccosh'
			self.tanh.text='arctanh'
			self.ln.text='e^'
			self.log.text='10^'
			y=2
		elif y==2:
			self.sin.text='sin'
			self.cos.text='cos'
			self.tan.text='tan'
			self.sinh.text='sinh'
			self.cosh.text='cosh'
			self.tanh.text='tanh'
			self.ln.text='ln'
			self.log.text='log'
			y=1
		return
	
		
	def delete_last(self,instance):
		if x==2:
			self.ans=''
			self.input.text=' '
		if self.input.text==' ':
			return	
			
		while self.input.text[-1]==' ':
			length=len(self.input.text)
			self.input.text=self.input.text[:length-1:]
		
		length=len(self.input.text)
		self.input.text=self.input.text[:length-1:]
		
		while True:
			if self.input.text==' ':
				return
			elif self.input.text[-1]==' ':
				length=len(self.input.text)
				self.input.text=self.input.text[:length-1:]
			else:
				break
		
		
	def clear_function(self,instance):
		self.ans=''
		self.input.text=' '
	
	def calc(self,instance,num):
		global x
		if x==1:
				
			if num in ('sin(','cos(','tan(','arccos(','arcsin(','arctan(','sinh(','cosh(','tanh(','arcsinh(','arccosh(','arctanh(','(','√(','floor(','π','e','log(','ln(','10^(','e^('):
				if self.input.text[-1] in ('1','2','3','4','5','6','7','8','9','0','π','e',')','%'):
					self.input.text+=' × '+str(num)
				else:
					self.input.text+=str(num)
				return
				
			if num in (1,2,3,4,5,6,7,8,9,0):
				if self.input.text[-1]=='e' or self.input.text[-1]=='π' or self.input.text[-1]=='%' or self.input.text[-1]==')':
					self.input.text+=' × '+str(num)
				else:
					self.input.text+=str(num)
			else:
				self.input.text+=str(num)
				
				
		if x==2:
			self.input.text=' '
			if num in (' + ',' - ',' × ',' / ',' ^ ','%'):
				self.input.text=' '+str(self.ans)+str(num)
			else:
				self.input.text=' '+str(num)
			x=1
		return
	
	def calculate(self,instance):
		global x
		exp=self.input.text
		while exp.count('(') >  exp.count(')'):
			exp=exp+')'
		while exp.count(')') > exp.count('('):
			exp='('+exp
		exp=exp.replace('^','**')
		exp=exp.replace('π',str(pi))
		exp=exp.replace('e',str(e))
		exp=exp.replace('√','sqrt')
		exp=exp.replace('log','log10')
		exp=exp.replace('ln','log')
		exp=exp.replace('%','/(100)')
		exp=exp.replace('×','*')
		exp=exp.replace('arc','a')
		exp=exp.replace('°','*'+str(pi)+'/180')
		try:
			self.ans=str(round(eval(exp),10))
			self.ans=self.ans.replace('e+','×10^')
			self.ans=self.ans.replace('e-','×10^-')
			self.input.text+='\n\n\n= {}'.format(str(0) if self.ans=='-0.0' else self.ans)
		except:
			if self.input.text==' ':
				pass
			elif 'Error' in self.input.text:
				pass
			elif '=' in self.input.text:
				self.input.text=str(self.ans)
			else:
				self.input.text+='\n\n\nError'
				self.ans=''
		x=2	
								
class myapp(App):
	def build(self):
		self.title='Calculator'
		self.icon='myicon.png'
		return mygrid()


if __name__=='__main__':
	myapp().run()