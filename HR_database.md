task 1

question

From the following tables, write a SQL query to find the first name, last name, department number, and department name for each employee. 

query


```sql
select emp.first_name, emp.last_name, emp.department_id, dep.department_name from employees emp join departments dep
on emp.department_id = dep.department_id
```

result

![image](https://user-images.githubusercontent.com/122611919/221794931-e58e53cb-86e4-45b7-bbca-09479a6ffc70.png)


task 2

question

From the following tables, write a SQL query to find the first name, last name, department, city, and state province for each employee.

query

```sql
select emp.first_name,emp.last_name, dep.department_name, loc.city, loc.state_province from employees emp join departments dep  
on emp.department_id = dep.department_id join locations loc
on dep.location_id = loc.location_id
```

result

![image](https://user-images.githubusercontent.com/122611919/221795888-6ee179c8-06dc-4506-b2eb-ad225a1736ee.png)


task 3

question

From the following table, write a SQL query to find the first name, last name, salary, and job grade for all employees

query

```sql
select emp.first_name, emp.last_name, emp.salary, job.grade_level
from employees emp join job_grades job on emp.salary between job.lowest_sal and job.highest_sal
```

result

![image](https://user-images.githubusercontent.com/122611919/221796871-323e5cb6-1b2a-4083-b123-284d71ac856a.png)


task 4

question

From the following tables, write a SQL query to find all those employees who work in department ID 80 or 40. Return first name, last name, department number and department name

query

```sql
select emp.first_name, emp.last_name, emp.department_id,  dep.department_name from employees emp join departments dep 
on emp.department_id = dep.department_id and emp.department_id in (80, 40) order by emp.last_name
```

result

![image](https://user-images.githubusercontent.com/122611919/221801120-cb195dd9-932a-4c0c-9bf2-8567803c7d79.png)


task 5

question

From the following tables, write a SQL query to find those employees whose first name contains the letter ‘z’. Return first name, last name, department, city, and state province.

query

```sql
select emp.first_name,emp.last_name, dep.department_name, loc.city, loc.state_province from employees emp join departments dep on emp.department_id = dep.department_id join locations loc  on dep.location_id = loc.location_id where emp.first_name like  '%z%'
```

result

![image](https://user-images.githubusercontent.com/122611919/221802119-69a932b1-f5ed-4579-8f9b-0bef0d6b521f.png)


