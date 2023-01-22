print("*** Rabbit & Turtle ***")
d ,Vr ,Vt , Vf = map(int,input("Enter Input : ").split())

s = Vf*(d/(Vt - Vr))
print("%.2f" %s)
