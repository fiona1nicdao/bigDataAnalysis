CREATE TABLE food_macros (
    id uuid,
    title ascii,
    rating float,
    calories int,
    protein int,
    fat int,
    sodium int,
    PRIMARY KEY ((id))
);

insert into student (id, title ascii, rating, calories, protein, fat, sodium) values ();

select * from food_macros;
DESCRIBE tables;
SELECT COUNT(*) FROM food_macros;
DROP TABLE food_macros;

docker exec -it cass_cluster cqlsh
DESCRIBE KEYSPACES
USE epi_data;