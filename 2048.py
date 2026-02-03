import random
import os
import copy


pole = [
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', 2],
    ]



def math(pole):
	maxs = []
	for i in pole:
		maxs.append(0)
	for i in range(len(pole)):
		for j in range(len(pole)):
			element = str(pole[i][j])
			if len(element) > maxs[j]:
				maxs[j] = len(element)			
	for i in pole:
		row = '|'
		for j in range(len(pole)):
			element = str(i[j])
			row += '_'*(maxs[j] - len(element)) + element + '|'
		print(row)


def is_full(pole):
    for i in range(len(pole)):
        for j in range(len(pole)):
            element = pole[i][j]
            if element == '_':
                return False
    return True


def rand_hod(pole):
	if is_full(pole) == True:
		return pole
	randomlist=(2,2,2,4)
	random_1 = random.choice(randomlist)
	while True:
		x = random.randint(0,len(pole)-1)
		y = random.randint(0,len(pole)-1)
		if pole[x][y] == '_':
			pole[x][y] = random_1
			return pole


def del_prob(pole):
    dlina = len(pole)
    while '_' in pole:
        pole.remove('_')
    while True:
        if len(pole) >= dlina:
            return pole
        pole.insert(0, '_')


def hod(pole):
    pole = del_prob(pole)
    for i in range(len(pole)-1,-1,-1):
        if pole[i] == pole[i-1] and pole[i] != '_':
            pole[i] *= 2
            pole[i-1] =  '_'
            pole=del_prob(pole)
    return pole


def tup_to_list(pole):
    pole1 = []
    for i in pole:
        pole1.append(list(i))
    return pole1


def score(pole):
	score = 0
	for i in range(len(pole)):
		for j in range(len(pole)):
			if pole[i][j] != '_':
				score += int(pole[i][j])
	print(score)


def is_lose(pole):
	pole_copy = copy.deepcopy(pole)
	pole_w = igra(pole, 'w')
	if pole != pole_w:
		return False
	pole_d = igra(pole, 'd')
	if pole != pole_d:
		return False
	pole_s = igra(pole, 's')
	if pole != pole_s:
		return False
	pole_a = igra(pole, 'a')
	if pole != pole_a:
		return False
	return True

def igra(pole, tip):
	if tip == 'd':
		for i in range(len(pole)):
			pole_list = pole[i]
			pole_list = hod(pole_list)
			pole[i] = pole_list
		return pole
	if tip == 'a':
		for i in range(len(pole)):
			pole_list = pole[i]
			pole_list.reverse()
			pole_list = hod(pole_list)
			pole_list.reverse()
			pole[i] = pole_list
		return pole
	if tip == 's':
		pole = list(zip(*pole))
		pole = tup_to_list(pole)
		for i in range(0,len(pole)):
			pole[i] = hod(pole[i])
		pole = list(zip(*pole))
		pole = tup_to_list(pole)
		return pole
	if tip == 'w':
		pole = list(zip(*pole))
		pole = tup_to_list(pole)
		for i in range(0,len(pole)):
			pole[i].reverse()
			pole[i] = hod(pole[i])
			pole[i].reverse()
		pole = list(zip(*pole))
		pole = tup_to_list(pole)
		return pole

	



while True:
	math(pole)
	if is_lose(pole):
		print('Game Over!!!')
		break
	inputed = input('w/a/s/d:')
	if inputed not in 'wasd':
		print('WTF???')
		continue
	pole = igra(pole,inputed)
	pole = rand_hod(pole)
	os.system('cls')
	score(pole)

	




#rand_hod(pole)
#print('/////////')
#math(pole)
#del_prob(pole)
#print(pole)
#print('/////////')
#math(pole)
#print('/////////')






