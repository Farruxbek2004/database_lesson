
task 1

Question

Write a SQL statement that displays all the information about all salespeople.

query
```python sql
SELECT * FROM salesman;
```
result

![image](https://user-images.githubusercontent.com/122611919/221349380-fcbbb55d-5ca2-4b31-9c92-a5f660373aee.png)

task 2

Question

Write a SQL statement to display a string "This is SQL Exercise, Practice and Solution".

query
```python sql
select  "This is SQL Exercise, Practice and Solution"
```

result

![image](https://user-images.githubusercontent.com/122611919/221349717-17a46b3f-c034-4914-945b-cfed86da8cce.png)


task 3

question

Write a SQL query to display three numbers in three columns

query

```python sql
select 1, 2, 3
```

result

![image](https://user-images.githubusercontent.com/122611919/221349800-e8706f8c-5591-41d0-a7a6-80c6645ded7e.png)


task 4

question

Write a SQL query to display the sum of two numbers 10 and 15 from the RDBMS server.

query

```python sql
select 5 + 20
```

result

![image](https://user-images.githubusercontent.com/122611919/221351236-316c0405-3cd6-47e9-abe6-f35a5fec8e26.png)


task 5

question

Write an SQL query to display the result of an arithmetic expression.

query

```python sql
select (20 + 5 - 3 * 5) / 2
```

result

![image](https://user-images.githubusercontent.com/122611919/221351282-9f4424e1-6864-4ef9-8de2-2f032ea5bed2.png)


task 6

question

Write a SQL statement to display specific columns such as names and commissions for all

query

```python sql
select name, commission
from salesman
```

result

![image](https://user-images.githubusercontent.com/122611919/221351411-5eff8b9c-3c02-4bbf-a6be-58aeeb9f9501.png)


task 7

question

Write a query to display the columns in a specific order, such as order date, salesman ID, order number, and purchase amount for all orders.

query

```python sql
select ord_date, salesman_id, ord_no, purch_amt
from orders
```

result

![image](https://user-images.githubusercontent.com/122611919/221351473-1df79d3f-bf72-4d58-b180-fc9c439bd1c3.png)


task 8

question

From the following table, write a SQL query to identify the unique salespeople ID. Return salesman_id.
 
query
 
```python sql
selct distinct salesman_id
from orders
```

result

![image](https://user-images.githubusercontent.com/122611919/221351583-1d46d533-991b-46be-89d2-62bc602117fd.png)


task 9


question

From the following table, write a SQL query to locate salespeople who live in the city of 'Paris'. Return salesperson's name, city.

query

```python sql
select name,city
from salesman
where city='Paris'
```

result

![image](https://user-images.githubusercontent.com/122611919/221351671-304d3011-daf3-4abb-811d-98a34067fd2b.png)




















