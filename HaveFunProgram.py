import random
import sys
import os

	

def suit():
	lagi = 'y'
	
	while lagi == 'y':
		
	    #pilihan user
	
		print('Pilih Angkanya (1 - 3) \n')
		print('1. Batu')
		print('2. Kertas')
		print('3. Gunting')
		pil = int(input("\nSilahkan Pilih: "))
		
		#kesalahan pilih
		if pil > 3:
			print('\n\tSalah nomor woi!')
		#pilihan computer
		com = random.choice(["Batu","Kertas","Gunting"])
	
		#program pilihan user
		
		if pil == 1:
			print('Pilihan Anda adalah: Batu')
			print('Pilihan Komputer adalah: ', com )
			if com == 'Batu':
				print('\tDraw!')
			elif com == 'Kertas':
				print('\tKamu Kalah')
			else:
			   print('\tKamu Menang')
			
		
		if pil == 2:
			print('Pilihan Anda adalah: Kertas')
			print('Pilihan Komputer adalah: ', com )
			if com == 'Kertas':
				print('\tDraw!')
			elif com == 'Gunting':
				print('\tKamu Kalah')
			else:
			   print('\tKamu Menang')
			
		
		if pil == 3:
			print('Pilihan Anda adalah: Gunting')
			print('Pilihan Komputer adalah: ', com )
			if com == 'Gunting':
				print('\tDraw!')
			elif com == 'Batu':
				print('\tKamu Kalah')
			else:
			   print('\tKamu Menang')
			
		lagi = input("\nMau Lagi? [y/t]: ")
		if lagi == 't':
			print('Thanks For Playing!')
		elif lagi != 't':
			print('[y/t] Ngentodd :v')
	
	
def kalkulator():
	
	def penjumlahan (a,b):
	    penjumlahan = a+b
	    return penjumlahan
	def pengurangan (a,b):
	    pengurangan = a-b
	    return pengurangan
	def perkalian (a,b):
	    perkalian = a*b
	    return perkalian
	def pembagian (a,b):
	    pembagian = a/b
	    return pembagian
	def pemangkatan (a,b):
	    pemangkatan = a ** b
	    return pemangkatan
	def modulus (a,b):
	    modulus = a % b
	    return modulus
	
	lgi = 'Silahkan Ulangi Lagi!'
	lagi= 'y'
	while lagi=='y':
	    print('\t   Program Kalkulator Kentang v1.0')
	    print('\n*Bagi orang awam disini tanda titik(.) = tanda koma(,)')
	    a= float(input('Masukan Bilangan 1: '))
	    b= float(input('Masukan Biilangan 2 : '))
	    print ('1. Penjumlahan \n2. Pengurangan \n3. Perkalian\n4. Pembagian \n5. Pemangkatan \n6. Modulus(sisa bagi) \n')
	    c= int(input('Pilih 1-6 : '))
	    if c== 1:
	        print('Hasilnya adalah = ', penjumlahan(a,b))
	    elif c== 2:
	        print('Hasilnya adalah = ', pengurangan(a,b))
	    elif c==3 :
	        print('Hasilnya adalah = ', perkalian(a,b))
	    elif c==4 :
	        print('Hasilnya adalah = ', pembagian(a,b))
	    elif c==5 :
	        print('Hasilnya adalah = ', pemangkatan(a,b))
	    elif c==6 :
	        print('Hasilnya adalah = ', modulus(a,b))
	    else :
	        print('1 - 6 Sayang :v')
	
	    lagi = input("Mau Lagi? [y/t] : ")
	
	    while lagi!='t' and lagi!= 'y':
	        if lagi != 't' and lagi != 'y':
	           print('[y/t] Ngentod :v')
	           print('{}'.format(lgi))
	        break
	    if lagi == 't':
	        print('Thanks For Using!')
		
	
#pengulangan system home		
lagi = 'y'			
while lagi == 'y':

	print('\tProgram Have Fun v1.0 by Taufiq')
	print('Pilih (1 - 2)\n')
	print('1. Suit Japan v.1.0')
	print('2. Kalkulator Kentang v1.0')
	pil = int(input('\nSilahkan Pilih: '))
	
	if pil > 2:
		print('Salah Nomor Woi!')
	if pil == 1:							
		suit()
	elif pil == 2:
		kalkulator()
	elif pil == 0:
		os.system("clear")
		sys.exit()
	
	
	lagi = input('\nMau main yang lain lagi? [y/t]: ')
		
	if lagi == 't':
		print('Thanks For Playing!!')
		print('\tBye bye :/')
	elif lagi != 't' or 'y':
		print('[y/t] Woiii!!')
	

	
	