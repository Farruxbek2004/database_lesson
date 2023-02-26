task 1

question

From the following table, write a SQL query to find the details of those salespeople who come from the 'Paris' City or 'Rome' City. Return salesman_id, name, city, commission.

query

```python sql
select * from salesman 
where city = 'Paris' or city = 'Rome'
```

result

![image](https://user-images.githubusercontent.com/122611919/221432540-20d14bbe-bb33-4ae1-8004-f58fc52a2001.png)


task 2

question

From the following table, write a SQL query to find the details of the salespeople who come from either 'Paris' or 'Rome'. Return salesman_id, name, city, commission. 

query

```python sql
select * from salesman 
where city in ('Paris','Rome')
```

result

![image](https://user-images.githubusercontent.com/122611919/221432796-e84713c7-1b75-403d-9ad4-c3f46ba08b23.png)


task 3

question

From the following table, write a SQL query to find the details of those salespeople who live in cities other than Paris and Rome. Return salesman_id, name, city, commission.

query

```python sql
selecy * from salesman 
where city not in('Paris','Rome')
```

result

![image](https://user-images.githubusercontent.com/122611919/221433180-a012e0c9-ff6d-4a45-b3a3-5861eb452e63.png)


task 4

question

From the following table, write a SQL query to retrieve the details of all customers whose ID belongs to any of the values 3007, 3008 or 3009. Return customer_id, cust_name, city, grade, and salesman_id.

query

```python sql
select * from customer 
where customer_id in (3007,3008,3009)
```

result

![image](https://user-images.githubusercontent.com/122611919/221433456-326467f1-d954-4d9a-88b3-46ff9af5caa1.png)

task 5

question

From the following table, write a SQL query to find salespeople who receive commissions between 0.12 and 0.14 (begin and end values are included). Return salesman_id, name, city, and commission. 

query

```python sql
select * from salesman 
where commission between 0.12 and 0.14
```

result

![image](https://user-images.githubusercontent.com/122611919/221433638-ad16e07e-cb3d-4bf6-b3ca-c2b6dd524beb.png)


task 6

question

From the following table, write a SQL query to select orders between 500 and 4000 (begin and end values are included). Exclude orders amount 948.50 and 1983.43. Return ord_no, purch_amt, ord_date, customer_id, and salesman_id


query 

``` python sql
select * from orders 
where (purch_amt between 500 and 4000) 
and not purch_amt in (948.50,1983.43)
```

result

![image](https://user-images.githubusercontent.com/122611919/221433975-99fac447-29a1-4b73-8c68-f49fdb37414a.png)
