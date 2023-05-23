-- drop table categories;

create table categories(
    id serial primary key,
    
    name varchar(100) not null, 
    description text
);

create table if not exists items (
    id serial primary key,

    name varchar(100) not null,
    description text not null,
    category_id integer not null, -- because not primary key needs to state type

    -- FK has to be at the end, usually FK's all listed at the end after columns
    foreign key (category_id) references categories (id)-- key (local column) reference table (local column of other table))
)