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






