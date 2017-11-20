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

from collections import deque

from classes import *

import networkx as nx
import matplotlib.pyplot as plt

operators = ["*", "/", "+", "-"]

def evaluateNode(node):

	if(node.isLeaf()):
		return node.getValue()
	else:
		if(node.getValue() == "+"):
			return float(evaluateNode(node.leftChild)) + float(evaluateNode(node.rightChild))
		if(node.getValue() == "-"):
			return float(evaluateNode(node.leftChild)) - float(evaluateNode(node.rightChild))
		if(node.getValue() == "*"):
			return float(evaluateNode(node.leftChild)) * float(evaluateNode(node.rightChild))
		if(node.getValue() == "/"):
			return float(evaluateNode(node.leftChild)) / float(evaluateNode(node.rightChild))

def evaluateExpression(parseTree):
	return evaluateNode(parseTree.getRoot())

def createTree(list):

	global operators

	arvore = Tree()
	node = arvore.getRoot()

	for i in range(len(list)):
		if i == 0:
			node = arvore.getRoot().createLeftChild()
		
		if list[i] == "(" and i != 0:
			node = node.createLeftChild()
		
		elif list[i].isnumeric():
			node.setValue(list[i])
			if node.getParent() != None:
				node = node.getParent()
		
		elif list[i] in operators:
			if node.getValue() == "":
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
			if node.getParent() != None:
				node = node.getParent()

		elif list[i] == "$":
			arvore.tela()
			print("\n")

	return arvore

def createSubtree(lista, indice):

	node = TreeNode()
	pilha = Stack()
	pilha.push(lista[indice])

	while(not pilha.isEmpty()):

		if(lista[indice] == "("):
			newNode = createSubtree(lista, indice)
		elif(lista[indice] == ")"):
			pilha.pop()
		elif(lista[indice] in operators):
			node.setValue(lista[indice - 1])

		elif(lista[indice].isnumeric()):
			numero = ""
			while(lista[indice].isnumeric()):
				numero += lista[indice]
				indice += 1
			node.setValue(numero)


def main():

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

		for i in range(len(list)):
			if list[i+1] == "$":
				break
			else:
				if list[i].isnumeric():
					while list[i + 1].isnumeric():
						list[i] += list[i + 1]
						del list[i + 1]
		print(list)
		arvore = createTree(list)

		resultado = evaluateExpression(arvore)
		print("O valor calculado é: " + str(resultado))


if __name__ == '__main__':main()
		
