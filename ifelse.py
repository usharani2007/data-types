person_1="bhavani"
person_2="usha"
interview={person_1:True,person_2:False}
if interview[person_1]:
     print("welcome to it sector")
else:
     print("go to cooking")

if interview[person_2]:
     print("welcome to it sector")
else:
     print("go to cooking")

marks={"teulugu":66,"hindi":55,"english":75,"maths":66,"social":66,"sience":55}
print(marks)
set_marks=set([marks["teulugu"],marks["hindi"],marks["english"],marks["maths"],marks["social"],marks["sience"]])
print(set_marks)
qulify=set(range(35,101))
print("student is qulified :",set_marks<qulify)
