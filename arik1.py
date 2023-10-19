import os
text = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCEAX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJTEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPXDIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PENTCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIKHKCZJOI OKEJSZCNHE."
hutsune_testua = ""
luzera = 0
letra_kont = {}
for karaktere in text:
	if karaktere.isalpha():
		if karaktere in letra_kont:
			letra_kont[karaktere] +=1
		else:
			letra_kont[karaktere] = 1

letrak_ord = sorted(letra_kont.items(), key=lambda x: x[1], reverse=True)


for c in text:
	if c == " " or c == "." or c == ",":
		hutsune_testua = hutsune_testua + c
	elif c.isdigit():
		hutsune_testua = hutsune_testua + c
	else:
		hutsune_testua = hutsune_testua + "_"
		luzera +=1
def inprimatu():
	print(" testuaren karaktere kopurua: ", luzera)
	for letra, kont in letrak_ord:
		print(f"{letra}: {kont}")
	print(hutsune_testua)
	print("\n")
	print(text)
	print("\n")



def aldaketa(a,b):
	mut_hutsune_testua = list(hutsune_testua)
	
	for i, char in enumerate(text):
		if char == a:
			mut_hutsune_testua[i] = b
			
	textu_berria2 = ''.join(mut_hutsune_testua)
	return textu_berria2
	
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
	
print("Textuko izkiak aldatzeko edo exit bukatzeko:")
print("\n")
jarraitu = True
while jarraitu == True:
	a = input("Ordezkatzeko izkia: ")
	b = input("Zeren ordez? ")
	if a == "exit" or b == "exit":
		jarraitu = False
	elif len(a) == 1 and len(b) == 1 and a.isalpha() and b.isalpha():		
		hutsune_testua = aldaketa(a,b)
		clear()
		inprimatu()
		

		
