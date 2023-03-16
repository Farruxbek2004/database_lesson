```sql
-- aircrafts_data
create or replace trigger airport_update_and_delete_trigger
    after update or delete
    on aircrafts_data
    for each row
execute procedure aicrafts_update_and_delete_trigger_func();

-- airports_data
create or replace trigger airport_update_trigger
    after update or delete
    on airports_data
    for each row
execute procedure airport_update_and_delete_trigger_func();

-- boarding_passes
create or replace trigger boarding_passes_update_delete_trigger
    after update or delete
    on boarding_passes
    for each row
execute procedure airport_update_and_delete_trigger_func();

-- bookings

create or replace trigger bookings_update_delete_trigger
    after update or delete
    on bookings
    for each row
execute procedure airport_update_and_delete_trigger_func();


-- flights

create or replace trigger flights_update_delete_trigger
    after update or delete
    on flights
    for each row
execute procedure airport_update_and_delete_trigger_func();

-- seats

create or replace trigger seats_update_delete_trigger
    after update or delete
    on seats
    for each row
execute procedure airport_update_and_delete_trigger_func();

-- ticket_flights

create or replace trigger ticket_flights_update_delete_trigger
    after update or delete
    on ticket_flights
    for each row
execute procedure airport_update_and_delete_trigger_func();

-- tickets
create or replace trigger tickets_update_delete_trigger
    after update or delete
    on tickets
    for each row
execute procedure airport_update_and_delete_trigger_func();

```

```sql
create table logs
(
    id         serial primary key,
    name       varchar(255),
    detail     text,
    old_data   json,
    new_data   json,
    table_name varchar(255)
);
create or replace function airport_update_and_delete_trigger_func()
    returns trigger
    language plpgsql
as
$$
declare
    value text := 'bookings';
BEGIN
    if tg_op = 'UPDATE' THEN
        insert into logs(detail, old_data, new_data, table_name)
        values ('Updated.', row_to_json(OLD), row_to_json(NEW),value );
        return NEW;
    elsif tg_op ='DELETE' THEN
        insert into logs(detail, old_data, table_name)
        values ('DELETED.', row_to_json(OLD),value);
        return OLD;
    END IF;
end;
$$;

```

--     aircrafts_data


![image](https://user-images.githubusercontent.com/122611919/225611618-f29d741d-916f-41cb-9537-f70b324ee97c.png)



-- airports_data


![image](https://user-images.githubusercontent.com/122611919/225611941-b2263104-7b03-47a0-83da-44949c50c0dc.png)




-- boarding_passes



![image](https://user-images.githubusercontent.com/122611919/225612276-c5b7777b-f30f-4c2c-9215-a97ad07f25de.png)


-- bookings


![image](https://user-images.githubusercontent.com/122611919/225612733-d4ce7f27-cdf9-4838-b274-45da15b3f531.png)



-- flights


![image](https://user-images.githubusercontent.com/122611919/225613080-295df043-5018-4244-8875-d7a76cd3b5a2.png)



-- seats


![image](https://user-images.githubusercontent.com/122611919/225613409-e4b6e134-83e2-448c-95ef-b412c8d75ba2.png)




-- ticket_flights



--     tickets

![img_1.png](img_1.png)
