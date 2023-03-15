-- task 3

```sql
create or replace function airports_data_by_upper(res varchar)
    returns text
    language plpgsql as

$$
declare
    example varchar;
begin
    select city::json ->> res
    into example
    from airports_data;
    return upper(example);
end;
$$;
```

select airports_data_by_upper('en')


![img_1.png](img_1.png)
