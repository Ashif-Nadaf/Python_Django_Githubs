#Boolean Operations:- (All Output True/False)
#------------------------------------------------------
#1. s.isalpha()
#2. s.isnumeric()
#3. s.isalnum()
#4. s.isupper()
#5. s.islower()
#6. s.startswith('pattern')
#7. s.endswith('pattern')
#------------------------------------------------------
#1. s.isalpha():- (True/False)
#==>Completely only Alphabet = s.isalpha()
'''
s = 'AshifRajjakNadaf'
print(s.isalpha())

print('AshifRajjakNadaf'.isalpha())

print('Ashif Rajjak Nadaf'.isalpha())

print('AshifRajjakNadaf1234'.isalpha())

print('AshifRajjak_Nadaf'.isalpha())

print('123456789'.isalpha())
'''

#2. s.isnumeric():- (True/False)
#==>Completely only number = s.isnumeric()
'''
s = 'AshifRajjakNadaf'
print(s.isnumeric())

print('AshifRajjakNadaf'.isnumeric())

print('Ashif Rajjak Nadaf'.isnumeric())

print('AshifRajjakNadaf1234'.isnumeric())

print('AshifRajjak_Nadaf'.isnumeric())

print('123456789'.isnumeric())
'''

#3. s.isalnum():- (True/False)
#==> a-z/0-9
'''
s = 'AshifRajjakNadaf'
print(s.isalnum())

print('AshifRajjakNadaf'.isalnum())

print('Ashif Rajjak Nadaf'.isalnum())

print('AshifRajjakNadaf1234'.isalnum())

print('AshifRajjak_Nadaf'.isalnum())

print('123456789'.isalnum())
'''
#4. s.isupper:- (True/False)
#==> All Alphbets is the Capital not space = s.isupper()
'''
s = 'AshifRajjakNadaf'
print(s.isupper())

print('AshifRajjakNadaf'.isupper())

print('Ashif Rajjak Nadaf'.isupper())

print('AshifRajjakNadaf1234'.isupper())

print('AshifRajjak_Nadaf'.isupper())

print('123456789'.isupper())

print('ASHIFRAJJAKNADAF'.isupper())
'''

#5. s.islower:- (True/False)
#==> All Alphabets is the Small not space = s.islower()
'''
s = 'AshifRajjakNadaf'
print(s.islower())

print('AshifRajjakNadaf'.islower())

print('Ashif Rajjak Nadaf'.islower())

print('AshifRajjakNadaf1234'.islower())

print('AshifRajjak_Nadaf'.islower())

print('123456789'.islower())

print('ASHIFRAJJAKNADAF'.islower())

print('ashifrajjaknadaf'.islower())
'''

#6. s.startswith('pattern'):- (True/False)
#==> Start is the same character = s.startswith()

s = 'planning'
print(s.startswith('p'))

print(s.startswith('Plan'))

print(s.startswith('plan'))

print(s.startswith('plann'))

print(s.startswith('plain'))


#7. s.endswith('pattern'):- (True/False)
#==> End is the same Charcter = s.endswith()

s = 'planning'
print(s.endswith('ing'))

print(s.endswith('gni'))

print(s.endswith('nning'))

print(s.endswith('gninn'))

print(s.endswith('ng'))


#Or  #== (True/False IMP..)
'''
s = 'planning'
print(s.lower().startswith('plan'))
'''

#===============================================================






