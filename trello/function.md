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
select aircraft_code,value_finder('en'), range from aircrafts_data;



select aircraft_code,value_finder('ru'), range from aircrafts_data;


![image](https://user-images.githubusercontent.com/122611919/225286590-0f0e4d74-caf8-438a-b61d-befdf62722aa.png)



![image](https://user-images.githubusercontent.com/122611919/225286778-e4f398c2-855e-4e85-91e1-c16223e81b62.png)
