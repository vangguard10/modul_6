print("This Program will determine the number of days of a given a month")

def hitung():
             
        if int(bulan) >= 13 or bulan == 0 or int(bulan) < -1:
            print("Invalid value entered : ",bulan)
        elif int(bulan) in (1,3,5,7,8,10,12):
            print("There are 31 days in the month")
        elif int(bulan) in (4,6,9,11):
            print("There are 30 days in the month")
        elif int(bulan) == 2:
            if (int(tahun) % 4 == 0 ):
                print("There are 29 days in the month")
            else:
                print("There are 28 days in the month")
def kabisat():
    if (int(tahun) % 4 == 0 ):
        print(f'{tahun} is a leap year')
    else:
        print((f'{tahun} is not a leap year'))
    
i = 1
while i==1:
    print('=============================================')
    print("Press <ENTER> to stop the program")
    bulan = input("Enter the month(1-12): ")
    tahun = input("Please enter the year (e.g., 2021): ")
    if bulan=='':
        i=0
    else: 
        hitung()
        kabisat()

        
print("Terima kasih telah menggunakan program saya. Sampai berjumpa lagi")
