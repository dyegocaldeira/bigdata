#!/usr/bin/python3
# -*- coding: utf-8 -*-

from utils import CSV
import time
from connections import Mysql
from interfaces import Field

############ Etapa 1

mysqlClient = Mysql()
# utilCsv = CSV()

tableName="planilha_dyego"
dm1Name="dm1_dyego"
dm2Name="dm2_dyego"
whereEmptyName="nome = ''"
whereEmptyEmail="email = ''"
whereEmptyPwd="pwd = ''"
whereEmptyIp="ip = ''"
whereEmptyDate="data = ''"
whereEmptyHour="hora = ''"
csvPath="access.csv"

"""
fields = []
  
fields.append( Field('id', 'INT NOT NULL AUTO_INCREMENT') ) 
fields.append( Field('nome', 'VARCHAR(100)') ) 
fields.append( Field('email', 'VARCHAR(100)') ) 
fields.append( Field('pwd', 'VARCHAR(30)') )
fields.append( Field('ip', 'VARCHAR(30)') )
fields.append( Field('data', 'VARCHAR(30)') )
fields.append( Field('hora', 'VARCHAR(30)') )

mysqlClient.createTable(tableName=tableName, fields=fields)

mysqlClient.showListDatabaseNames()

dataToInsert = utilCsv.openCsvByName(csvPath)

mysqlClient.insertManyIntoPlanilhaDyego(dataToInsert)
mysqlClient.showListDataByTable(tableName)
"""

############ Etapa 2

"""
print('Show empty name')
mysqlClient.getByTableAndWhere(tableName, whereEmptyName)

print('Show empty email')
mysqlClient.getByTableAndWhere(tableName, whereEmptyEmail)

print('Show empty pwd')
mysqlClient.getByTableAndWhere(tableName, whereEmptyPwd)

print('Show empty ip')
mysqlClient.getByTableAndWhere(tableName, whereEmptyIp)

print('Show empty date')
mysqlClient.getByTableAndWhere(tableName, whereEmptyDate)

print('Show empty hour')
mysqlClient.getByTableAndWhere(tableName, whereEmptyHour)

mysqlClient.deleteByTableAndWhere(tableName, whereEmptyName)
mysqlClient.deleteByTableAndWhere(tableName, whereEmptyEmail)
mysqlClient.deleteByTableAndWhere(tableName, whereEmptyPwd)
mysqlClient.deleteByTableAndWhere(tableName, whereEmptyIp)
mysqlClient.deleteByTableAndWhere(tableName, whereEmptyDate)
mysqlClient.deleteByTableAndWhere(tableName, whereEmptyHour)
"""
"""

fields = []
  
fields.append( Field('id', 'INT NOT NULL AUTO_INCREMENT') ) 
fields.append( Field('nome', 'VARCHAR(100)') ) 
fields.append( Field('email', 'VARCHAR(100)') ) 
fields.append( Field('pwd', 'VARCHAR(30)') )

mysqlClient.createTable(tableName=dm1Name, fields=fields)

fields = []

fields.append( Field('id', 'INT NOT NULL AUTO_INCREMENT') ) 
fields.append( Field('ip', 'VARCHAR(30)') ) 
fields.append( Field('data', 'VARCHAR(30)') )
fields.append( Field('hora', 'VARCHAR(30)') )

mysqlClient.createTable(tableName=dm2Name, fields=fields)

fields = ['nome', 'email', 'pwd']
mysqlClient.copyTableFields(tableName1=dm1Name, tableName2=tableName, fields=fields)


fields = ['ip', 'data', 'hora']
mysqlClient.copyTableFields(tableName1=dm2Name, tableName2=tableName, fields=fields)
"""

fields = ['ip', 'data']
mysqlClient.showMoreThanOne(tableName, fields)