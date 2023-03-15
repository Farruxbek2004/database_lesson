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

select airports_data_by_zone('Asia/Yakutsk');



![image](https://user-images.githubusercontent.com/122611919/225271019-9594ce8c-ff47-496b-b956-a13a0c7e8cab.png)
