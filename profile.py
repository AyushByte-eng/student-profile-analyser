print("Student Profile Analyser")

a= input("enter your name: ")
b= input("enter your city: ")
d= input("enter your branch: ")
c1= input("enter your first language: ")
c2= input("enter your second language: ")


#list 
c =[c1,c2]

#tuples
branches= ("CSE", "AI/ML", "AI/DS", "Mechanical", "ECE")


print("====PROFILE===")

print("NAME: ", a)
print("City: ",b)
print("Branch: ",d)

print("\nFavourite Languages:")
print("1." ,c[0])
print("2." ,c[1])

#branch analsis 
print("===BRANCH===")

if  d== "CSE":
    print("Branch category: Computer Science")
elif d== "AI/ML":
    print("Branch category: Artificial Intelligence")
elif d== "AI/DS":
    print("Branch category: Artificial Intelligence and Data Science")
elif d== "ECE":
    print("Branch category: Electronics")
elif d== "Mechanical":
    print("Branch category: Core Engineering")

print("===BRANCH CHECK===")

if d in branches:
    print("Your branch is available in our list ")
else:
    print("Your branch is not in our list ")

print("\n====Analysis Complete===")
