task 1

question

From the following table, write a SQL query to find all reviewers whose ratings contain a NULL value. Return reviewer name. 

query

```sql
select rev_name from reviewer
inner join rating using(rev_id)
where rev_stars is null
```

result

![image](https://user-images.githubusercontent.com/122611919/221956678-1c22962f-7f4b-4bfc-9fbf-199e29a3e4ba.png)


task 2

question

From the following table, write a SQL query to find out who was cast in the movie 'Annie Hall'. Return actor first name, last name and role.

query

```sql
select act_fname,act_lname,role
from actor join movie_cast on actor.act_id=movie_cast.act_id
join movie on movie_cast.mov_id=movie.mov_id 
and movie.mov_title='Annie Hall'
```

result

![image](https://user-images.githubusercontent.com/122611919/221957104-2a816b1e-c036-4d3c-adfe-93cae9a85799.png)


task 3


question

From the following table, write a SQL query to find the director who directed a movie that featured a role in 'Eyes Wide Shut'. Return director first name, last name and movie title

query

```sql
SELECT dir_fname, dir_lname, mov_title
FROM  director 
NATURAL JOIN movie_direction
NATURAL JOIN movie
NATURAL JOIN movie_cast
WHERE role IS  NOT NULL
AND mov_title='Eyes Wide Shut'
```

result

![image](https://user-images.githubusercontent.com/122611919/221957327-d5b8c984-da78-4903-8d39-65a24a1894f7.png)


task 4


question

From the following tables, write a SQL query to find the director of a movie that cast a role as Sean Maguire. Return director first name, last name and movie title.

query

```sql
SELECT dir_fname, dir_lname, mov_title
FROM  director, movie_direction, movie, movie_cast
WHERE director.dir_id=movie_direction.dir_id
AND movie_direction.mov_id=movie.mov_id
AND movie.mov_id=movie_cast.mov_id
AND movie_cast.role='Sean Maguire'
```


result

![image](https://user-images.githubusercontent.com/122611919/221957618-3baf5087-cb40-43a0-bbfc-0ba94db2597b.png)


task 5

question

From the following table, write a SQL query to find out which actors have not appeared in any movies between 1990 and 2000 (Begin and end values are included.). Return actor first name, last name, movie title and release year. 


query

```sql
select act_fname, act_lname, mov_title, mov_year
from actor join movie_cast on actor.act_id=movie_cast.act_id
join movie on movie_cast.mov_id=movie.mov_id
where mov_year not between 1990 and 2000
```

result

![image](https://user-images.githubusercontent.com/122611919/221958031-970eaeac-eee3-4bf7-93f9-95ab69484b99.png)


task 6

question

From the following table, write a SQL query to find the directors who have directed films in a variety of genres. Group the result set on director first name, last name and generic title. Sort the result-set in ascending order by director first name and last name. Return director first name, last name and number of genres movies. 

query

```sql
SELECT dir_fname,dir_lname, gen_title,count(gen_title)
FROM director
NATURAL JOIN movie_direction
NATURAL JOIN movie_genres
NATURAL JOIN genres
GROUP BY dir_fname, dir_lname,gen_title
ORDER BY dir_fname,dir_lname
```

result

![image](https://user-images.githubusercontent.com/122611919/221958288-74955fa4-79e7-4906-b621-5ee1b5180978.png)


task 7

question

From the following table, write a SQL query to find the movies with year and genres. Return movie title, movie year and generic title.

query

```sql
SELECT mov_title, mov_year, gen_title
FROM movie
NATURAL JOIN movie_genres
NATURAL JOIN genres
```

result

![image](https://user-images.githubusercontent.com/122611919/221958516-50ea2243-edfc-46b5-b39b-98b378d825c3.png)


task 8

question

From the following tables, write a SQL query to find all the movies with year, genres, and name of the director.

query

```sql
SELECT mov_title, mov_year, gen_title, dir_fname, dir_lname
FROM movie
NATURAL JOIN movie_genres
NATURAL JOIN genres
NATURAL JOIN movie_direction
NATURAL JOIN director
```


result

![image](https://user-images.githubusercontent.com/122611919/221958747-159a5b1c-2ed2-4836-97d5-2ad4460ff1fc.png)


task 9

question

From the following tables, write a SQL query to find the movies released before 1st January 1989. Sort the result-set in descending order by date of release. Return movie title, release year, date of release, duration, and first and last name of the director.


query

```sql
SELECT movie.mov_title, mov_year, mov_dt_rel,
mov_time,dir_fname, dir_lname 
FROM movie
JOIN  movie_direction 
ON movie.mov_id = movie_direction.mov_id
JOIN director 
ON movie_direction.dir_id=director.dir_id
WHERE mov_dt_rel <'01/01/1989'
ORDER BY mov_dt_rel desc
```

result

![image](https://user-images.githubusercontent.com/122611919/221959126-81f8bb9d-8368-4f73-903e-1365eaa7a901.png)


task 10

question

From the following table, write a SQL query to calculate the average movie length and count the number of movies in each genre. Return genre title, average time and number of movies for each genre.

query

```sql
SELECT gen_title, AVG(mov_time), COUNT(gen_title) 
FROM movie
NATURAL JOIN  movie_genres
NATURAL JOIN  genres
GROUP BY gen_title
```

result

![image](https://user-images.githubusercontent.com/122611919/221959312-93543369-dcc7-4fcb-b57b-31b187c112d6.png)


task 11

question

From the following table, write a SQL query to find movies with the shortest duration. Return movie title, movie year, director first name, last name, actor first name, last name and role. 

query

```sql
SELECT mov_title, mov_year, dir_fname, dir_lname, 
act_fname, act_lname, role 
FROM  movie
NATURAL JOIN movie_direction
NATURAL JOIN movie_cast
NATURAL JOIN director
NATURAL JOIN actor
WHERE mov_time=(SELECT MIN(mov_time) FROM movie)
```

result

![image](https://user-images.githubusercontent.com/122611919/221959575-61aca6a4-6570-472b-8439-e864b3838dc4.png)


task 12

question

From the following table, write a SQL query to find the years in which a movie received a rating of 3 or 4. Sort the result in increasing order on movie year.

query

```sql
SELECT DISTINCT mov_year
FROM movie
INNER JOIN rating 
ON movie.mov_id = rating.mov_id
WHERE rev_stars IN (3, 4)
ORDER BY mov_year
```

result

![image](https://user-images.githubusercontent.com/122611919/221960185-e81b8a6c-b64d-4551-a107-e20016c90c14.png)


task 13

question

From the following tables, write a SQL query to get the reviewer name, movie title, and stars in an order that reviewer name will come first, then by movie title, and lastly by number of stars. 

query

```sql
SELECT rev_name, mov_title, rev_stars
FROM movie
INNER JOIN rating ON movie.mov_id = rating.mov_id
INNER JOIN reviewer ON reviewer.rev_id = rating.rev_id
WHERE rev_name IS NOT NULL
ORDER BY rev_name, mov_title, rev_stars
```

result

![image](https://user-images.githubusercontent.com/122611919/221960482-85252590-d674-40b1-a473-a579e3c7865a.png)


task 14

question

From the following table, write a SQL query to find those movies that have at least one rating and received the most stars. Sort the result-set on movie title. Return movie title and maximum review stars. 


query

```sql
SELECT mov_title, MAX(rev_stars)
FROM movie
INNER JOIN rating USING(mov_id)
GROUP BY mov_title 
HAVING MAX(rev_stars)>0
ORDER BY mov_title
```

result

![image](https://user-images.githubusercontent.com/122611919/221960750-0b2766d5-9445-4983-9b13-b1f60ce14dd0.png)


task 15

question

From the following table, write a SQL query to find out which movies have received ratings. Return movie title, director first name, director last name and review stars.

query

```sql
SELECT mov_title, dir_fname,dir_lname, rev_stars
FROM Movie
JOIN movie_direction USING(mov_id)
join director using (dir_id)
left join rating using(mov_id)
where rev_stars is not null
```


result

![image](https://user-images.githubusercontent.com/122611919/221961026-7afb2d27-b788-4bf4-a555-451c27e31caf.png)


task 16

question

From the following table, write a SQL query to find movies in which one or more actors have acted in more than one film. Return movie title, actor first and last name, and the role

query

```sql
SELECT mov_title, act_fname, act_lname, role
FROM movie 
JOIN movie_cast 
ON movie_cast.mov_id=movie.mov_id 
JOIN actor 
ON movie_cast.act_id=actor.act_id
WHERE actor.act_id IN (
SELECT act_id 
FROM movie_cast 
GROUP BY act_id HAVING COUNT(*)>=2)
```


result

![image](https://user-images.githubusercontent.com/122611919/221961281-d5557bf8-347e-4ef7-8453-0f195f720d50.png)


task 17

question


From the following tables, write a SQL query to find the actor whose first name is 'Claire' and last name is 'Danes'. Return director first name, last name, movie title, actor first name and last name, role. 

query

```sql
SELECT dir_fname, dir_lname, mov_title, act_fname, act_lname, role
FROM actor
JOIN movie_cast 
ON actor.act_id=movie_cast.act_id
JOIN movie_direction 
ON movie_cast.mov_id=movie_direction.mov_id
JOIN director 
ON movie_direction.dir_id=director.dir_id
JOIN movie 
ON movie.mov_id=movie_direction.mov_id
WHERE act_fname='Claire' 
AND act_lname='Danes'
```

result

![image](https://user-images.githubusercontent.com/122611919/221961625-a17ac480-4c4a-4b5a-b683-4047ce6f6f33.png)

task 18

question

From the following table, write a SQL query to find for actors whose films have been directed by them. Return actor first name, last name, movie title and role.

query

```sql
SELECT act_fname, act_lname, mov_title, role
FROM actor
JOIN movie_cast 
ON actor.act_id=movie_cast.act_id
JOIN movie_direction 
ON movie_cast.mov_id=movie_direction.mov_id
JOIN director 
ON movie_direction.dir_id=director.dir_id
JOIN movie 
ON movie.mov_id=movie_direction.mov_id
WHERE act_fname=dir_fname 
AND act_lname=dir_lname
```

result

![image](https://user-images.githubusercontent.com/122611919/221961889-ce44216a-fede-43a1-b354-87bbb89fa43f.png)


task 19

question

From the following tables, write a SQL query to find the cast list of the movie ‘Chinatown’. Return first name, last name

query

```sql
SELECT a.act_fname, a.act_lname
FROM
movie_cast c
JOIN actor a ON
c.act_id = a.act_id
Where mov_id = (
SELECT mov_id
FROM movie
Where mov_title = 'Chinatown')
```


result

![image](https://user-images.githubusercontent.com/122611919/221962407-b52db35f-64bc-47ff-a539-6f4ad8352681.png)


task 20

question


From the following tables, write a SQL query to find those movies where actor’s first name is 'Harrison' and last name is 'Ford'. Return movie title

query

```sql
SELECT m.mov_title
FROM  movie m
JOIN movie_cast c 
ON  m.mov_id = c.mov_id
WHERE c.act_id IN ( 
Select act_id 
FROM actor 
WHERE act_fname='Harrison' 
AND act_lname='Ford')
```

result

![image](https://user-images.githubusercontent.com/122611919/221962604-cce652e3-fa2a-4407-a4ac-39c5facdbd07.png)


task 21

question

From the following tables, write a SQL query to find the highest-rated movies. Return movie title, movie year, review stars and releasing country

query

```sql
SELECT mov_title, mov_year, rev_stars, mov_rel_country
FROM movie 
NATURAL JOIN rating
WHERE rev_stars = (
SELECT MAX(rev_stars)
FROM rating)
```

result

![image](https://user-images.githubusercontent.com/122611919/221962851-65349785-4861-4832-a5e6-b4adbd02fc49.png)


task 22

question

From the following tables, write a SQL query to find the highest-rated ‘Mystery Movies’. Return the title, year, and rating

query

```sql
SELECT mov_title, mov_year, rev_stars
FROM movie 
NATURAL JOIN movie_genres 
NATURAL JOIN genres 
NATURAL JOIN rating
WHERE gen_title = 'Mystery' AND rev_stars >= ALL (
SELECT rev_stars
FROM rating 
NATURAL JOIN movie_genres 
NATURAL JOIN genres
WHERE gen_title = 'Mystery')
```

result

![image](https://user-images.githubusercontent.com/122611919/221963157-6ecae38e-955d-4001-9f1b-a3072fb750bb.png)


task 23

question

From the following tables, write a SQL query to find the years when most of the ‘Mystery Movies’ produced. Count the number of generic title and compute their average rating. Group the result set on movie release year, generic title. Return movie year, generic title, number of generic title and average rating.

query

```sql
SELECT mov_year,gen_title,count(gen_title), avg(rev_stars)
FROM movie 
NATURAL JOIN movie_genres 
NATURAL JOIN genres
NATURAL JOIN rating
WHERE gen_title='Mystery' 
GROUP BY mov_year,gen_title
```

result

![image](https://user-images.githubusercontent.com/122611919/221963350-c392d305-eac7-4316-8e98-d682cc88d880.png)


task 24

question

From the following tables, write a query in SQL to generate a report, which contain the fields movie title, name of the female actor, year of the movie, role, movie genres, the director, date of release, and rating of that movie

query

```sql
SELECT mov_title, act_fname, act_lname, 
mov_year, role, gen_title, dir_fname, dir_lname, 
mov_dt_rel, rev_stars
FROM movie 
NATURAL JOIN movie_cast
NATURAL JOIN actor
NATURAL JOIN movie_genres
NATURAL JOIN genres
NATURAL JOIN movie_direction
NATURAL JOIN director
NATURAL JOIN rating
WHERE act_gender='F'
```

result

![image](https://user-images.githubusercontent.com/122611919/221963632-6043a031-cf3b-406e-b57b-bc94e2a8d2c0.png)



