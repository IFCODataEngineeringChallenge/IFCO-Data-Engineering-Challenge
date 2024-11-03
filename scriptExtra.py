
############################################################################
################################## EXTRA 1 #################################
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
################################## EXTRA 2 #################################
############################################################################

crateType = [row[4] for row in ORDERS[1:]]
date = [row[1] for row in ORDERS[1:]]
nDate = len(date)
crateTypeU = list(set(crateType))
mCrateType = len(crateTypeU)

#Number of sales by type
nPlastic = crateType.count('Plastic')
nMetal = crateType.count('Metal')
nWood = crateType.count('Wood')

numYears = 5

sales = [[0 for _ in range(3)] for _ in range(numYears)]

#for every order 'i'
for i in range(0,nDate):
    #for every year 'j'
    for j in range(0,numYears):
        #check the year
        if int(date[i][-1:]) == j+1:
            #check the createType
            if crateType[i] == 'Plastic':
                sales[j][0] = sales[j][0] + 1
            if crateType[i] == 'Metal':
                sales[j][1] = sales[j][1] + 1
            if crateType[i] == 'Wood':
                sales[j][2] = sales[j][2] + 1


############################################################################
################################## EXTRA 3 #################################
############################################################################

salesPlastic = [row[2] for row in ORDERS if row[4] == 'Plastic']
salesPlasticU = list(set(salesPlastic))
mSalesPlastic = len(salesPlasticU)

topCompaniesPlastic = []

for i in range(0,mSalesPlastic):
    
    #We create an auxiliary list to add the relevant information, which we will add to the topCompaniesPlastic matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(salesPlasticU[i])
    finalAppendList.append(salesPlastic.count(salesPlasticU[i]))

    #FINAL: we add the information to the matrix topCompaniesPlastic.
    topCompaniesPlastic.append(finalAppendList)

#As a final step, we order the list
topCompaniesPlastic = sorted(topCompaniesPlastic, key=lambda x: x[1], reverse=True)[:3]

for i in range (0,3):
    topCompaniesPlastic[i][0] = [row[3] for row in ORDERS if row[2] == topCompaniesPlastic[i][0]][0]


salesMetal = [row[2] for row in ORDERS if row[4] == 'Metal']
salesMetalU = list(set(salesMetal))
mSalesMetal = len(salesMetalU)

topCompaniesMetal = []

for i in range(0,mSalesMetal):
    
    #We create an auxiliary list to add the relevant information, which we will add to the topCompaniesMetal matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(salesMetalU[i])
    finalAppendList.append(salesMetal.count(salesMetalU[i]))

    #FINAL: we add the information to the matrix topCompaniesMetal.
    topCompaniesMetal.append(finalAppendList)

#As a final step, we order the list
topCompaniesMetal = sorted(topCompaniesMetal, key=lambda x: x[1], reverse=True)[:3]

for i in range (0,3):
    topCompaniesMetal[i][0] = [row[3] for row in ORDERS if row[2] == topCompaniesMetal[i][0]][0]


salesWood = [row[2] for row in ORDERS if row[4] == 'Wood']
salesWoodU = list(set(salesWood))
mSalesWood = len(salesWoodU)

topCompaniesWood = []

for i in range(0,mSalesWood):
    
    #We create an auxiliary list to add the relevant information, which we will add to the topCompaniesWood matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(salesWoodU[i])
    finalAppendList.append(salesWood.count(salesWoodU[i]))

    #FINAL: we add the information to the matrix topCompaniesWood.
    topCompaniesWood.append(finalAppendList)

#As a final step, we order the list
topCompaniesWood = sorted(topCompaniesWood, key=lambda x: x[1], reverse=True)[:3]

for i in range (0,3):
    topCompaniesWood[i][0] = [row[3] for row in ORDERS if row[2] == topCompaniesWood[i][0]][0]
