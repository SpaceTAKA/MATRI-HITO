print("Welcome to MATRI-HITO ver.shit!")
print("\n")
print("Enter numbers of lines and complete MatrixA")

print("\n")
print("How to use :" )
print("Press q to quit to enter line1")
print("Enter as many q as fill all the form to quit to enter lines of MatrixA")
print("\n")

import csv
LINE=[]
line1=[]
while True:
    line1_fact=input("ENTER:")
    line1.append(line1_fact)
    print(line1)
    if "q" in line1:
        e=len(line1)-1
        line1=line1[0:e]
        restriction=len(line1)
        LINE.append(line1)
        print(LINE)
        break
while True:
    line=[]
    lines_end=["q"]*(restriction)

    for i in range(1,restriction+1):
        line_fact=input("ENTER:")
        line.append(line_fact)
        print(line)
    LINE.append(line)
    print(LINE)


    if lines_end in LINE:
        E=len(LINE)-1
        LINE=LINE[0:E]
        print("\n")
        print("Here is MatrixA")

        print("\n")



        
    
        with open("MatrixA","w") as f:
            w=csv.writer(f,delimiter=",")
            x=len(LINE)-1
            for i in range(0,x+1):
                w.writerow(LINE[i])
        with open("MatrixA","r") as f:
            r=csv.reader(f,delimiter=",")
            for lines in r:
                print("|".join(lines))

        break

print("\n")


#MatrixB　　gets started

print("\n")
print("Well, complete MatrixB")

print("\n")
print("Press q to quit to enter line1")

print("\n")



LINE_2=[]
line1_2=[]
while True:
    line1_2_fact=input("ENTER:")
    line1_2.append(line1_2_fact)
    print(line1_2)
    if "q" in line1_2:
        e=len(line1_2)-1
        line1_2=line1_2[0:e]
        restriction_2=len(line1_2)
        LINE_2.append(line1_2)
        print(LINE_2)
        break
for i in range(1,restriction):
    line_2=[]
   

    for i in range(1,restriction_2+1):
        line_fact_2=input("ENTER:")
        line_2.append(line_fact_2)
        print(line_2)
        
    LINE_2.append(line_2)
    print(LINE_2)

print("\n")

p=len(LINE_2)
q=restriction_2

ROW=[]
for j in range(0,q):
    rows=[]
    for i in range(0,p):
        rows.append(LINE_2[i][j])
    ROW.append(rows)


print("Here is MatrixB")

print("\n")

with open("MatrixB","w") as f:
    w=csv.writer(f,delimiter=",")
    x=len(LINE_2)-1
    for i in range(0,x+1):
        w.writerow(LINE_2[i])
with open("MatrixB","r") as f:
    r=csv.reader(f,delimiter=",")
    for lines_2 in r:
        print("|".join(lines_2))
    
print("\n")



print("Here is MatrixA and MatrixB")

print("\n")

print("MatrixA")
with open("MatrixA","r") as f:
    r=csv.reader(f,delimiter=",")
    for lines in r:
        print("|".join(lines))


print("\n")
print("MatrixB")
with open("MatrixB","r") as f:
    r=csv.reader(f,delimiter=",")
    for lines_2 in r:
        print("|".join(lines_2))
print("\n")





print("Okay, I'll multiply MatrixA and MatrixB")

print("\n")

print("...make it!")

print("\n")

print("This is MatrixC!")

print("\n")
#translate str into int

for I in range(0,restriction):
    for J in range(0,len(LINE)):
        LINE[J][I]=int(LINE[J][I])


for I in range(0,restriction):
    for J in range(0,len(ROW)):
        ROW[J][I]=int(ROW[J][I])
    





C=[]
for a in range(0,len(LINE)):
    linesC=[]
    for b in range(0,len(ROW)):
        Multipled=[]
        for i in range(0,restriction):
            m=int(LINE[a][i]*ROW[b][i])
            Multipled.append(m)
        f=0
        for i in Multipled:
            f +=i
        linesC.append(f)  
    C.append(linesC)
        



with open("MatrixC","w") as f:
    w=csv.writer(f,delimiter=",")
    c=len(C)
    for i in range(0,c):
        w.writerow(C[i])
with open("MatrixC","r") as f:
    r=csv.reader(f,delimiter=",")
    for LINEC in r:
        print("|".join(LINEC))
    
