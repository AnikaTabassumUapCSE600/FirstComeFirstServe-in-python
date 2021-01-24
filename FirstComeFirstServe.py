print("How Many Process? :")
x = int(input())
burst_time_list = []
for i in range(0,x):
  print("Enter Burst Time for P"+str(i+1)+" :")
  burst_time = int(input())
  burst_time_list.append(burst_time)

sum = 0
tmps = []
print("The Average Waiting time will be  (0+", sep='', end='', flush=True)
for i in range(0,x-1):
  if i==0:
  
    sum = sum + burst_time_list[i]
    tmps.append(burst_time_list[i])
    print(str(burst_time_list[i])+"+", sep='', end='', flush=True)
  else:
    tmp = 0
    for j in range(0,i):
      tmp = tmp + burst_time_list[j]
    sum = sum + burst_time_list[i]+tmp
    tmps.append(burst_time_list[i]+tmp)
    print(str(burst_time_list[i]+tmp), sep='', end='', flush=True)
    if i != x-2:
      print("+",sep='', end='', flush=True)
print("/"+str(x)+")")
print("\t\t\t\t ="+"{:.2f}".format(sum/x))

print("Grant Chart 0 |", sep=' ', end='', flush=True)
for i in range(0,x):
  if i!=x-1:
    print(" P"+str(i+1)+" | "+str(tmps[i])+" " , sep=' ', end='|', flush=True)
  if i==x-1:
    print(" P"+str(i+1)+" | "+str(tmps[i-1]+burst_time_list[i])+" " , sep=' ', end='|', flush=True)

