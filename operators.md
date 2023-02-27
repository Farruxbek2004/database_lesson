task 1

question
    
From the following table, write a SQL query to locate the details of customers with grade values above 100. Return customer_id, cust_name, city, grade, and salesman_id. 

query

```python sql
select * from customer where grade > 100
```

result

![image](https://user-images.githubusercontent.com/122611919/221358032-48acd580-39e4-42f0-95cf-fb0848409f39.png)


task 2

question

From the following table, write a SQL query to find all the customers in ‘New York’ city who have a grade value above 100. Return customer_id, cust_name, city, grade, and salesman_id.


query

```python sql
select * from customer 
where city = 'New York' and grade>100
```

result

![image](https://user-images.githubusercontent.com/122611919/221358102-6fcb00e3-3de4-4bb4-b590-d922e0187fe4.png)


task 3


question

From the following table, write a SQL query to find customers who are from the city of New York or have a grade of over 100. Return customer_id, cust_name, city, grade, and salesman_id.

query


```python sql
select * from customer 
where city = 'New York' or grade>100
```

result


![image](https://user-images.githubusercontent.com/122611919/221358178-09cc45f4-8281-4bc1-8e61-a7de6557d9db.png)



task 4


question


From the following table, write a SQL query to find customers who are either from the city 'New York' or who do not have a grade greater than 100. Return customer_id, cust_name, city, grade, and salesman_id.


query


```python sql
select * from customer 
where city = 'New York' or not grade>100
```

result

![image](https://user-images.githubusercontent.com/122611919/221358273-1c9456f6-34ac-4b39-976a-42f97ff34c7f.png)



task 5


question

From the following table, write a SQL query to identify customers who do not belong to the city of 'New York' or have a grade value that exceeds 100. Return customer_id, cust_name, city, grade, and salesman_id. 
 

query

```python sql
select * from customer 
where not (city = 'New York' or grade>100)
```

result

![image](https://user-images.githubusercontent.com/122611919/221358376-645abb03-17b9-4de5-8bb1-9e93618411ab.png)

 
task 6

question

From the following table, write a SQL query to find details of all orders excluding those with ord_date equal to '2012-09-10' and salesman_id higher than 5005 or purch_amt greater than 1000.Return ord_no, purch_amt, ord_date, customer_id and salesman_id


query

```python sql
select * from  orders 
where not ((ord_date ='2012-09-10' 
and salesman_id>5005) 
or purch_amt>1000.00)
```

result

![image](https://user-images.githubusercontent.com/122611919/221358446-ac946b9c-bbf0-4a60-b1d5-e06c5a88cfb4.png)


task 7


question

From the following table, write a SQL query to find the details of those salespeople whose commissions range from 0.10 to0.12. Return salesman_id, name, city, and commission. 

query


```python sql
select salesman_id,name,city,commission from salesman 
where (commission > 0.10  and commission< 0.12)
```

result

![image](https://user-images.githubusercontent.com/122611919/221358521-624ffaca-3cd1-4cfb-915d-752763f3fd23.png)


task 8

question

From the following table, write a SQL query to find details of all orders with a purchase amount less than 200 or exclude orders with an order date greater than or equal to '2012-02-10' and a customer ID less than 3009. Return ord_no, purch_amt, ord_date, customer_id and salesman_id

query


```python sql
select * from  orders where (purch_amt<200 or 
not(ord_date>='2012-02-10' and customer_id<3009))
```

result

![image](https://user-images.githubusercontent.com/122611919/221358611-c1df5e18-a495-41f4-91f5-c182de0bf3df.png)


task 9


question


From the following table, write a SQL query to find all orders that meet the following conditions. Exclude combinations of order date equal to '2012-08-17' or customer 
ID greater than 3005 and purchase amount less than 1000.


query

```python sql
select * from  orders where not((ord_date ='2012-08-17' 
or customer_id>3005) and purch_amt<1000)
```

result

![image](https://user-images.githubusercontent.com/122611919/221358647-40f7578b-fc17-4a37-a3e3-117df97eae9b.png)


task 11

question

From the following table, write a SQL query to find the details of all employees whose last name is ‘Dosni’ or ‘Mardy’. Return emp_idno, emp_fname, emp_lname, and emp_dept.


query

```python sql
select * from emp_details where emp_lname ='Dosni' or emp_lname= 'Mardy'
```

result

![image](https://user-images.githubusercontent.com/122611919/221358969-27bbda7d-62ca-42fd-9cdd-3b553228794e.png)


task 12

question

From the following table, write a SQL query to find the employees who work at depart 47 or 63. Return emp_idno, emp_fname, emp_lname, and emp_dept

query

```python sql
select * from emp_details
where emp_dept = 47 or emp_dept = 63
```

result

![image](https://user-images.githubusercontent.com/122611919/221359064-3c90f92d-11c9-4264-b768-fca5b6c273fb.png)


