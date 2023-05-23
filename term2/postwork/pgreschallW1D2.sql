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

