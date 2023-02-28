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


task 6

question

From the following tables, write a SQL query to find all departments, including those without employees. Return first name, last name, department ID, department name.

query

``` sql
select emp.first_name, emp.last_name, dep.department_id, dep.department_name 
from employees emp right outer join departments dep on
emp.department_id = dep.department_id
```

result

![image](https://user-images.githubusercontent.com/122611919/221941459-953098c7-64b8-42a6-af3d-dcdb63b3de20.png)


task 7

question

From the following table, write a SQL query to find the employees who earn less than the employee of ID 182. Return first name, last name and salary.

query

```sql
select emp.first_name, emp.last_name, emp.salary from employees emp 
join employees s on emp.salary < s.salary and s.employee_id = 182
```

result

![image](https://user-images.githubusercontent.com/122611919/221942298-1858076e-d119-4fec-81db-03f5c6f0bcee.png)


task 8

question

From the following table, write a SQL query to find the employees and their managers. Return the first name of the employee and manager
 
query

```sql
select emp.first_name as "Employee Name",  m.first_name as "Manager"
from employees emp join employees m on emp.manager_id = m.employee_id
```

result

![image](https://user-images.githubusercontent.com/122611919/221942819-f64132e5-622d-469f-9388-ec0d8583828b.png)


task 9

question

From the following tables, write a SQL query to display the department name, city, and state province for each department.

query

```sql
select dep.department_name , loc.city , loc.state_province
from  departments dep join locations loc on  
dep.location_id = loc.location_id
```

result

![image](https://user-images.githubusercontent.com/122611919/221943316-92c99b2f-7a95-4779-872f-d9b5b61fe62d.png)


task 10

question

From the following tables, write a SQL query to find out which employees have or do not have a department. Return first name, last name, department ID, department name.

query

```sql
select emp.first_name, emp.last_name, emp.department_id,dep.department_name 
from employees emp left outer 
join departments dep 
on emp.department_id = dep.department_id
```

result

![image](https://user-images.githubusercontent.com/122611919/221944040-899ab309-bab6-4875-a18c-5a6dd1c0aa9a.png)


task 11

question

From the following table, write a SQL query to find the employees and their managers. Those managers do not work under any manager also appear in the list. Return the first name of the employee and manager. 

query

```sql
select emp.first_name as "Employee Name", m.first_name as "Manager"
from employees emp left outer join employees m
on emp.manager_id = m.employee_id
```

result

![image](https://user-images.githubusercontent.com/122611919/221944522-604af75c-9267-43fe-9980-e5f75f2d6517.png)


task 12

question

From the following tables, write a SQL query to find the employees who work in the same department as the employee with the last name Taylor. Return first name, last name and department ID

query

```sql
select emp.first_name, emp.last_name, emp.department_id 
from employees emp join employees s
on emp.department_id = s.department_id
and s.last_name = 'Taylor'
```

result

![image](https://user-images.githubusercontent.com/122611919/221945332-c6f0bf7f-7878-413e-8d03-a370da22c834.png)


task 13

question

From the following tables, write a SQL query to find all employees who joined on or after 1st January 1993 and on or before 31 August 1997. Return job title, department name, employee name, and joining date of the job

query

```sql
select job_title, department_name, first_name || ' ' || last_name AS Employee_name, start_date from job_history join jobs using (job_id) 
join departments using (department_id)  join  employees using (employee_id) where 
start_date>='1993-01-01' and start_date<='1997-08-31'
```

result

![image](https://user-images.githubusercontent.com/122611919/221946853-080a98bc-1f9b-4cef-bf23-9f861df86a8d.png)


task 14

question

From the following tables, write a SQL query to calculate the difference between the maximum salary of the job and the employee's salary. Return job title, employee name, and salary difference

query

```sql
select job_title, first_name || ' ' || last_name as Employee_name, max_salary-salary as salary_difference from employees 
natural join jobs
```

result

![image](https://user-images.githubusercontent.com/122611919/221947626-6f5c0443-94ee-4fee-a234-26466aadd629.png)


task 15

question

From the following table, write a SQL query to calculate the average salary, the number of employees receiving commissions in that department. Return department name, average salary and number of employees.

query

```sql
select department_name, avg(salary), count(commission_pct) 
from departments join employees using (department_id) 
group by department_name order by  count(commission_pct) desc
```

result

![image](https://user-images.githubusercontent.com/122611919/221948319-85bd0dba-86d9-4d97-954b-08d198235294.png)

task 16

question

From the following tables, write a SQL query to calculate the difference between the maximum salary and the salary of all the employees who work in the department of ID 80. Return job title, employee name and salary difference

query

```sql
select job_title, first_name || ' ' || last_name as Employee_name, 
max_salary-salary as salary_difference from employees 
natural join jobs where department_id  = 80
```

result

![image](https://user-images.githubusercontent.com/122611919/221948814-859782ec-4f66-445f-a260-8cd9d2f7e55f.png)


task 17

question


From the following table, write a SQL query to find the name of the country, city, and departments, which are running there.

query

```sql
select country_name,city, department_name from countries 
join locations using (country_id) join departments using (location_id)
```

result

![image](https://user-images.githubusercontent.com/122611919/221949152-1c39e448-4808-4a8f-913f-3727b7a61ab9.png)


task 18

question

From the following tables, write a SQL query to find the department name and the full name (first and last name) of the manager. 

query

```sql
select department_name, first_name || ' ' || last_name as name_of_manager	from departments dep join employees emp on (dep.manager_id=emp.employee_id)
```

result

![image](https://user-images.githubusercontent.com/122611919/221949577-3f60b071-04f6-4f72-9c00-564f5a386213.png)


task 19

question

From the following table, write a SQL query to calculate the average salary of employees for each job title

query

```sql
select job_title, avg(salary) from employees 
natural join jobs group by job_title
```

result

![image](https://user-images.githubusercontent.com/122611919/221949990-3915c225-f47b-4106-b8ec-00139f66c6a9.png)


task 20

question

From the following table, write a SQL query to find the employees who earn $12000 or more. Return employee ID, starting date, end date, job ID and department ID. 

query

```sql
select job_history.* from  job_history 
join employees on (job_history.employee_id = employees.employee_id)
where salary >= 12000
```

result

![image](https://user-images.githubusercontent.com/122611919/221950871-bd1ca318-a0a2-4110-8df1-89d7dfa1c628.png)


task 21

question

From the following tables, write a SQL query to find out which departments have at least two employees. Group the result set on country name and city. Return country name, city, and number.

query

```sql
select country_name,city, COUNT(department_id)
from countries join locations using (country_id) 
join departments using (location_id) 
where department_id in (select department_id 
from employees group by department_id 
having count(department_id)>=2)
group by country_name,city
```

result

![image](https://user-images.githubusercontent.com/122611919/221951518-c9825177-c8fb-47f7-8484-2cfadf803462.png)


task 22

question

From the following tables, write a SQL query to find the department name, full name (first and last name) of the manager and their city.

query

```sql
select department_name, first_name || ' ' || last_name as name_of_manager, city from departments dep
join employees emp on (dep.manager_id=emp.employee_id) 
join locations loc using (location_id);
```

result

![image](https://user-images.githubusercontent.com/122611919/221951754-9e2ad392-c249-4b02-a6aa-e3bfb9a8e6c4.png)


task 23

question

From the following tables, write a SQL query to calculate the number of days worked by employees in a department of ID 80. Return employee ID, job title, number of days worked

query

```sql
select employee_id, job_title, end_date-start_date days 
from job_history natural join jobs 
where department_id=80
```

result

![image](https://user-images.githubusercontent.com/122611919/221952419-105778d5-dd0a-4904-85f1-0e0c66987d85.png)


task 24

question

From the following tables, write a SQL query to find full name (first and last name), and salary of all employees working in any department in the city of London.

query

```sql
select first_name || ' ' || last_name as Employee_name, salary
from employees join departments using (department_id) 
join  locations USING (location_id) 
where  city = 'London'
```

result

![image](https://user-images.githubusercontent.com/122611919/221952798-d1f4b696-caec-413e-9ac9-37774a0fdcf9.png)


task 25

question

From the following tables, write a SQL query to find full name (first and last name), job title, start and end date of last jobs of employees who did not receive commissions

query

```sql
SELECT CONCAT(e.first_name, ' ', e.last_name) AS Employee_name,
j.job_title, h.*
FROM employees e JOIN
(SELECT MAX(start_date),
MAX(end_date),
employee_id
FROM job_history
GROUP BY employee_id) h ON e.employee_id=h.employee_id
JOIN jobs j ON j.job_id=e.job_id
WHERE e.commission_pct = 0;
```
result

![image](https://user-images.githubusercontent.com/122611919/221952984-82c10fa9-fa4d-4137-b9d2-8af66b2f9221.png)


task 26

question

From the following tables, write a SQL query to find the department name, department ID, and number of employees in each department.

query

```sql
SELECT d.department_name,
e.* FROM departments d
JOIN
(SELECT count(employee_id),
department_id
FROM employees
GROUP BY department_id) e USING (department_id)
   ```
   
result

![image](https://user-images.githubusercontent.com/122611919/221953358-b7d13d2e-5a4d-4003-9297-d22443dc7435.png)


task 27

question

From the following tables, write a SQL query to find out the full name (first and last name) of the employee with an ID and the name of the country where he/she is currently employed.


query

```sql 
SELECT first_name || ' ' || last_name 
AS Employee_name, employee_id, country_name 
FROM employees 
JOIN departments 
USING(department_id) 
JOIN locations 
USING( location_id) 
JOIN countries 
USING ( country_id)
```

result

![image](https://user-images.githubusercontent.com/122611919/221953833-65fc6ef0-aa92-4a66-a41d-c261354dd307.png)
