shop_dictionary = {
    "piekarnia":["chleb","bułki","pączek"],
    "warzywniak":["marchew","seler","rukola"]
    }
for key,value in shop_dictionary.items():
    value_copy = [word.title() for word in value] 
    print (f"Idę do sklepu {key.title()}  i kupuję tam {value_copy}")
list = []
list1= shop_dictionary["piekarnia"]
list2= shop_dictionary["warzywniak"]
list=list1+list2
print(f"W sumie kupię {len(list)} produktów.")
