message = """Nhpbz Qbspbz Jhlzhy dhz h Yvthu nlulyhs huk zahalzthu dov wshflk h jypapjhs yvsl pu aol lcluaz aoha slk av aol kltpzl vm aol Yvthu Ylwbispj huk aol ypzl vm aol Yvthu Ltwpyl. Pu 60 IJ, Jhlzhy, Jyhzzbz huk Wvtwlf mvytlk aol Mpyza Aypbtcpyhal, h wvspapjhs hssphujl aoha kvtpuhalk Yvthu wvspapjz mvy zlclyhs flhyz. Aolpy haaltwaz av hthzz wvdly hz Wvwbshylz dlyl vwwvzlk if aol Vwapthalz dpaopu aol Yvthu Zluhal, htvun aolt Jhav aol Fvbunly dpao aol mylxblua zbwwvya vm Jpjlyv. Jhlzhy yvzl av iljvtl vul vm aol tvza wvdlymbs wvspapjphuz pu aol Yvthu Ylwbispj aoyvbno h zaypun vm tpspahyf cpjavyplz pu aol Nhsspj Dhyz, jvtwslalk if 51 IJ, dopjo nylhasf lealuklk Yvthu alyypavyf. Kbypun aopz aptl ol ivao puchklk Iypahpu huk ibpsa h iypknl hjyvzz aol Yopul ypcly. Aolzl hjoplcltluaz huk aol zbwwvya vm opz clalyhu hytf aoylhalulk av ljspwzl aol zahukpun vm Wvtwlf, dov ohk ylhspnulk optzlsm dpao aol Zluhal hmaly aol klhao vm Jyhzzbz pu 53 IJ. Dpao aol Nhsspj Dhyz jvujsbklk, aol Zluhal vyklylk Jhlzhy av zalw kvdu myvt opz tpspahyf jvtthuk huk ylabyu av Yvtl. Slhcpun opz jvtthuk pu Nhbs dvbsk tlhu svzpun opz pttbupaf av jyptpuhs wyvzljbapvu if opz lultplz; ruvdpun aopz, Jhlzhy vwlusf klmplk aol Zluhal'z hbaovypaf if jyvzzpun aol Ybipjvu huk thyjopun avdhykz Yvtl ha aol olhk vm hu hytf. Aopz ilnhu Jhlzhy'z jpcps dhy, dopjo ol dvu, slhcpun opt pu h wvzpapvu vm ulhy bujohsslunlk wvdly huk pumsblujl.""".lower()


def caesar_cipher(message, shift):
    deciphered_message = ""
    print(shift)
    for char in message:
        if(char.isalpha()):
            uni = ord(char)
            shifted = (uni-97+shift)%26
            deciphered_message += chr(97+shifted)
        else:
            deciphered_message += char
    return deciphered_message


deciphered_message = caesar_cipher(message, -7)
print(deciphered_message)
