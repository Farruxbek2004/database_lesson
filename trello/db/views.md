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


![image](https://user-images.githubusercontent.com/122611919/225826947-ddd73b38-5699-4f87-9500-5944da812633.png)



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
