m = float(input("Uma distancia em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a {:.0f}cm , {:.0f}mm , {:.0f}dam , {:.0f}hm e {:.0f}km' .format(m, cm, mm, dam, hm, km))