drop table if exists STUDENTS, teachers, subjects, enrollments;

create table STUDENTS(
    student_id serial PRIMARY KEY,
    f_name text NOT NULL,
    l_name text NOT NULL,
    dob date
    );

create table teachers (
    teacher_id serial PRIMARY KEY,

    teacher_name varchar(100)
    );

create table subjects (
    subject_id serial PRIMARY KEY, 

    subject_name varchar(100) not null, 

    teacher_id integer,

    FOREIGN KEY (teacher_id) references teachers (teacher_id) on delete set null
    );

create table enrollments (
    enrollment_id serial PRIMARY KEY,

    subject_id int not null,
    student_id int not null,
    enrollment_date date default current_date,

    FOREIGN KEY (student_id) references students (student_id) on delete cascade,
    FOREIGN KEY (subject_id) references subjects (subject_id) on delete cascade
    );

-- can do all below in terminal but i placed here for reference purposes

INSERT INTO students (f_name, l_name) VALUES 
    ('name 1', 'last 1'),
    ('name 2', 'last 2'),
    ('name 3', 'last 3'),
    ('name 4', 'last 4'),
    ('name 5', 'last 5')
;

INSERT INTO teachers (teacher_name) VALUES
    ('teacher_name 1'),
    ('teacher_name 2'),
    ('teacher_name 3')
;

INSERT INTO subjects (subject_name) VALUES
    ('subject_name 1'),
    ('subject_name 2'),
    ('subject_name 3'),
    ('subject_name 4')
;

INSERT INTO ENROLLMENTS(student_id, subject_id) VALUES
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 2),
    (3, 1),
    (3, 4),
    (4, 1),
    (4, 3),
    (5, 2),
    (5, 3)
;


UPDATE students SET dob = '10/10/1999' WHERE student_id = 1;

INSERT INTO subjects (subject_name) VALUES ('Software Development'); -- added program subject section
 
UPDATE subjects SET subject_name = 'Programming' WHERE subject_name = 'Software Development'; -- changed to software development


-- SELECT f_name, l_name, dob FROM students ORDER BY dob desc; selects students then orders by youngest

-- SELECT student_id FROM students WHERE dob BETWEEN '1/1/1990' AND '1/1/2000'; selects range of people birthday in 90s

-- SELECT student_id FROM students WHERE l_name like 'last%'; MUST PUT LIKE FOR WILDCARDS