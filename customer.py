from atm_card  import ATMCard
class Customer:
  def __init__(self, id, custPin = 1234, custBalance = 10000):
    self.id = id
    self.pin = custPin
    self.saldo = custBalance
  def cekID(self):
  	return self.id
  def cekPIN(self):
  	return self.pin
  def cekSaldo(self):
  	return self.saldo
  #membuat metode Simpan dan Tarik
  def tarikSaldo(self, nominal):
  	self.saldo -= nominal
  def tambahSaldo(self, nominal):
  	self.saldo += nominal