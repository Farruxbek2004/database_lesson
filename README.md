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







