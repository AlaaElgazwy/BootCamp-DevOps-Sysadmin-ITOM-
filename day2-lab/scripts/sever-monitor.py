cpu_usages = []
for i in range(5):
   cpu=int(input("Enter cpu usage:"))
   cpu_usages.append(cpu)

for cpu in cpu_usages:
      
     if cpu < 70 :
       print("cpu status: Normal")

     elif cpu < 90 :
       print("cpu status : Warning")
     elif cpu <= 100 :      
       print("cpu status : Critical")
     else:
       print("Invalid cpu percentage")

    