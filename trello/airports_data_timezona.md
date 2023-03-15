-- task 2

```sql
create function airports_data_by_zone(value character varying)
    returns SETOF airports_data
    language plpgsql
as
$$
begin
    return query select * from airports_data where timezone = value;
end;

$$;
```

![img.png](img.png)