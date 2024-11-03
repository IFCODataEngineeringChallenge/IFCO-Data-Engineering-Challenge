
############################################################################
################################## PART 7 ##################################
############################################################################

import csv

ORDERS = []

with open('orders.txt', mode='r') as file:
    # Use the csv reader with delimiter ';' to process the .txt file
    reader = csv.reader(file, delimiter=';')
    
    # Save each row in the list
    for row in reader:
        ORDERS.append(row)


############################################################################
################################## PART 8 ##################################
############################################################################

crateType = [row[4] for row in ORDERS[1:]]
crateTypeU = list(set(crateType))
mCrateType = len(crateTypeU)

nPlastic = crateType.count('Plastic')
nMetal = crateType.count('Metal')
nWood = crateType.count('Wood')

import matplotlib.pyplot as plt

#Define the data
names = ['Plastic', 'Metal', 'Wood']
values = [nPlastic, nMetal, nWood]  # Percentages or quantities for each number

#Create the pie chart
plt.figure(figsize=(6, 6))  # Size of the figure
plt.pie(values, labels=names, autopct='%1.1f%%', startangle=140)

#Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

#Title
plt.title('Distribtion of orders by crate type')

#Show the plot
plt.show()


############################################################################
################################## PART 9 ##################################
############################################################################

#Lets assume we are at 15.06.25

dateToday = '15.06.25'
auxNumY = int(dateToday[-2:])
auxNumM = int(dateToday[-5:][:2])
auxNumD = int(dateToday[:2])

dates = [row[1] for row in ORDERS[1:]]
nDates = len(dates)

#We search for the record from which we need to start analyzing the data
p = 0
for i in range(0,nDates):
    if p == 0:
        if int(dates[i][-2:]) >= auxNumY-1:
            if int(dates[i][-5:][:2]) >= auxNumM:
                if int(dates[i][:2]) >= auxNumD:
                    p=i

#We filter the data starting from that record
DATA = ORDERS[p:]
salesownersPlastic = [row[6] for row in DATA if row[4] == 'Plastic']
nSalesownersPlastic = len(salesownersPlastic)

finalSalesownerPlastic = []

#We search for all sales by name
for i in range(0,nSalesownersPlastic):

    auxList =salesownersPlastic[i].split(', ')
    nAuxList = len(auxList)

    for j in range(0,nAuxList):
        #FINAL: we add the information to the matrix finalSalesownerPlastic.
        finalSalesownerPlastic.append(auxList[j])

#We count the number of times each one appears
finalSalesownerPlastic
finalSalesownerPlasticU = list(set(finalSalesownerPlastic))
mFinalSalesownerPlastic = len(finalSalesownerPlasticU)

numberSalesownerPlastic = []

for i in range(0,mFinalSalesownerPlastic):

    #We create an auxiliary list to add the relevant information, which we will add to the numberSalesownerPlastic matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(finalSalesownerPlasticU[i])
    finalAppendList.append(finalSalesownerPlastic.count(finalSalesownerPlasticU[i]))

    #FINAL: we add the information to the matrix numberSalesownerPlastic.
    numberSalesownerPlastic.append(finalAppendList)

#We order
numberSalesownerPlastic = sorted(numberSalesownerPlastic, key=lambda x: x[1])

# Extract names and values
names = [item[0] for item in numberSalesownerPlastic]  # Get the names
values = [item[1] for item in numberSalesownerPlastic]  # Get the associated numbers

# Create a bar chart
plt.figure(figsize=(10, 6))  # Set the size of the figure
plt.barh(names, values, color='skyblue')  # Horizontal bar chart

# Add labels and title
plt.xlabel('Number of plastic crates orders in which he/she has participated')
plt.ylabel('Names')
plt.title('Top performers selling plastic crates last 12 months')

# Show the plot
plt.show()


############################################################################
################################# PART 10 ##################################
############################################################################

#Lets assume we are at 30.06.25

#It's the same code as PART 9 but repeated for each period.


salesownersPlastic1 = [row[6] for row in ORDERS if row[1][-5:] == '04.25' and row[4] == 'Plastic']
nSalesownersPlastic1 = len(salesownersPlastic1)
salesownersPlastic2 = [row[6] for row in ORDERS if row[1][-5:] == '05.25' and row[4] == 'Plastic']
nSalesownersPlastic2 = len(salesownersPlastic2)
salesownersPlastic3 = [row[6] for row in ORDERS if row[1][-5:] == '06.25' and row[4] == 'Plastic']
nSalesownersPlastic3 = len(salesownersPlastic3)

finalSalesownerPlastic1 = []
finalSalesownerPlastic2 = []
finalSalesownerPlastic3 = []

#We search for all sales by name 1
for i in range(0,nSalesownersPlastic1):

    auxList =salesownersPlastic1[i].split(', ')
    nAuxList = len(auxList)

    for j in range(0,nAuxList):
        #FINAL: we add the information to the matrix finalSalesownerPlastic1.
        finalSalesownerPlastic1.append(auxList[j])

#We search for all sales by name 2
for i in range(0,nSalesownersPlastic2):

    auxList =salesownersPlastic2[i].split(', ')
    nAuxList = len(auxList)

    for j in range(0,nAuxList):
        #FINAL: we add the information to the matrix finalSalesownerPlastic2.
        finalSalesownerPlastic2.append(auxList[j])

#We search for all sales by name 3
for i in range(0,nSalesownersPlastic3):

    auxList =salesownersPlastic3[i].split(', ')
    nAuxList = len(auxList)

    for j in range(0,nAuxList):
        #FINAL: we add the information to the matrix finalSalesownerPlastic3.
        finalSalesownerPlastic3.append(auxList[j])

#We count the number of times each one appears
finalSalesownerPlastic1
finalSalesownerPlastic2
finalSalesownerPlastic3
finalSalesownerPlasticU1 = list(set(finalSalesownerPlastic1))
finalSalesownerPlasticU2 = list(set(finalSalesownerPlastic2))
finalSalesownerPlasticU3 = list(set(finalSalesownerPlastic3))
mFinalSalesownerPlastic1 = len(finalSalesownerPlasticU1)
mFinalSalesownerPlastic2 = len(finalSalesownerPlasticU2)
mFinalSalesownerPlastic3 = len(finalSalesownerPlasticU3)

numberSalesownerPlastic1 = []

for i in range(0,mFinalSalesownerPlastic1):

    #We create an auxiliary list to add the relevant information, which we will add to the numberSalesownerPlastic1 matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(finalSalesownerPlasticU1[i])
    finalAppendList.append(finalSalesownerPlastic1.count(finalSalesownerPlasticU1[i]))

    #FINAL: we add the information to the matrix numberSalesownerPlastic1.
    numberSalesownerPlastic1.append(finalAppendList)

numberSalesownerPlastic2 = []

for i in range(0,mFinalSalesownerPlastic2):

    #We create an auxiliary list to add the relevant information, which we will add to the numberSalesownerPlastic2 matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(finalSalesownerPlasticU2[i])
    finalAppendList.append(finalSalesownerPlastic2.count(finalSalesownerPlasticU2[i]))

    #FINAL: we add the information to the matrix numberSalesownerPlastic2.
    numberSalesownerPlastic2.append(finalAppendList)

numberSalesownerPlastic3 = []

for i in range(0,mFinalSalesownerPlastic3):

    #We create an auxiliary list to add the relevant information, which we will add to the numberSalesownerPlastic3 matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(finalSalesownerPlasticU3[i])
    finalAppendList.append(finalSalesownerPlastic3.count(finalSalesownerPlasticU3[i]))

    #FINAL: we add the information to the matrix numberSalesownerPlastic3.
    numberSalesownerPlastic3.append(finalAppendList)

#We order the data
numberSalesownerPlastic1 = sorted(numberSalesownerPlastic1, key=lambda x: x[1])
numberSalesownerPlastic2 = sorted(numberSalesownerPlastic2, key=lambda x: x[1])
numberSalesownerPlastic3 = sorted(numberSalesownerPlastic3, key=lambda x: x[1])

# Monthly data
sales_data = {
    'April': numberSalesownerPlastic1,
    'May': numberSalesownerPlastic2,
    'June': numberSalesownerPlastic3
}

# Get unique names of all salespersons
all_names = sorted({name for month in sales_data.values() for name, _ in month})

# Create a dictionary with sales data for each month
sales_by_month = {name: {'April': 0, 'May': 0, 'June': 0} for name in all_names}
for month, data in sales_data.items():
    for name, sales in data:
        sales_by_month[name][month] = sales

# Extract names and values for each month
names = list(sales_by_month.keys())
values_april = [sales_by_month[name]['April'] for name in names]
values_may = [sales_by_month[name]['May'] for name in names]
values_june = [sales_by_month[name]['June'] for name in names]

# Plot setup
bar_width = 0.25
positions_april = range(len(names))
positions_may = [p + bar_width for p in positions_april]
positions_june = [p + bar_width * 2 for p in positions_april]

plt.figure(figsize=(12, 8))

# Bar chart for each month
plt.bar(positions_april, values_april, width=bar_width, label='April', color='skyblue')
plt.bar(positions_may, values_may, width=bar_width, label='May', color='lightgreen')
plt.bar(positions_june, values_june, width=bar_width, label='June', color='salmon')

# Labels and title
plt.xlabel('Salespersons')
plt.ylabel('Number of Sales')
plt.title('Monthly Sales by Salesperson for April, May, and June')
plt.xticks([p + bar_width for p in positions_april], names, rotation=45)

plt.legend()
plt.tight_layout()

# Show the plot
plt.show()

# Show the plot
plt.show()

