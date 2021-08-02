passwordReal = input("Insira a sanha que você que codificar: ")
choiceCode = int(input("Insira um numero de 1 á 3: "))
while choiceCode > 3:
    choiceCode = int(input("Insira um numero de 1 á 3: "))
passwordCode = []
number = "123456789"
symbols = "!#$&?@"
real = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/-+*=_(){}[]^´~!@#$%¨&:;<>,.|\ "
case1 = ">Vz,WdqDBjU!9Xg1&CFLEZ6_]-Rp)H{¨;t=N.bm+0:oSTkGrf5%l|n$uy7s2w^Jc}´@O(x*Y8vKe#i/[I<a4A~3PMQh "
case2 = "|56M(#st+*E-!qHRP8_X{2mg$%jx^b>D01LNYGlIVw@B7K3kcOe:CW}h,;<¨f´FQa4v)[nSJ.pzr~yudUAi=9/]oTZ& "
case3 = "uR~:¨iAzWLr]V6n,fa[s>%q7|ZOpj.GdHFEe1c)!4m9b;P=52&U$y0K3NvMo}X^lIT´t*g+(Y-x8hB{S@JkQ#D_w<C/ "


def calc(case):
    w = 0
    for _ in passwordReal:
        if passwordReal[w] not in real:
            print("Senha a ser codificada, não suportada, tente outra por favor")
            break
        y = passwordReal[w]
        z = real.index(y)
        w = w + 1
        passwordCode.append(case[z])
    print("Sua senha codificada é: ")
    final = "".join(passwordCode)
    print(final)
    if symbols not in passwordCode and number not in passwordCode:
        print("Sua senha codificada com simbolos e numeros é: ")
        print("@{}1".format(final))


if choiceCode == 1:
    choice = case1
    calc(choice)
elif choiceCode == 2:
    choice = case2
    calc(choice)
elif choiceCode == 3:
    choice = case3
    calc(choice)
