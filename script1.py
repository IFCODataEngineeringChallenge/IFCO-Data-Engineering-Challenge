
############################################################################
################################## PART 0 ##################################
############################################################################

import csv

ORDERS = []

with open('orders.txt', mode='r') as file:
    #Use the csv reader with delimiter ';' to process the .txt file
    reader = csv.reader(file, delimiter=';')
    
    #Save each row in the list
    for row in reader:
        ORDERS.append(row)
        

############################################################################
################################## PART 1 ##################################
############################################################################

for i in range(len(ORDERS[0])):
    
    auxColumn = [row[i] for row in ORDERS]
    nAuxColumn = len(auxColumn)
    mAuxColumn = len(set(auxColumn))

    if nAuxColumn == mAuxColumn:

        print(f"The column number {i + 1} has unique records")

    else:

        print(f"The column number {i + 1} does not have unique records")
    

############################################################################
################################## PART 2 ##################################
############################################################################

#We look at the company names, the unique records of the company names, and their sizes.
companyName = [row[3] for row in ORDERS[1:]]
nCompanyName = len(companyName)
listCompanyName = list(set(companyName))
mCompanyName = len(set(companyName))

#We look at the Crate Types, the unique records of the Crate Types, and their sizes.
crateType = [row[4] for row in ORDERS[1:]]
nCrateType = len(crateType)
listCrateType = list(set(crateType))
mCrateType = len(set(crateType))

crateTypeDistribution = []

for i in range(0,mCompanyName):

    #We create an auxiliary list to add the relevant information, which we will add to the crateTypeDistribution matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(listCompanyName[i])

    #We select all the types of crates that the company 'i' has requeste
    auxList = [row[4] for row in ORDERS if row[3] == listCompanyName[i]]

    #For each crate type 'j', we look at the number of times it has been used (note that this works for any number of crates mCrateType)
    for j in range(0,mCrateType):
        auxNum = sum(1 for row in auxList if listCrateType[j] in row)
        finalAppendList.append(auxNum)

    #FINAL: we add the information to the matrix crateTypeDistribution.
    crateTypeDistribution.append(finalAppendList)


############################################################################
################################## PART 3 ##################################
############################################################################

import json

#We will create a matrix with the information we need: ['Name', 'Surname', 'City', 'cp']. This matrix will be called contactDataMatrix

#We look at the contact data and their size.
contactData = [row[-2] for row in ORDERS]
contactData = contactData[1:]
nContactData = len(contactData)

contactDataMatrix = []

#In this loop, with the help of JSON, we are going to transform the JSON into a Python list.
for i in range(0,nContactData):

    #Check if the name is recorded and, if not, place John Doe
    if len(contactData[i]) == 0:
        finalAppendList = ['John','Doe','Unknown','UNK00']
        
    else:
    
        #Convert the JSON string into a Python object
        auxData = json.loads(contactData[i])

        #Extract de values
        if auxData:
            finalAppendList = [
                auxData[0].get("contact_name"),
                auxData[0].get("contact_surname"),
                auxData[0].get("city"),
                auxData[0].get("cp")
            ]
        else:
            finalAppendList = []

    #FINAL: we add the information to the matrix crateTypeDistribution.
    contactDataMatrix.append(finalAppendList)

#We verify all cp are recorden and, if not, place UNK00
nContactDataMatrix = len(contactDataMatrix)

for i in range(0,nContactDataMatrix):
    if None in contactDataMatrix[i]:
        contactDataMatrix[i][3] = 'UNK00'

#At this point, we create the first data frame (df_1) and the second data frame (df_2)
datFrame1 = ['order_id','contact_full_name']
datFrame2 = ['order_id','contact_address']

#Now we introduce the previously generated data into the DataFrame1 and DataFrame2
for i in range(0,nContactData):

    #We create an auxiliary list to add the relevant information, which we will add to the datFrame1 matrix at the end of the loop.
    finalAppendList1 = []
    finalAppendList2 = []
    
    finalAppendList1.append(ORDERS[i+1][0])
    finalAppendList1.append(f"{contactDataMatrix[i][0]} {contactDataMatrix[i][1]}")

    finalAppendList2.append(ORDERS[i+1][0])
    finalAppendList2.append(f"{contactDataMatrix[i][2]}, {contactDataMatrix[i][3]}")

    #FINAL: we add the information to the matrix crateTypeDistribution.
    datFrame1.append(finalAppendList1)
    datFrame2.append(finalAppendList2)


