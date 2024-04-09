def flatten_list(a,new_array=[]):
  for i in range(len(a)):
    if type(a[i]) == type([]):
      flatten_list(a[i],new_array)
    else:
      new_array.append(a[i])
    if i==(len(a)-1):
        return new_array

a = [1,2,[3,[4,5,[6,7,[8]],9],10]]
output = [1,2,3,4,5,6,7,8,9,10]
new_array = []
print(flatten_list(a,new_array))