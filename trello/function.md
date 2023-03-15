-- task 1
```sql
create or replace function value_finder(res varchar)
    returns text
    language plpgsql as

$$
declare
    example varchar;
begin
    select model::json ->> res
    into example
    from aircrafts_data;
    return example;

end;

$$;
```
select value_finder('en');



select value_finder('ru');


![image](https://user-images.githubusercontent.com/122611919/225271280-ef6ca6ce-4f31-4608-a6d8-12114ef17a7d.png)


![image](https://user-images.githubusercontent.com/122611919/225271312-7a416a47-2164-41ce-a128-5c668b0f0a7e.png)
