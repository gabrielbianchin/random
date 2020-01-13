import os
import csv

items = os.listdir()

arq = open('dataset.csv', 'w+')

dic_amino = {
"A": '0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"C": '0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"D": '0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"E": '0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"F": '0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0',
"G": '0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"H": '0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"I": '0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"K": '0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"L": '0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"M": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0', 
"N": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0', 
"P": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0', 
"Q": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0', 
"R": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0', 
"S": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0', 
"T": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0', 
"V": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0', 
"W": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0',
"Y": '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1'
}

dic_s8 = {
"B": '1, 0, 0, 0, 0, 0, 0, 0',
"E": '0, 1, 0, 0, 0, 0, 0, 0',
"G": '0, 0, 1, 0, 0, 0, 0, 0',
"H": '0, 0, 0, 1, 0, 0, 0, 0',
"I": '0, 0, 0, 0, 1, 0, 0, 0',
"L": '0, 0, 0, 0, 0, 1, 0, 0',
"S": '0, 0, 0, 0, 0, 0, 1, 0',
"T": '0, 0, 0, 0, 0, 0, 0, 1'
}

dic_s3 = {
"C": '1, 0, 0',
"E": '0, 1, 0',
"H": '0, 0, 1'
}

cont = 0

total = 0
cond = 0

t0 = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t10 = 0
t12 = 0
t40 = 0
arq.write('A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, Q81, Q82, Q83, Q84, Q85, Q86, Q87, Q88, Q31, Q32, Q33\n')
for item in items:
	path = item
	if path.find('txt') != -1:
		print(cont)
		#cont += 1
		total += 1
		saida = ''
		with open(path, encoding='utf-8', errors='ignore') as f:
			line = f.readline()
			line = f.readline()
			line = f.readline()
			line = line.replace('\n','')
		#	linhas8 = f.readline()
		#	linhas8 = linhas8.replace('\n','')
		#	linhas3 = f.readline()
		#	linhas3 = linhas3.replace('\n','')
		#	auxaux = 0
			if len(line) < 100:
				t0 += 1
			elif len(line) < 200:
				t1 += 1
			elif len(line) < 300:
				t2 += 1
			elif len(line) < 400:
				t3 += 1
			elif len(line) < 500:
				t4 += 1
			elif len(line) < 600:
				t5 += 1
			elif len(line) < 700:
				t6 += 1
			elif len(line) < 1000:
				t10 += 1
			elif len(line) < 1200:
				t12 += 1
			else:
				t40 += 1
			cont += 1


print()
print(t0)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t10)
print(t12)
print(t40)

"""
				for i in range(len(line)):
					if line[i].upper() in dic_amino:
						saida += str(dic_amino[line[i].upper()]) + ',' + str(dic_s8[linhas8[i]]) + ',' + str(dic_s3[linhas3[i]]) + '\n'
						auxaux += 1
				for k in range(700 - auxaux):
						saida += '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0\n'
				cont += 1
				arq.write(str(saida))
		if cont > 2000:
			break
"""
