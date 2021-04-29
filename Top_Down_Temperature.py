
########## Read in Data  ###########
    ##Open the file for reading
openfile=input('write down the name of the file to proceed further please: ')
infile= open(openfile, 'r')
#print(infile.read())
    ##Read in lines of file
datalist=[]
for line in infile:
    #get data from string
    date,temperaturemin,temperaturemax,precipitation,swfall,swdepth,avgwindspeed,fastest2minwinddir,fastest2minwindspeed,fastest5secwinddir,fastest5secwindspeed=(line.split(';'))
    y,m,d=date.split('-')
    year=int(y)
    month=int(m)
    day=int(d)
    Tmin=float(temperaturemin)
    Tmax=float(temperaturemax)
    rain=float(precipitation)
    #put data into a list
    # store data in a larger list
    datalist.append([day,month,year,Tmin,Tmax,rain])

    #Close the File
infile.close()


########### Analyze Data  ############
    ##get the special date
in_day=int(input("please enter the day"))
in_month=int(input("please enter the month"))

    ##find historical data for that date
gooddata=[]
    #loop through all prior data
for singleday in datalist:
    #Compare day and month to user's input
    if in_month == singleday[1] and in_day == singleday[0]:
          #if matching store in a new list
        gooddata.append([singleday[2], singleday[3], singleday[4], singleday[5]])
    ##analyze historical data
minsofar=50
maxsofar=40
numgooddates=0
sumofmin=0
sumofmax=0
print(gooddata)
#loop through all data
for item in gooddata:
    numgooddates+=1
    sumofmax+=item[2]
    sumofmin+=item[1]
    if minsofar>item[1]:
        minsofar=item[1]
    if maxsofar<item[2]:
        maxsofar=item[2]

        #compute average Tmax and Tmin
avgmintemp=sumofmin/numgooddates
avgmaxtemp=sumofmax/numgooddates
########### Presents Data ############
print("The sum of the minimum temperatures is",sumofmin)
print("The sum of the maximum temperatures is",sumofmax)
print("The average of the minimum temperatures is",avgmintemp,"°K")
print("The average of the maximum temperatures is",avgmaxtemp,"°K")