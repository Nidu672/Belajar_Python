import random
import datetime
import time
from customer import Customer

#membuat Instance dari Customer 

program_atm = Customer(id)

#buat program loop Verifikasi

while True :
	id = int(input('Masukkan Nomor PIN :'))
	percobaan = 0

	while (id != program_atm.cekPIN()) and percobaan < 3 :
		id = int(input('Pin salah. Masukkan ulang PIN :'))
		percobaan += 1 

		if percobaan == 3 :
			print('Terlalu banyak kesalahan. Silahkan ulangi dari awal. Mohon ambil kartu anda')
			exit()
#buat Loop sambutan
	while True:
		print("Selamat Datang, Silahkan Pilih Menu di bawah ini")
		print("\n1 - Cek Saldo \n2 - Tarik Tabungan \n3 - Simpan \n4 - Ganti Pin \n5 - Keluar")

		pilihan_pengguna = int(input('Masukkan Menu Pilihan Anda(1-5) :'))

	#membuat controlflow berdasarkan masukan user
		if pilihan_pengguna == 1:
			print("Saldo anda sekarang : Rp. " + str(program_atm.cekSaldo()) +'\n')
		elif pilihan_pengguna == 2:
			nominal = float(input('Masukkan jumlah uang yang ingin ditarik :'))
			konfirmasi = input('Anda akan menarik uang sebesar : Rp.' + "\t" + str(nominal) + '\n' +"Apa Anda Yakin? : Y/N ")
		
			if konfirmasi == 'Y' or 'y' :
				print('Menarik Rp. ' + str(nominal) + ' dari Saldo')
			else:
				break

			if nominal < program_atm.cekSaldo():
				program_atm.tarikSaldo(nominal)
				print('Transaksi Berhasil')
				print("Sisa Saldo Anda : Rp." + str(program_atm.cekSaldo()) + " ")
			else:
				print('Transaksi Dibatalkan. Saldo Anda tidak mencukupi')
				print('Silahkan Tambah Saldo Anda')

		elif pilihan_pengguna == 3:
			nominal = float(input('Masukkan jumlah uang yang ingin disimpan :'))
			konfirmasi = input('Anda akan menyimpan uang sebesar : Rp.' + "\t" + str(nominal) + '\n' +'Apa Anda Yakin? : Y/N ')

			if konfirmasi == 'Y' or 'y':
				program_atm.tambahSaldo(nominal)
				print('Transaksi Berhasil')
				print("Saldo Anda : Rp." + str(program_atm.cekSaldo()) + " ")
			else:
				print('Transaksi Dibatalkan')
				break

		elif pilihan_pengguna == 4:
			verifikasi_pin = int(input('Masukkan PIN Anda:'))

			while verifikasi_pin != int(program_atm.cekPIN()):
				print('PIN salah, Masukkan Ulang :')

			PIN_baru = int(input('Masukkan PIN baru Anda :'))
			konfirmasigantiPIN = int(input('Masukkan Ulang PIN baru Anda :'))

			if konfirmasigantiPIN == PIN_baru:
				print('Ganti PIN sukses')
			else:
				print('PIN salah')

		elif pilihan_pengguna == 5:
			print('Resi tercetak otomatis saat anda keluar. \n Harap simpan sebagai tanda bukti transaksi Anda')
			print('No. Transaksi', random.randint(100000, 1000000))
			print('Tanggal :', datetime.datetime.now())
			print('Saldo Anda :', program_atm.cekSaldo())
			print('Terimakasih Telah Menggunakan Layanan Kami')
			time.sleep(7)
			exit()
		else:
			print('Menu yang dimasukkan salah')
