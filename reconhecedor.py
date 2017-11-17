# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------
#Projeto CTC34 - Parser de expressoes matematica em C                              |
#Arquivo: Reconhecedor de expressoes matematicas validas com numeros inteiros em C |
#Aceitação da Cadeia
#COMP-19                                                                           |
#2o Semestre                                                                       |
#                                                                                  |
#Grupo:                                                                            |
#Gabriela Lima                                                                     |
#Lindemberg Teixeira                                                               |
#Talize Facó                                                                       |
#                                                                                  |
#Professor: Forster S2                                                             |
#----------------------------------------------------------------------------------|

class TreeNode:
	def __init__(self,value="",left=None,right=None,parent=None):
		self.value = value
		self.leftChild = left
		self.rightChild = right
		self.parent = parent
		
	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothChildren(self):
		return self.rightChild and self.leftChild

	def getParent(self):
		return self.parent

	def setValue(self, value):
		self.value = value

	def setLeftChild(self, leftChild):
		leftChild.parent = self
		self.leftChild = leftChild
		return self.leftChild

	def setRightChild(self, rightChild):
		rightChild.parent = self
		self.rightChild = rightChild
		return self.rightChild

	def createLeftChild(self):
		self.leftChild = TreeNode("", None, None, self)
		return self.leftChild

	def createRightChild(self):
		self.rightChild = TreeNode("", None, None, self)
		return self.rightChild

	def printValue(self):
		print(self.value)

	def drawNode(self,x, jmpLine):
		#print(self.isLeftChild(),end="")
		if self.isLeftChild() or self.isRoot():
			for i in range(x+1):
				print("  ", end="")

		else:
			print("   ", end="")

		print(self.value, end="")
		
		if jmpLine:
			print("	")

		if self.hasBothChildren():
			for m in range(x):
				print("  ", end="")
			print("/   \\")
			self.hasLeftChild().drawNode(x-1, False)
			self.hasRightChild().drawNode(x+1, True)

		elif self.hasLeftChild():
			for j in range(x-1):
				print("  ", end="")
			print("/", end="")
			self.hasLeftChild().drawNode(x-1, True)

		elif self.hasRightChild():
			for k in range(x+1):
				print("  ", end="")
			print("		\\")
			self.hasRightChild().drawNode(x+2, True)

class Tree:
	def __init__(self):
		self.root = TreeNode()
	
	def getRoot(self):
		return self.root

	def tela(self):
		self.root.drawNode(10, True)

exp = input("Cadeia a ser avaliada:")


exp = exp.replace(" ", "")

list = []
parenteses = []

for ch in exp:
    list.append(ch)
list.append("$")

print("\n" + "Sequencia de simbolos:")

print(list)

print("\n")

operators = ["*", "/", "+", "-"]

est = "inicio"

print("Caminho de estados percorrido:")
for i in range(len(list)):
	if est == "inicio":
		
		if list[i].isnumeric():
			est = "num"
			
		elif list[i] == "(":
			parenteses.append("(")
			est = "inicio"

		elif list[i] == "+":
			est = "sinal_p"
		
		elif list[i] == "-":
			est = "sinal_n"
		
		else:
			est ="rejeita"
			break
	
	elif est == "sinal_p":
		if list[i].isnumeric():
			est = "num"
		
		elif list[i]=="(":
			parenteses.append("(")
			est = "inicio"
		
		else:
			est = "rejeita"
			break

	elif est == "sinal_n":
		if list[i].isnumeric():
			est = "num"
		
		elif list[i]=="(":
			est = "inicio"
			parenteses.append("(")
		
		else:
			est= "rejeita"
			break

	elif est == "num":
		if list[i].isnumeric():
			est = "num"

		elif list[i]=="+" or list[i]=="-" or list[i]=="*" or list[i]=="/" or list[i]=="%":
			est = "operador"
		
		elif list[i] == "$":
			if len(parenteses) == 0:
				est="aceita"
			else:
				est="rejeita"
			break
		
		elif list[i]==")":
			try:
				parenteses.remove("(")
				est = "fpar"
			except ValueError:
				est = "rejeita"
		
		else:
			est="rejeita"

	elif est == "operador":
		if list[i].isnumeric():
			est = "num"
		
		elif list[i]=="(":
			est = "inicio"
			parenteses.append("(")
		
		elif list[i-1]=="+" and list[i]=="-":
			est = "operador"
		
		elif list[i-1]=="-" and list[i]=="+":
			est = "operador"
		
		elif (list[i-1]=="*" or list[i-1]=="/") and (list[i]=="+" or list[i]=="-"):
			est = "operador"
		
		else:
			est = "rejeita"
			break
	
	elif est == "fpar":
		if list[i] == "$" :
			if len(parenteses) == 0:
				est="aceita"
			else:
				est="rejeita"
			
			break
		
		elif list[i]==")":
			try:
				parenteses.remove("(")
				est = "fpar"
			except ValueError:
				est = "rejeita"

		elif list[i]=="+" or list[i]=="-" or list[i]=="*" or list[i]=="/":
			est = "operador"
		else:
			est = "rejeita"
			break
	print(est)

if est == "rejeita":
	print("\n" +"A cadeia " + str(exp) + " constitui uma expressao matematica INVALIDA")
if est == "aceita":
	
	print("\n" + "A cadeia " + str(exp) + " constitui uma expressao matematica VALIDA")
	print("A arvore de precedencias: " + "\n")

	arvore = Tree()
	node = arvore.getRoot()

	for i in range(len(list)):
		if i == 0:
			node = arvore.getRoot().createLeftChild()
		
		if list[i] == "(" and i != 0:
			node = node.createLeftChild()
		
		elif list[i].isnumeric():
			node.setValue(list[i])
			if not node.getParent().hasBothChildren():
				node = node.getParent()
		
		elif list[i] in operators:
			if node.value == "":
				node.setValue(list[i])
				node = node.createRightChild()

			else:
				nodeAux = node
				if node.getParent() != None:
					node = node.getParent()
					node = node.createRightChild()
				else:
					newTree = Tree()
					node = newTree.getRoot()
					arvore = newTree
				
				node.setValue(list[i])
				aux = node.setLeftChild(nodeAux)
				node =  node.createRightChild()

		elif list[i] == ")":
			node = node.getParent()

		elif list[i] == "$":
			arvore.tela()
			print("\n")
	