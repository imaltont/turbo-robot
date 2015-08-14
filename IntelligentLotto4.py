#Non-deterministic after first couple
from random import*
from IntelligentLotto2 import utility_func2

lotto_tall = [] #skal inneholde lister
valgte_rekker = []
fire = 0
fem = 0
seks = 0
syv = 0

comp_list = [2, 7, 11, 21, 24, 28, 34]

#Hente fra fil
with open('LottoResultat-tal-mtil.txt') as tall:
	temp_list = []
	for line in tall:
		temp_list = line.split('|')
		temp_list[2] = temp_list[2].replace("\n","")
		for i in range(0, len(temp_list)):
			temp_list[i] = int(temp_list[i])
		lotto_tall.append(temp_list)

#Regne utility; antall ganger delt paa hvor lenge siden det var sist
def utility_func(tall_liste):
	utility_list = []
	for number in tall_liste:
		utility_list.append([float(float(number[1])/float(number[2])), number[0]])
	return utility_list

#Sorter listen paa utility
def quick_sort(line, p, r):
	if p < r:
		q = partition(line, p, r)
		quick_sort(line, p, q-1)
		quick_sort(line, q+1, r)
	return line

def partition(A, p, r):
	x = A[r]
	i = p-1
	for j in range (p, r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r] = A[r], A[i+1]
	return i+1


#velg de syv med lavest utility
def the_chosen_ones(util_list, j):
	temp_chosen = []
	right = 0
	global fem
	global syv
	global seks
	global fire
	for i in range(0, 7):
		temp_chosen.append(util_list[i][1])
	temp_chosen = quick_sort(temp_chosen, 0, len(temp_chosen)-1)
	if temp_chosen not in valgte_rekker:
		valgte_rekker.append(temp_chosen)
		print j, " ", temp_chosen
		for numb in temp_chosen:
			if numb in comp_list:
				right += 1
		if right == 7:
			syv += 1
		elif right == 6:
			seks += 1
		elif right == 5:
			fem += 1
		elif right == 4:
			fire += 1
		return True
	else:
		while temp_chosen in valgte_rekker:
			temp_util = utility_func2(lotto_tall)
			temp_chosen = []
			for i in range(0, 7):
				while len(temp_chosen) <= i:
					randi = randint(0, len(temp_util)-1)

					if temp_util[randi] not in temp_chosen:
						temp_chosen.append(temp_util[randi])
						temp_util.pop(randi)
			temp_chosen = quick_sort(temp_chosen, 0, len(temp_chosen)-1)
		valgte_rekker.append(temp_chosen)
		print j, " ", temp_chosen
		for numb in temp_chosen:
			if numb in comp_list:
				right += 1
		if right == 7:
			syv += 1
		elif right == 6:
			seks += 1
		elif right == 5:
			fem += 1
		elif right == 4:
			fire += 1

		return True

#oppdater listen
def update_list(lotto_tall, chosen):
	for number in lotto_tall:
		if number[0] in chosen:
			number[2] = 1
			number[1] += 1
		else:
			number[2] += 1
			number[1] += 1

#gjenta ti ganger per kupong som skal spilles
def main():
	num_coupon = input('Hvor mange kuponger?(Kun hele tall): ')
	print ''
	coupon_number = 1
	while len(valgte_rekker) < num_coupon*10:
		print 'Kupong nummer', coupon_number
		coupon_number += 1
		counter = 0
		while counter < 10:
			check = the_chosen_ones(quick_sort(utility_func(lotto_tall), 0, len(utility_func(lotto_tall))-1), counter+1)
			#if (check):
			counter += 1
			update_list(lotto_tall, valgte_rekker[len(valgte_rekker)-1])

		print ''
		if syv == 1:
			break

	print fire
	print fem
	print seks
	print syv
#main()
#ekstra funksjon for aa oppdatere txt filen med lotto resultat per uke
def update_lotto(row, extra):
	new_lotto_tall = []
	with open('LottoResultat-tal-mtil.txt') as tall:
		lotto_list = []
		for line in tall:
			lotto_list = line.split('|')
			lotto_list[2] = lotto_list[2].replace("\n","")
			for i in range(0, len(lotto_list)):
				lotto_list[i] = int(lotto_list[i])
			new_lotto_tall.append(lotto_list)

	for x in new_lotto_tall:
		if x[0] in row:
			x[1] += 1
			x[2] = 1
		elif x[0] == extra:
			x[2] = 1
		else:
			x[2] += 1

	with open('LottoResultat-tal-mtil.txt', 'w') as tall:
		tall.truncate()

		print new_lotto_tall
		for x in new_lotto_tall:
			counter = 0
			for y in x:
				tall.write(str(y))
				if counter != 2:
					tall.write('|')
				counter += 1
			tall.write("\n")

update_lotto([2, 7, 11, 21, 24, 28, 34], 6)