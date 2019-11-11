#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

MYSQL_DB = 'health_stragegy'
MYSQL_USER = 'health_stragegy'
MYSQL_PASS = 'd41d8cd98f00b204'
MYSQL_HOST = '10.6.149.102'

connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,
                             password=MYSQL_PASS, db=MYSQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
