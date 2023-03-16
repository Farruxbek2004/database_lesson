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


![img_2.png](img_2.png)


-- airports_data


![img_3.png](img_3.png)



-- boarding_passes

![img_4.png](img_4.png)



-- bookings


![img_5.png](img_5.png)


-- flights


![img_6.png](img_6.png)


-- seats


![img_7.png](img_7.png)



-- ticket_flights


![img_8.png](img_8.png)


--     tickets

![img_1.png](img_1.png)
