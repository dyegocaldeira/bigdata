#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mysql import connector
from dotenv import load_dotenv
from pathlib import Path
import os

class Mysql:
    
    def __init__(self):
        load_dotenv()
        env_path = Path('../') / '.env'
        load_dotenv(dotenv_path=env_path)

        self.host=os.getenv("HOST")
        self.user=os.getenv("USERDB")
        self.passwd=os.getenv("PASSDB")
        self.db=os.getenv("DB")
        self.connectDB()
        self.selectDB()

    def connectDB(self):
        self.connection = connector.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        print('Connected database!\n');

    def closeConnection(self):
        self.db.close()

    def selectDB(self):
        self.db = self.connection.cursor()

    def createTable(self, tableName, fields):
        sql = 'CREATE TABLE {} ('.format(tableName)
        for field in fields:
            sql += '{} {}'.format(field.name, field.type)
            if field != fields[-1]:
                sql += ', '
        sql += ', PRIMARY KEY (id))'
        #print(sql)
        self.db.execute(sql)
        self.connection.commit()
    
    def showListDatabaseNames(self):
        self.db.execute('SHOW TABLES')
        for row in self.db:
            print(row)

    def insertManyIntoPlanilhaDyego(self, data):
        count=1
        for row in data:
            print('inserindo linha {}'.format(count))
            count += 1
            self.db.execute("INSERT INTO planilha_dyego (id, nome, email, pwd, ip, data, hora) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)", row)
        self.connection.commit()
        print('Inser many data finished')

    def showListDataByTable(self, tableName):
        self.db.execute('SELECT * FROM {}'.format(tableName))
        select = self.db.fetchall()
        for row in select:
            print(row)

    def getByTableAndWhere(self, tableName, where):
        self.db.execute('SELECT * FROM {} WHERE {}'.format(tableName, where))
        select = self.db.fetchall()
        for row in select:
            print(row)

    def deleteByTableAndWhere(self, tableName, where):
        self.db.execute('DELETE FROM {} WHERE {}'.format(tableName, where))
        self.connection.commit()
    
    def copyTableFields(self, tableName1, tableName2, fields):
        
        sql1 = 'INSERT INTO {} ('.format(tableName1)
        sql2 = ''
        for field in fields:
            sql1 += '{}'.format(field)
            sql2 += '{}'.format(field)
            if field != fields[-1]:
                sql1 += ', '
                sql2 += ', '
        sql1 += ') SELECT'
        sql2 += ' FROM {}'.format(tableName2)
        sql = '{} {}'.format(sql1, sql2)

        #print(sql)
        self.db.execute(sql)
        self.connection.commit()

    def showMoreThanOne(self, tableName, fields):

        sql1 = 'SELECT COUNT(*), '
        sql2 = '{} GROUP BY '.format(tableName)
        for field in fields:
            sql1 += '{}'.format(field)
            sql2 += '{}'.format(field)
            if field != fields[-1]:
                sql1 += ', '
                sql2 += ', '
        sql1 += ' FROM'
        sql2 += ' HAVING COUNT(*) > 1'
        sql = '{} {}'.format(sql1, sql2)

        self.db.execute(sql)
        select = self.db.fetchall()
        print('Usuários com mais de uma tentativa de login:')
        for row in select:
            print(row)
            print('\n')
            print('Lista de acessos do ip {}:'.format(row[1]))
            self.getByTableAndWhere('planilha_dyego', "ip = '{}'".format(row[1]))


