#Proyekti review elememishden qabaq dictionary bilmek mutleqdir
#
#                                            |
#                                            |
#                                            |
#                                            |
#                                            |
#                                            |     
#                                       \    |    /
#                                        \   |   /
#                                         \  |  /
#                                          \ | /
#                                           \|/
#                                             
#                                      DICTIONARY 
#                                     VACIB QEYDLER

#Dictionary ozunde datalari saxliya bilen bir yigimdir, Datalari yaddasda saxlamaq ucun ramdan istifade eliyir,
#key, value mentiqi ile ishliyir, yeni dictionary her bir elementi key ve value ozunde saxliyir,
#meselen 'mehemmed_bov':'meqi123'  bir dictionaryde bir element sayilir, mehemmed_bov keydi burda, meqi12321 ise value
#dictionary qaydalarina gore keyler tekrarlana bilmez, yeni basqa biri mehemmed_bov adiyla qeydiyyatdan kecmek istese
#onu dictionarye elave elemek olmuyacaq, cunki evvelceden var idi ve tekrarlana bilmez. value ise tekrarlana biler.
#dictionaryde key bilirikse ve value-ya chatmaq isdirikse, DictionaryAdi[key] yazsaq value ala bilerik
#meselen menim bu kodda Dictionary adim Usersdir, ve mehemmed_bov-un valuesini yeni sifresini almaq isdiyirem.
#Kod bele olacaq : Users['mehemmed_bov']
# bu kod mene sifreni yeni 'meqi123' qaytaracaq

#eger bele bir kod yazsaq ki , Users['hakunamatata']='hakuna123'
#dictionary birinci baxacaq ki, hakunamatata adli key(username) var?
#eger varsa gedib onun valuesini(passwordunu) hakuna123 eliyecek
#eger ele bir username yoxdusa, onu gedib dictionarye elave eliyecek, valuesin de hakuna123 eliyecek
#dictionary ishleme mentiqi bele qurulub

#besdi bu qeder yazdim, biraz da googleda arasdirarsiniz ozunuz




#-------------------------------------------PROJECT START-------------------------------------------

#Users bizim datalari saxlamaq ucun istifade etdiyim dictionarydir,
#Numune olaraq 4 istifadeci yaradiriq
Users ={
'mehemmed_bov':'meqi123',
'the_hesenoff':'remzi123',
'vusallbv':'vusal123',
'ebilovva':'aytac123'
}


while True:
    choose=input("login or registration : ")
    if(choose=='login'):
        #------------------ Login Page Start -----------------------#
        username = input("Enter username : ")
        password = input("Enter password : ")

        IsCorrectInformation=False

        for i in Users.keys():
            if(i==username):
                if(Users[username]==password):
                    IsCorrectInformation=True
                    break

        if(IsCorrectInformation==True):
            print("Logined succesfully")
        else:
            print("Username or password is incorrect try again.")
        #------------------ Login Page End -------------------------#


    elif(choose=='reg'):
        #------------------ Register Page Start -----------------------#
        username = input("Enter username : ")
        HasUsernameInUsers=False

        for i in Users.keys():
            if(i==username):
                HasUsernameInUsers=True
                break

        if(HasUsernameInUsers==True):
            print('Username is already exists.Try again...')
        else:
            password=input("Enter password : ")
            #biz artiq burda emin oluruq ki username bizde yoxdur,
            #ona gore asagidaki kod onu dictionarye elave eliyecey(etrafli yuxarida yazmisam)
            Users[username]=password
        
        #------------------ Register Page End -------------------------#
        
    elif(choose=='exit'):
        print("Thanks for using...")
        break
    else:
        print("You can only use 3 tags in below")
        print("[login]  [reg]  [exit]")
    print()

#-------------------------------------------PROJECT END-------------------------------------------

