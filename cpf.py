#########################
#                       #
#      github.com       #
#          /            #
#       Faintzy         #
#                       #
#########################

cpfin = str(input("Input the CPF: "))

cpf = {}
cpf['str'] = cpfin[0:9]
cpf['fdigit'] = cpfin[9:10]
cpf['secdigit'] = cpfin[10:11]

flist = [int(i) for i in cpf['str']]
fmultiply = []

i = 10

for x in flist:

        fmultiply.append(i * x)

        i -= 1 

fdigit = 11 - (sum(fmultiply) % 11)
flist.append(fdigit)

secmultiply = []

k = 10

for x in flist[1:]:

        secmultiply.append(x * k)

        k -= 1

secdigit = 11 - (sum(secmultiply) % 11)

if int(cpf['fdigit']) == fdigit and int(cpf['secdigit']) == secdigit:

        print("Is valid cpf")

else: 

        print("Invalid cpf")
