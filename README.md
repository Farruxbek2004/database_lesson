Task 1

Question

Categories jadval barcha ustun ma’lumotlarini bilan qaytaring?

Query

select * from categories;

Result
 ![image](https://user-images.githubusercontent.com/122611919/220969666-71ec6fed-6afc-4994-8f02-71f7fe7b29bb.png)

Task 2

Question

Categories jadval category_name va description ustun ma’lumotlarini qaytaring

Query

select category_name, description from categories;

Result

![image](https://user-images.githubusercontent.com/122611919/220971139-f170a8dd-c1cc-48bc-89e5-66e7dbd3d182.png)

Task 3

Question

Categories jadval barcha ustun ma’lumotlari olishda ustun nomlarini o’zbekcha tarjimada
qaytaring. M-n: category_name=Nomi

Query

select category_id as id, category_name as nomi, description as tavsif from categories

Result

![image](https://user-images.githubusercontent.com/122611919/220972048-438ff0ff-cb3a-4ff0-ba12-ae73de27ad1b.png)

Task 4

Question

Categories jadvaldan kategoriya nomi ’Confections’ ga teng bo’lgan ma’lumotlarni
qaytaring.


Query

select * from categories where category_name = 'Confections'

Result

![image](https://user-images.githubusercontent.com/122611919/220972438-5045066e-3ed2-427d-aff8-a7a065f92a04.png)


Task 5

Question

Categories jadvaldan kategoriya nomi ‘Produce’ yoki ‘Seafood’ bo’lgan ma’lumotlarni
qaytaring.

Query

select * from categories where category_name = 'Produce' or  category_name = 'Seafood';

Result

![image](https://user-images.githubusercontent.com/122611919/220972881-19fb6a01-146e-4ca1-8c18-51772f44b61e.png)



Task 6

Question

Categories jadvaldan quyida belgilangan ma’lumotlarni qaytaring.

Query

 select * from categories limit 3 offset 5

Result

![image](https://user-images.githubusercontent.com/122611919/220973440-c6ed4349-fa2a-437b-8e3a-9cf263ed4961.png)



Task 7

Question

Categories jadvaldan ma’lumotlarni description alifbo bo’yicha Z-A tartibida chiqaring.

Query

select * from categories order by description desc 

Result

![image](https://user-images.githubusercontent.com/122611919/220974055-f095fcbe-c925-4ccb-ae19-a4e1565252d0.png)



Task 8

Question

Customers jadvalidan barcha ma’lumotlarni oling.

Query

select * from customers; 

Result

![image](https://user-images.githubusercontent.com/122611919/220975945-7372c02c-5ef0-403d-9dd5-72fbfe2349ed.png)


Task 9

Question

Customers jadvalida ustun nomlarini o’zbekcha holatda oling.

Query

select customer_id as id, company_name as shirkat_nomi, contact_name as kontakt_nomi, contact_title as kontakt_sarlavhasi,
       address as manzil, city as shahar, region as mintaqa, postal_code as pochta_kodi, country as mamlakat,
       phone as telfon, fax as faks from customers;

Result

![image](https://user-images.githubusercontent.com/122611919/220977207-3d99bd36-fd89-4856-8371-e5e2526d5104.png)

![image](https://user-images.githubusercontent.com/122611919/220977406-08b76ed7-568c-49f4-949b-9cfa8fdf5c84.png)



Task 10

Question

Customers jadvalidan contact_title ‘Owner’ bo’lgan ma’lumotlarni qaytaring.

Query

select * from customers where contact_title = 'Owner'

Result

![image](https://user-images.githubusercontent.com/122611919/220978079-774bd953-acae-449d-b973-bcd49203aa57.png)


Task 11

Question

Customers jadvalidan city ‘London’ bo’lgan ma’lumotlarni qaytaring.

Query

select * from customers where city = 'London'

Result

![image](https://user-images.githubusercontent.com/122611919/220978508-d55558ff-3f30-433c-a5c1-670c270cc0e9.png)


Task 12

Question


Customers jadvalidan region ustun NULL bo’lgan ma’lumotlarni qaytaring.

Query

select * from customers where region is null

Result

![image](https://user-images.githubusercontent.com/122611919/220979017-bf166cd1-0d70-4a40-a8dd-dd93f63ee395.png)


Task 13

Question

Customers jadvalidan region ustun NULL bo’lmagan ma’lumotlarni qaytaring.


Query

select * from customers where region is not null;

Result

![image](https://user-images.githubusercontent.com/122611919/220979298-62d3d747-9244-4eec-9223-f043b3ffddfd.png)



Task 14

Question

Customers jadvalidan country ustun Germany bo’lgan ma’lumotlarni qaytaring.

Query

select * from customers where country = 'Germany';

Result

![image](https://user-images.githubusercontent.com/122611919/220979541-0da6fd43-b65e-4b63-b05a-0526b1075574.png)



Task 15

Question

 Customers jadvalidan country ustun Germany bo’lgan qatorlar sonini qaytaring.

Query

select count(country) from customers where country = 'Germany';

Result

![image](https://user-images.githubusercontent.com/122611919/220979743-ddebd718-4fe5-4a94-815e-df1dbce5e7cb.png)



Task 16

Question

Customers jadvalidan fax ustun NULL bo’lmalgan ma’lumotlarni contact_name ustun
alifbo tartiba tartiblab qaytaring.

Query

select * from customers where fax is not null order by contact_name;

Result

![image](https://user-images.githubusercontent.com/122611919/220983044-acd7fd6c-e125-4ce8-88a1-0a1b6df9f30e.png)

![image](https://user-images.githubusercontent.com/122611919/220983081-6379b911-566d-411d-aaaa-ee8d0396897e.png)



Task 17

Question

Employees jadvaldan barcha ma’lumotlarni qaytaring.

Query

select * from employees

Result

![image](https://user-images.githubusercontent.com/122611919/220983398-e62f61eb-859b-436f-98b5-3d238e14ccd9.png)



Task 18

Question

Employees jadval ustun nomlarini o’zbekcha qaytaring

Query


select
employee_id as id ,
first_name as ismi ,
last_name as familiya ,
title as sarlavha,
address as adres ,
title_of_courtesy as "murojaat qilish odobi",
birth_date as "tug'ilgan sanasi",
hire_date as "ishga qabul qilingan sanasi",
address as adres,
city as shahar,
region as hudud,
postal_code as "pochta kodi",
country as viloyat,
home_phone as "uy telefon",
extension as kengaytma,
photo as rasm,
photo_path as "rasm linki",
notes as elsatmalar
from employees;


Result

![image](https://user-images.githubusercontent.com/122611919/220984205-73d14ac6-3172-479a-840e-9c6109fe9b0d.png)


![image](https://user-images.githubusercontent.com/122611919/220984397-badb57f0-df55-4a50-95c8-5dc2d02d38a0.png)


Task 19

Question

Employess jadvaldan title_of_courtest ‘Mr’ bo’lgan xodimlarni firts_name alifbo tartibida
qaytaring.


Query

select * from employees where title_of_courtesy = 'Mr.' order by first_name;

Result

![image](https://user-images.githubusercontent.com/122611919/220984801-69b5bb29-70fb-40af-bb33-5e4919f92d17.png)



Task 20

Question

Employes jadvalda title ‘Sales Representative’ bo’lgan xodimlar sonini qaytaring.

Query

select count(title) from employees where title = 'Sales Representative';

Result

![image](https://user-images.githubusercontent.com/122611919/220984999-9e6eca02-9d26-4c90-a91a-11bf95114822.png)



Task 21

Question

Employes jadvalda hire_date 1994-yilda bo’lgan ma’lumotlarni qaytaring.

Query

select * from employees where hire_date between '1994-01-01' and '1994-12-31';

Result

![image](https://user-images.githubusercontent.com/122611919/220985385-78107e45-8285-4ac2-8aea-796f2fe97afc.png)



Task 22

Question

Employes jadvaldan region NULL bo’lmagan xodimlarni first_name, last_name, title, city,
home_phone ma’lumotlarini first_name Z-A alifbo tartibida qaytaring.

Query

select first_name, last_name, title, city, home_phone from employees where region is not null order by first_name desc;

Result

![image](https://user-images.githubusercontent.com/122611919/220985600-70012cc9-a38f-4057-92fc-ccb7fb81ddbc.png)


Task 23

Question

Orders jadvaldan customer_id ‘VINET’ bo’lgan buyurtmalarni qaytaring.

Query

select * from orders where customer_id = 'VINET';

Result

![image](https://user-images.githubusercontent.com/122611919/220985887-1f2e82d3-7804-430f-9edb-f1e88545b62e.png)


Task 24

Question


Orders jadvaldan order_date ustuni orqali 1996-yildagi ma’lumotlarni qaytaring.

Query

select * from orders where order_date between '1996-01-01' and '1996-12-31';

Result

![image](https://user-images.githubusercontent.com/122611919/220986166-6f0ab6fe-73e9-49c6-a968-928cc6b5cc37.png)


Task 25

Question

Orders jadvaldan ship_region ustun NULL bo’lmagan ma’lumotlarni qaytaring.

Query

select * from orders where ship_region is not null;

Result

![image](https://user-images.githubusercontent.com/122611919/220986504-6551fcce-2892-41d3-9e69-f7b926537403.png)



Task 26

Question

 Orders jadvaldan order_id 10300 va 10400 orasida bo’lgan ma’lumotlarni qaytaring

Query

select * from orders where order_id between 10300 and 10400;

Result

![image](https://user-images.githubusercontent.com/122611919/220986766-a4e9d32e-454a-4b95-95ef-f3d8ba5a28c6.png)


Task 27

Question

Order Details jadvaldan unit_price ustun umumiy qiymatini qaytaring.

Query

select sum(unit_price) from order_details;

Result

![image](https://user-images.githubusercontent.com/122611919/220986935-08bcbf75-aa6d-4fd3-8fb7-bb0a9906b549.png)




