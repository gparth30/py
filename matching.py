male_date=str(input("Enter Male Birth Date.:"))
male_month=str(input("Enter Male Birth Month.:"))
female_date=str(input("Enter Female Birth Date.:"))
female_month=str(input("Enter Female Birth Month.:"))
dob_m=male_date+male_month
dob_f=female_date+female_month
print(f"Male D.O.B={dob_m}")
print(f"Female D.O.B={dob_f}")

if dob_m in ['21March','22March','23March','24March','25March','26March','27March','28March','29March','30March','31March','1April','2April','3April','4April','5April','6April','7April','8April','9April','10April','11April','12April','13April','14April','15April','16April','17April','18April','19April']:
    print("Male Zodiac Sign Is Aries")
elif dob_m in ['20April','21April','22April','23April','24April','25April','26April','27April','28April','29April','30April','1May','2May','3May','4May','5May','6May','7May','8May','9May','10May','11May','12May','13May','14May','15May','16May','17May','18May','19May','20May']:
    print("Male Zodiac Sign Is Taurus")
elif dob_m in ['21May','22May','23May','24May','25May','26May','27May','28May','29May','30May','31May','1June','2June','3June','4June','5June','6June','7June','8June','9June','10June','11June','12June','13June','14June','15June','16June','17June','18June','19June','20June']:
    print("Male Zodiac Sign Is Gemini")
elif  dob_m in ['21June','22June','23June','24June','25June','26June','27June','28June','29June','30June','1July','2July','3July','4July','5July','6July','7July','8July','9July','10July','11July','12July','13July','14July','15July','16July','17July','18July','19July','20July','21July','22July']:
    print("Male Zodiac Sign Is Cancer")
elif dob_m in ['23July','24July','25July','26July','27July','28July','29July','30July','31July''1August','2August','3August','4August','5August','6August','7August','8August','9August','10August','11August','12August','13August','14August','15August','16August','17August','18August','19August','20August','21August','22August']:
    print("Male Zodiac Sign Is Leo")
elif dob_m in ['23August','24August','25August','26August','27August','28August','29August','30August','31August''1September','2September','3September','4September','5September','6September','7September','8September','9September','10September','11September','12September','13September','14September','15September','16September','17September','18September','19September','20September','21September','22September']:
    print("Male Zodiac Sign Is Virgo")
elif dob_m in['23September','24September','25September','26September','27September','28September','29September','30September','1Octomber','2Octomber','3Octomber','4Octomber','5Octomber','6Octomber','7Octomber','8Octomber','9Octomber','10Octomber','11Octomber','12Octomber','13Octomber','14Octomber','15Octomber','16Octomber','17Octomber','18Octomber','19Octomber','20Octomber''21Octomber','22Octomber']:
    print("Male Zodiac Sign Is Libra")
elif dob_m in ['23Octomber','24Octomber','25Octomber','26Octomber','27Octomber','28Octomber','29Octomber','30Octomber','31Octomber','1November','2November','3November','4November','5November','6November','7November','8November','9November','10November','11November','12November','13November','14November','15November','16November','17November','18November','19November','20November','21November']:
    print("Male Zodiac Sign Is Scorpio")
elif dob_m in ['22November','23November','24November','25November','26November','27November','28November','29November','30November','1December','2December','3December','4December','5December','6December','7December','8December','9December','10December','11December','12December','13December','14December','15December','16December','17December','18December','19December','20December','21December']:
    print("Male Zodiac Sign Is Sagittarius")
elif dob_m in ['22December','23December','24December','25December','26December','27December','28December','29December','30December','31December','1January','2January','3January','4January','5January','6January','7January','8January','9January','10January','11January','12January','13January','14January','15January','16January','17January','18January','19January']:
    print("Male Zodiac Sign Is Capricorn")
elif dob_m in ['21January','22January','23January','24January','25January','26January','27January','28January','29January','30January','31January','1February','2February','3February','4February','5February','6February','7February','8February','9February','10February','11February','12February','13February','14February','15February','16February','17February','18February']:
    print("Male Zodiac Sign Is Aquarius")
elif dob_m in ['19February','20February','21February','22February','23February','24February','25February','26February','27February','28February','29February','1March','2March','3March','4March','5March','6March','7March','8March','9March','10March','11March','12March','13March','14March','15March','16March','17March','18March','19March','20March']:
    print("Male Zodiac Sign Is Pisces")
else:
    print("Please Input Valid Date")

if dob_f in ['21March','22March','23March','24March','25March','26March','27March','28March','29March','30March','31March','1April','2April','3April','4April','5April','6April','7April','8April','9April','10April','11April','12April','13April','14April','15April','16April','17April','18April','19April']:
    print("Female Zodiac Sign Is Aries")
elif dob_f in ['20April','21April','22April','23April','24April','25April','26April','27April','28April','29April','30April','1May','2May','3May','4May','5May','6May','7May','8May','9May','10May','11May','12May','13May','14May','15May','16May','17May','18May','19May','20May']:
    print("Female Zodiac Sign Is Taurus")
elif dob_f in ['21May','22May','23May','24May','25May','26May','27May','28May','29May','30May','31May','1June','2June','3June','4June','5June','6June','7June','8June','9June','10June','11June','12June','13June','14June','15June','16June','17June','18June','19June','20June']:
    print("Female Zodiac Sign Is Gemini")
elif  dob_f in ['21June','22June','23June','24June','25June','26June','27June','28June','29June','30June','1July','2July','3July','4July','5July','6July','7July','8July','9July','10July','11July','12July','13July','14July','15July','16July','17July','18July','19July','20July','21July','22July']:
    print("Female Zodiac Sign Is Cancer")
elif dob_f in ['23July','24July','25July','26July','27July','28July','29July','30July','31July''1August','2August','3August','4August','5August','6August','7August','8August','9August','10August','11August','12August','13August','14August','15August','16August','17August','18August','19August','20August','21August','22August']:
    print("Female Zodiac Sign Is Leo")
elif dob_f in ['23August','24August','25August','26August','27August','28August','29August','30August','31August''1September','2September','3September','4September','5September','6September','7September','8September','9September','10September','11September','12September','13September','14September','15September','16September','17September','18September','19September','20September','21September','22September']:
    print("Female Zodiac Sign Is Virgo")
elif dob_f in['23September','24September','25September','26September','27September','28September','29September','30September','1Octomber','2Octomber','3Octomber','4Octomber','5Octomber','6Octomber','7Octomber','8Octomber','9Octomber','10Octomber','11Octomber','12Octomber','13Octomber','14Octomber','15Octomber','16Octomber','17Octomber','18Octomber','19Octomber','20Octomber''21Octomber','22Octomber']:
    print("Female Zodiac Sign Is Libra")
elif dob_f in ['23Octomber','24Octomber','25Octomber','26Octomber','27Octomber','28Octomber','29Octomber','30Octomber','31Octomber','1November','2November','3November','4November','5November','6November','7November','8November','9November','10November','11November','12November','13November','14November','15November','16November','17November','18November','19November','20November','21November']:
    print("Female Zodiac Sign Is Scorpio")
elif dob_f in ['22November','23November','24November','25November','26November','27November','28November','29November','30November','1December','2December','3December','4December','5December','6December','7December','8December','9December','10December','11December','12December','13December','14December','15December','16December','17December','18December','19December','20December','21December']:
    print("Female Zodiac Sign Is Sagittarius")
elif dob_f in ['22December','23December','24December','25December','26December','27December','28December','29December','30December','31December','1January','2January','3January','4January','5January','6January','7January','8January','9January','10January','11January','12January','13January','14January','15January','16January','17January','18January','19January']:
    print("Female Zodiac Sign Is Capricorn")
elif dob_f in ['21January','22January','23January','24January','25January','26January','27January','28January','29January','30January','31January','1February','2February','3February','4February','5February','6February','7February','8February','9February','10February','11February','12February','13February','14February','15February','16February','17February','18February']:
    print("Female Zodiac Sign Is Aquarius")
elif dob_f in ['19February','20February','21February','22February','23February','24February','25February','26February','27February','28February','29February','1March','2March','3March','4March','5March','6March','7March','8March','9March','10March','11March','12March','13March','14March','15March','16March','17March','18March','19March','20March']:
    print("Female Zodiac Sign Is Pisces")
else:
    print("Please Input Valid Date")

male_zodiac=str(input("Enter Male Zodiac.:"))
female_zodiac=str(input("Enter Female Zodiac.:"))
sign=male_zodiac+female_zodiac
print(f"Sign={sign}")
if male_zodiac==female_zodiac:
   print("Favourable:Should Be an Excellent Love Match") 
else:
    if sign==('AriesTaurus'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('AriesGemini'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AriesCancer'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('AriesLeo'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AriesVirgo'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('AriesLibra'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AriesScorpio'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('AriesSagittairus'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AriesCapricorn'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('AriesAquarious'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AriesPisces'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('TaurusAries'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('TaurusGemini'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('TaurusCancer'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('TaurusLeo'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('TaurusVirgo'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('TaurusLibra'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('TaurusScorpio'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('TaurusSagittarius'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('TaurusCapricorn'):
         print("Favourable:Should Be an Excellent Love Match")
    elif sign==('TaurusAquarius'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('TaurusPisces'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('GeminiAries'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('GeminiTaurus'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('GeminiCancer'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('GeminiLeo'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('GeminiVirgo'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('GeminiLibra'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('GeminiScorpio'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('GeminiSagittarius'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('GeminiCapricorn'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('GeminiAquarius'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('GeminiPisces'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('CancerAries'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('CancerTaurus'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CancerGemini'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CancerLeo'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CancerVirgo'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CancerLibra'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('CancerScorpio'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CancerSagittarius'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CancerCapricorn'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CancerAquarius'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CancerPisces'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LeoAries'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LeoTaurus'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('LeoGemini'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LeoCancer'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('LeoVirgo'):
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('LeoLibra'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LeoScorpio'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('LeoSagittarius'):
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LeoCapricorn'):
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('LeoAquarius'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LeoPisces'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('VirgoAries'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('VirgoTaurus'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('VirgoGemini'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('VirgoCancer'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('VirgoLeo'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('VirgoLibra'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('VirgoScorpio'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('VirgoSagittarius'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('VirgoCapricorn'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('VirgoAquarius'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('VirgoPisces'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LibraAries'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LibraTaurus'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('LibraGemini'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LibraCancer'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('LibraLeo'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LibraVirgo'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('LibraScorpio'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('LibraSagittarius'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LibraCapricorn'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('LibraAquarius'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('LibraPisces'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('ScorpioAries'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('ScorpioTaurus'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('ScorpioGemini'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('ScorpioCancer'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('ScorpioLeo'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('ScorpioVirgo'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('ScorpioLibra'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('ScorpioSagittarius'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('ScorpioCapricorn'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('ScorpioAquarius'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('ScorpioPisces'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('SaggittariusAries'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('SagittariusTaurus'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('SagittariusGemini'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('SagittariusCancer'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('SagittariusLeo'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('SagittariusVirgo'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('SagittariusLibra'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('SagittariusScorpio'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('SagittariusCapricorn'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('SagittariusAquarius'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('SagittariusPisces'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('CapricornAries'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('CapricornTaurus'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CapricornGemini'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CapricornCancer'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CapricornLeo'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CapricornVirgo'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CapricornLibra'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('CapricornScorpio'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('CapricornSagittarius'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CapricornAquarius'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('CapricornPisces'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AquariusAries'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AquariusTaurus'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('AquariusGemini'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AquariusCancer'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('AquariusLeo'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AquariusVirgo'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('AquariusLibra'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AquariusScorpio'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('AquariusSagittarius'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('AquariusCapricorn'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('AquariusPisces'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('PiscesAries'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('PiscesTaurus'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('PiscesGemini'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('PiscesCancer'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('PiscesLeo'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('PiscesVirgo'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('PiscesLibra'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    elif sign==('PiscesScorpio'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('PiscesSagittarius'):    
        print("Critical:Can be hard to make this relationship progress smoothly")
    elif sign==('PiscesCapricorn'):    
        print("Favourable:Should Be an Excellent Love Match")
    elif sign==('PiscesAquarius'):    
        print('''
        Less Favourabel:May Be Good,but both of you need to
        continue to work on the RELATIONSHIP
        ''')
    else:
        print("Please Valid Input")