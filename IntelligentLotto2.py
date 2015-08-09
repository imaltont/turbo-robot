#non-deterministic
from random import*

lotto_tall = [] #skal inneholde lister
valgte_rekker = []
fire = 0
fem = 0
seks = 0
syv = 0

comp_list = [7, 9, 12, 14, 25, 26, 27]

#Hente fra fil
with open('LottoResultat-tal-mtil.txt') as tall:
	temp_list = []
	for line in tall:
		temp_list = line.split('|')
		temp_list[2] = temp_list[2].replace("\n","")
		for i in range(0, len(temp_list)):
			temp_list[i] = int(temp_list[i])
		lotto_tall.append(temp_list)

chosen_length = int(len(lotto_tall)/2)

#Regne utility; antall ganger delt paa hvor lenge siden det var sist
def utility_func(tall_liste):
	utility_list_temp = []
	utility_list = []
	for number in tall_liste:
		for i in range(0, number[2]):
			utility_list_temp.append([float(float(number[1])/float(number[2])), number[0]])
	
	utility_list_temp = quick_sort(utility_list_temp, 0, len(utility_list_temp)-1)

	counter = 1

	for i in range(0, len(utility_list_temp)-1):
		for j in range (counter):
			utility_list.append(utility_list_temp[i][1])

	return utility_list

def utility_func2(tall_liste):
	utility_list_temp = []
	utility_list = []
	for number in tall_liste:
		for i in range(0, number[2]):
			utility_list_temp.append([float(float(number[1])/float(number[2])), number[0]])
		
	utility_list_temp = quick_sort(utility_list_temp, 0, len(utility_list_temp)-1)
	
	counter = 1
	
	for i in range(0, len(utility_list_temp)-1):
		for j in range (counter):
			utility_list.append(utility_list_temp[i][1])
	
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
	temp_util = list(util_list)
	for i in range(0, 7):
		while len(temp_chosen) <= i:
			randi = randint(0, len(temp_util)-1)
	
			if temp_util[randi] not in temp_chosen:
				temp_chosen.append(temp_util[randi])
				temp_util.pop(randi)

	temp_chosen = quick_sort(temp_chosen, 0, len(temp_chosen)-1)
	if temp_chosen not in valgte_rekker:
		valgte_rekker.append(temp_chosen)
		print j, " ", temp_chosen
		right = 0
		for numb in temp_chosen:
			if numb in comp_list:
				right += 1
		if right == 7:
			global syv
			syv += 1
		elif right == 6:
			global seks
			seks += 1
		elif right == 5:
			global fem
			fem += 1
		elif right == 4:
			global fire
			fire += 1
		return True
	else:
		return False

#oppdater listen
def update_list(lotto_tall, chosen):
	for number in lotto_tall:
		if number[0] in chosen:
			number[2] = 1
			#number[1] += 1
		else:
			number[2] += 1
			#number[1] += 1

#gjenta ti ganger per kupong som skal spilles
def main():
	num_coupon = input('Hvor mange kuponger?(Kun hele tall): ')
	print ''
	coupon_number = 1
	seven_counter = 0
	while len(valgte_rekker) < num_coupon*10:
	#while syv == 0:
		print 'Kupong nummer', coupon_number
		coupon_number += 1
		counter = 0
		while counter < 10:
			check = the_chosen_ones(quick_sort(utility_func(lotto_tall), 0, len(utility_func(lotto_tall))-1), counter+1)
			if (check):
				counter += 1
		seven_counter += 1		
		print ''

	print fire
	print fem
	print seks
	print syv
	#print seven_counter
#smain()
#ekstra funksjon for aa oppdatere txt filen med lotto resultat per uke