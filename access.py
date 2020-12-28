import code as x
x.create("x1",25)
x.create("src",70,3600) 
x.read("x1")
x.read("src")
x.create("x1",50)
#usually returns error as key name is already present in database
#for you to solve this error 
#you need to use modify operation
#you can also use delete and recreate it
x.modify("x1",55)
x.delete("x1")
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
