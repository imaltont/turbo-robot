from random import*

lotto_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
lotto_no = 7

viking_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
viking_no = 6

#regner en hel kupong
def lotto_generator(lotto):
	numbers = []
	lines = 0
	line = []
	if lotto == 1:
		numbers = list(lotto_numbers)
		lines = lotto_no
	elif lotto == 2:
		numbers = list(viking_numbers)
		lines = viking_no

	for i in range (0, lines):
		num = randint(0, len(numbers)-1)
		line.append(numbers.pop(num))
	line = quick_sort(line, 0, len(line)-1)
	print (line)

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

def main():
	lotto = input('Hvilken lotto? (1 for vanlig, 2 for viking): ')
	num_coupon = input('Hvor mange kuponger?(Kun hele tall): ')
	print ''
	for i in range (0, num_coupon):
		print 'Kupong nummer', i+1
		for i in range (0, 10):
			lotto_generator(lotto)
		print ''

while (True):
	main()