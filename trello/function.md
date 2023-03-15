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
select value_finder('ru')

![img_2.png](img_2.png)


![img_3.png](img_3.png)