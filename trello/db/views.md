--  1
```sql
create or replace view ticket_and_flights_data as
select ticket_no,
       tf.flight_id,
       f.flight_no,
       f.aircraft_code,
       amount
from ticket_flights tf
         inner join flights f on f.flight_id = tf.flight_id
where f.flight_no like '%6';

select * from ticket_and_flights_data;
```
--  2
```sql
create or replace view ticket_and_flights_and_boarding_passes_data as
select ticket_no,
       f.flight_id,
       bp.seat_no,
       bp.boarding_no

from flights f
         inner join boarding_passes bp on f.flight_id = bp.flight_id
where seat_no like '%F';


select * from ticket_and_flights_data;
```
--  3
```sql
create or replace view views_aircrafts_by_seats as
select
    ai.aircraft_code,
    ai.model,
    se.seat_no,
    se.fare_conditions
    from aircrafts_data ai
    inner join seats se on ai.aircraft_code = se.aircraft_code;


select * from views_aircrafts_by_seats
```
-- 4
```sql
create or replace view boarding_ticket_flights_and_ticket as
    select bo.ticket_no,
           ti.fare_conditions,
           ti.amount,
           t.passenger_name,
           t.passenger_id

    from boarding_passes bo inner join ticket_flights ti on bo.ticket_no = ti.ticket_no
    inner join tickets t on t.ticket_no = ti.ticket_no
    where ti.fare_conditions = 'Economy';

select * from boarding_ticket_flights_and_ticket
```

-- 5
```sql
create or replace view employee_territories_employees_views as
    select
        em.employee_id,
        e.city,
        e.country,
        em.territory_id
    from employee_territories em inner join employees e on e.employee_id = em.employee_id
    where country = 'USA';


select * from employee_territories_employees_views;
```