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
