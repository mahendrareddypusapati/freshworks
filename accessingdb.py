

import maincode as db


db.create("Amrita",25)


db.create("src",70,3600) 


db.read("Amrita")


db.read("src")



db.create("Amrita",50)



db.modify("Amrita",55)


 
db.delete("Amrita")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()


