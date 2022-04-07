#This program is designed to find out the 
#diversity of a particular goup of people.

birthcountries = set()        #Create a set
def add_people(country):      #Adding Items to the set
    for i in country:
        birthcountries.add(i) #Add each item given.
     

#This is the test to make sure that the set is functioning correctly. 
#We should get an output of
# "{'Jamaca', 'Switzerland', 'America', 'New England', 'Korea', 'Israel'}"
country_list = ["America", "Jamaca", "Korea", 
"Israel", "New England", "Jamaca","Switzerland","America", "Korea", "Korea" ]
add_people(country_list)
print(birthcountries)