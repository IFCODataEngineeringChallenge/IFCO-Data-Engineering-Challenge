
############################################################################
################################## PART 4 ##################################
############################################################################

import csv
import json

ORDERS = []

with open('orders.txt', mode='r') as file:
    #Use the csv reader with delimiter ';' to process the .txt file
    reader = csv.reader(file, delimiter=';')
    
    #Save each row in the list
    for row in reader:
        ORDERS.append(row)


#Open and load the JSON file
with open('invoicing_data.json', 'r') as file:
    invoiceData = json.load(file)

#Extract the invoices
invoices = invoiceData['data']['invoices']

#Convert each invoice to a list of specific values
INVOICE = [[invoice['id'], invoice['orderId'], invoice['companyId'], invoice['grossValue'], invoice['vat']] for invoice in invoices]

nINVOICE = len(INVOICE)


############################################################################
################################## PART 5 ##################################
############################################################################

#We look at the Orders ID, the salesowners, and their sizes.
orderID = [row[0] for row in ORDERS[1:]]
salesowner = [row[-1] for row in ORDERS[1:]]
n = len(orderID)

#We will divide this PART 5 into 3 steps.
#In the first step, we filter the order_ids that have an amount and note their salesowners.
#In the second step, we calculate the commissions earned by each salesowner and order (there will be duplicate salesowners).
#In the third step, we sum the amounts for each salesowner and sort the list to generate the final result.

#STEP 1

#We are going to create a first auxiliary matrix with the IDs that do have an amount and their respective salesowners.

firstAuxComissions = []

for i in range(0,n):

    #we check if for te orderID 'i' are a invoice
    if len([row[1] for row in INVOICE if row[1] == orderID[i]]) != 0:
        
        #We create an auxiliary list to add the relevant information, which we will add to the auxComissions matrix at the end of the loop.
        finalAppendList = []
        finalAppendList.append(orderID[i])
        finalAppendList.append([row[3] for row in INVOICE if row[1] == orderID[i]][0])

        #We check all the names in salesowner
        auxList = salesowner[i].split(', ')
        mAux = len(auxList)
        #We ignore all salesowners that are beyond the third position
        for j in range(0,mAux):
            if j < 3:
                finalAppendList.append(auxList[j])
        
        #FINAL: we add the information to the matrix firstAuxComissions.
        firstAuxComissions.append(finalAppendList)


nFirstAuxComissions = len(firstAuxComissions)

#STEP 2

#We are going to create a second auxiliary matrix with the commissions earned by each salesowner and each order.

secondAuxComissions = []

#We record de commissions ammounts
p1 = 0.06
p2 = 0.025
p3 = 0.0095

for i in range(0,nFirstAuxComissions):
    #Number of the salesolwners
    nAux = len(firstAuxComissions[i])-2
    #Name of the salesowners
    auxList = firstAuxComissions[i][2:]
    #invoice of the oriderID 'i'
    auxInvoice = firstAuxComissions[i][1]
    for j in range(0,nAux):
        finalAppendList = []
        #We add the salesowner's name
        finalAppendList.append(auxList[j])
        if j == 0:
            auxStrg = str(round(int(auxInvoice)*p1))
            #We add the p1 commission
            finalAppendList.append(auxStrg[:-2] + '.' + auxStrg[-2:])
        if j == 1:
            auxStrg = str(round(int(auxInvoice)*p2))
            #We add the p2 commission
            finalAppendList.append(auxStrg[:-2] + '.' + auxStrg[-2:])
        if j == 2:
            auxStrg = str(round(int(auxInvoice)*p3))
            #We add the p3 commission
            finalAppendList.append(auxStrg[:-2] + '.' + auxStrg[-2:])
        

        #FINAL: we add the information to the matrix secondAuxComissions.
        secondAuxComissions.append(finalAppendList)

#STEP 3

#We are going to create the final matrix commissionsSalesowners with the information on the commissions earned by each salesowner
salesowner = [row[0] for row in secondAuxComissions]
nSalesowner = len(salesowner)
salesownerU = list(set(salesowner))
mSalesowner = len(salesownerU)

comissionsSalesowners = []

for i in range(0,mSalesowner):

    #We create an auxiliary list to add the relevant information, which we will add to the comissionsSalesowners matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(salesownerU[i])

    #We select all the comission for each salesowner 'i' and sum that numbers
    auxList = [row[1] for row in secondAuxComissions if row[0] == salesowner[i]]
    auxNum = round(sum(float(value) for value in auxList),2)
    finalAppendList.append(auxNum)

    #FINAL: we add the information to the matrix comissionsSalesowners.
    comissionsSalesowners.append(finalAppendList)

#As a final step, we order the list
comissionsSalesowners = sorted(comissionsSalesowners, key=lambda x: x[1], reverse=True)


############################################################################
################################## PART 6 ##################################
############################################################################

companyID = [row[2] for row in ORDERS[1:]]
companyIdU = list(set(companyID))
mCompanyID = len(companyIdU)

datFrame3 = []

for i in range(0,mCompanyID):

    #We create an auxiliary list to add the relevant information, which we will add to the datFrame3 matrix at the end of the loop.
    finalAppendList = []
    finalAppendList.append(companyIdU[i])
    finalAppendList.append([row[3] for row in ORDERS if row[2] == companyIdU[i]][0])

    #We search for all the people who have participated in the company's orders
    auxList = [row[-1] for row in ORDERS if row[2] == companyIdU[i]]
    nAuxList = len(auxList)
    auxAppendList = []

    #For each company ID 'i' and each order 'j', we search for each collaborator
    for j in range(0,nAuxList):
        auxAppendList.append(auxList[j].split(', '))

    #We combine it into a single list, removing duplicates, sorting it alphabetically, and formatting it properly
    singleAuxAppendList = ', '.join(sorted(list(set([item for sublist in auxAppendList for item in sublist]))))
    finalAppendList.append(singleAuxAppendList)

    #FINAL: we add the information to the matrix datFrame3.
    datFrame3.append(finalAppendList)











    
