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


![image](https://user-images.githubusercontent.com/122611919/225272001-fe959608-13a5-4cce-862d-409eb97c68a9.png)

