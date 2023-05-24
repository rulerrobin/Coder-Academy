drop table if exists items, categories;

create table if not exists categories(
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
    foreign key (category_id) references categories (id) on delete cascade-- key (local column) reference table (local column of other table))
    -- if a row in the "categories" table is deleted, all related rows in the current table with the foreign key constraint will also be deleted automatically.
);

-- truncate items, categories;

insert into categories (name, description) values 
    ('Electronics', 'Gadgets to make life easier'),
    ('Car Parts', 'Expensive stuff for your car'),
    ('Sports', 'Get out and play!'),
    ('Video Games', 'Stay in and play!');

INSERT INTO items (name, description, category_id) values 
    ('Skyrim', 'Awesome open-world RPG', 4),
    ('Word of Warcraft', 'Popular MMORPG', 4),
    ('iPhone', 'Apple''s flagship smartphone', 1), -- to do single quote double it
    ('Greg Normal gold clubs', 'At least you can look like a pro', 3)
    ; 
-- cat id has to be included because not null and also has to be existing as it takes as a foreign key

-- cat id's are sure because tables are dropped at the start (reset counter) but can just use select * to check