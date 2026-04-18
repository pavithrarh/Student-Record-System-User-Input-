class student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def show(self):
    print(self.name,self.marks)
def average(lst):
  total = 0
  for i in lst:
      total += i.marks
  return total / len(lst)
def topper(lst):
  top=lst[0]
  for i in lst:
    if i.marks>top.marks:
      top=i
  print("topper",top.name,top.marks)
def pass_fail(lst):
    pass_count = 0
    fail_count = 0
    for i in lst:
        if i.marks >= 40:
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count
lst=[]
n=int(input("enter the number of student:"))
for i in range(n):
  name=input("enter the name :")
  marks=int(input("enter the marks:"))
  s=student(name,marks)
  lst.append(s)

for i in lst:
  i.show()
result=average(lst)
print(result)
topper(lst)
resul=pass_fail(lst)
print(resul)