
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


task 10

question

From the following table, write a SQL query to find customers whose grade is 200. Return customer_id, cust_name, city, grade, salesman_id.

query

```python sql
select customer_id, cust_name, city, grade, salesman_id from customer
where grade=200
```

result

![image](https://user-images.githubusercontent.com/122611919/221354239-b940b950-6163-4410-9872-4748b149679a.png)


task 11

question

From the following table, write a SQL query to find orders that are delivered by a salesperson with ID. 5001. Return ord_no, ord_date, purch_amt.  

query

```python sql
select ord_no, ord_date, purch_amt
from orders
where salesman_id=5001
```

result

![image](https://user-images.githubusercontent.com/122611919/221354345-4cbac0e0-c826-45a9-8832-b1be7a5a712e.png)


task 12

question


From the following table, write a SQL query to find the Nobel Prize winner(s) for the year 1970. Return year, subject and winner.


query

```python sql
select year,subject,winner 
from nobel_win 
where year=1970;
```

result

![image](https://user-images.githubusercontent.com/122611919/221354594-c8fe4e3a-0df9-4d2a-b559-d8ad964035a7.png)


task 13

question

From the following table, write a SQL query to find the Nobel Prize winner in ‘Literature’ for 1970. Return winner.

query

```python sql
select winner from nobel_win where year = 1971 and 
subject = 'Literature'
```

result

![image](https://user-images.githubusercontent.com/122611919/221354737-00cfad76-2e50-44ad-b197-2d4dfd8ece52.png)


task 14

question

From the following table, write a SQL query to locate the Nobel Prize winner ‘Dennis Gabor'. Return year, subject

query

```python sql
select year, subject from nobel_win
where winner = 'Dennis Gabor';
```

result

![image](https://user-images.githubusercontent.com/122611919/221354843-dcbc1a3c-e8e9-4bfa-86ae-9d9b47c4157d.png)


task 15

question

From the following table, write a SQL query to find the Nobel Prize winners in the field of ‘Physics’ since 1950. Return winner

query

```python sql
select winner from nobel_win where year>=1950
and subject='Physics'
```

result

![image](https://user-images.githubusercontent.com/122611919/221355004-4e558117-78f3-4b6d-bb2a-eea1deb5169c.png)


task 16

question

From the following table, write a SQL query to find the Nobel Prize winners in ‘Chemistry’ between the years 1965 and 1975. Begin and end values are included. Return year, subject, winner, and country.


query

```python sql
select year, subject, winner, country from nobel_win
where subject = 'Chemistry' and year>=1965 AND year<=1975
```

result

![image](https://user-images.githubusercontent.com/122611919/221355079-c9e09558-b9c9-4649-afa4-0e5b9e16393a.png)


task 17

question

Write a SQL query to display all details of the Prime Ministerial winners after 1972 of Menachem Begin and Yitzhak Rabin

query

```python sql
select * from nobel_win where year >1972
and winner in ('Menachem Begin', 'Yitzhak Rabin')
```

result

![image](https://user-images.githubusercontent.com/122611919/221355166-6c0a513a-1fbd-4279-8b67-234e56104b26.png)


task 18

question

From the following table, write a SQL query to retrieve the details of the winners whose first names match with the string ‘Louis’. Return year, subject, winner, country, and category.

query

```
python sql
select * from nobel_win where winner like 'Louis%'
```

result

![image](https://user-images.githubusercontent.com/122611919/221355253-ec819a7b-2607-435d-91e4-ec82ac92c7c2.png)


task 19

question

From the following table, write a SQL query that combines the winners in Physics, 1970 and in Economics, 1971. Return year, subject, winner, country, and category. 

query

```python sql
select * from nobel_win  where (subject ='Physics' and year=1970) union (select * from nobel_win  where (subject ='Economics' and year=1971))
```

result

![image](https://user-images.githubusercontent.com/122611919/221355419-1a168968-7594-4006-a867-a54606598abe.png)


task 20

question

From the following table, write a SQL query to find the Nobel Prize winners in 1970 excluding the subjects of Physiology and Economics. Return year, subject, winner, country, and category

query

```python sql
select * from nobel_win where year=1970
and subject not in('Physiology','Economics')
```

result

![image](https://user-images.githubusercontent.com/122611919/221355480-2f2d1fe0-a9ee-4e22-b2bb-6cdfceb01c1a.png)


task 21

question

From the following table, write a SQL query to combine the winners in 'Physiology' before 1971 and winners in 'Peace' on or after 1974. Return year, subject, winner, country, and category.


query

```python sql
select * from nobel_win where (subject ='Physiology' and year<1971) union (select * from nobel_win where (subject ='Peace' and year>=1974));
```

result

![image](https://user-images.githubusercontent.com/122611919/221355599-437d7680-eb8b-4b6e-906c-6037df96e655.png)




















