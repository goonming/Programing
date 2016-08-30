#creating and accessing and modifying a dict

#ereate and print Dict
emptyDict={}
print "the value of emptyDict is :", emptyDict

#creat and print Dict with initial values
Dict={'Name':'chenming','age':100}
print "this is chen ming: ", Dict

#accessing and modifying the Dict
age_2= raw_input("please input a age: ")
Dict['age']=int(age_2)
print Dict

print "delete///"
del Dict['age']
print "the Dict after deleting: ", Dict

print "add////"
Dict['height']= 190
print "the Dict after adding is : ", Dict