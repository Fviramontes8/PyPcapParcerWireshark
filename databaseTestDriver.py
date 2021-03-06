'''
author: Seth Decker

Description: This code is a driver to test databaseReader and databaseVerification



Output:
    #>>> python databaseTestDriver
         Connecting to the PostgreSQL database...
         PostgreSQL database version:
         ('PostgreSQL 9.6.2, compiled by Visual C++ build 1800, 64-bit',)
         Database connection closed.
         
         [('192.168.1.121', '255.255.255.0', 'video', 250.0, 1.5),
         ('192.168.1.122', '255.255.255.1', 'blog', 55.0, 12.5),
         ('192.168.1.123', '255.255.255.2', 'video', 356.0, 15.5),
         ('192.168.1.124', '255.255.255.3', 'music', 157.0, 17.5),
         ('192.168.1.125', '255.255.255.4', 'other', 58.0, 15.5),
         ('192.168.1.126', '255.255.255.5', 'other', 9.0, 12.5)]
         
         Connecting to the PostgreSQL database...
         Connected to host '192.168.1.121'
         Data written
         Database connection closed.
         
         [('192.168.1.121', '255.255.255.0', 'video', 250.0, 1.5),
         ('192.168.1.122', '255.255.255.1', 'blog', 55.0, 12.5),
         ('192.168.1.123', '255.255.255.2', 'video', 356.0, 15.5),
         ('192.168.1.124', '255.255.255.3', 'music', 157.0, 17.5),
         ('192.168.1.125', '255.255.255.4', 'other', 58.0, 15.5),
         ('192.168.1.126', '255.255.255.5', 'other', 9.0, 12.5),
         ('202.163.1.248', '255.255.244.5', 'other', 9.0, 12.5),
         ('155.163.5.155', '255.255.255.5', 'other', 9.0, 12.5)]
'''

import databaseReader as dr
import databaseVerification as dv
import databaseWriter as dw

#dw.databaseWriteTable()
out = dr.getTableNames()
print(out)
#dv.verify()
#dw.databaseWriteTable()
out = dr.read(table_name = '4/14/2017PROT3None', output=True, excel=True)
print(out)
            #key, timestamp, usea, useb, totalbits, flags0-8, #packets, avstr, avgdatarate, dur, durpre, bgn
#data_list = []
#data_list.append(["1231231231", 213123, "12312321", "12123123", 123, 0, 1, 2, 3, 4, 5, 6, 7, 22, -55, 33, 22, 2, 'b'])
#data_list.append(["15645234", 123123, "623463245", "856773", 163, 7, 6, 5, 4, 3, 2, 1, 0, 12, -33, 27, 14, 2, 'g'])

#dw.databaseWriteList(data_list, table_time="4/14/2017PROT3")

#ut = dr.read(output=True)
