import json

file=open(r"C:\Users\Hp\Desktop\test311\result.json" , mode='r' )
a=json.load(file)
file.close()


data={"Username":'name',
              "password":'password'
         
         
} 

a.append(data)


file=open(r"C:\Users\Hp\Desktop\test311\result.json" , mode='w')
json.dump(a,file)
file.close()
for i in a:
    print()
    print(i["Username"],i["password"])
    
