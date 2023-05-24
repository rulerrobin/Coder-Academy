drop table if exists STUDENTS, teachers, subjects, enrollments;

CREATE TABLE STUDENTS(
student_id serial PRIMARY KEY,
f_name text NOT NULL,
l_name text NOT NULL,
email text NOT NULL,
dob date);

CREATE TABLE TEACHERS(
teacher_id serial PRIMARY KEY,
f_name text NOT NULL,
l_name text NOT NULL);

CREATE TABLE SUBJECTS(
subject_id serial PRIMARY KEY,
subject_name text NOT NULL,
area text DEFAULT 'Databases',
teacher_id integer,
FOREIGN KEY (teacher_id) REFERENCES TEACHERS(teacher_id) ON DELETE SET NULL);

CREATE TABLE ENROLLMENTS(
enrollment_id serial PRIMARY KEY,
student_id integer NOT NULL,
subject_id integer NOT NULL,
enrollment_date date DEFAULT CURRENT_DATE,
FOREIGN KEY (student_id) REFERENCES STUDENTS (student_id) ON DELETE CASCADE,
FOREIGN KEY (subject_id) REFERENCES SUBJECTS (subject_id) ON DELETE CASCADE);

INSERT INTO STUDENTS(f_name, l_name, dob, email) VALUES 
('Ben', 'Allen', '10/21/1990', 'ben.allen@email.com'), 
('Karen', 'Mills', '11/15/1995', 'karen.mills@email.com'), 
('Bob', 'Wall', '10/13/1999', 'bob.wall@email.com'), 
('Julia', 'Richardson', '08/07/2002', 'julia.richardson@email.com'), 
('Simon', 'Hull', '12/04/1993', 'simon.hull@email.com');

INSERT INTO TEACHERS(f_name, l_name) VALUES 
('Martin', 'Roberts'), 
('Belinda', 'White'), 
('Stephanie', 'Knowles');

INSERT INTO SUBJECTS(subject_name, teacher_id, area) VALUES 
('Databases',2, 'Computer Science'), 
('Software Development', 3, 'Computer Science'), 
('Mathematics', 2, 'Computer Science'), 
('Information Technology', 1, 'Comnputer Science');

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
(5, 3);


UPDATE students SET dob = '10/10/1999' WHERE student_id = 1;

INSERT INTO subjects (subject_name) VALUES ('Software Development'); -- added program subject section
 
UPDATE subjects SET subject_name = 'Programming' WHERE subject_name = 'Software Development'; -- changed to software development


-- SELECT f_name, l_name, dob FROM students ORDER BY dob desc; selects students then orders by youngest

-- SELECT student_id FROM students WHERE dob BETWEEN '1/1/1990' AND '1/1/2000'; selects range of people birthday in 90s

-- SELECT student_id FROM students WHERE l_name like 'last%'; MUST PUT LIKE FOR WILDCARDS
-- SELECT dob FROM students ORDER BY dob desc limit 1  selects youngest student also can be || SELECT MAX(dob) FROM STUDENTS;
-- SELECT MIN(enrollment_date), MAX(enrollment_date) FROM enrollments;  selects latest asnd earliest enrollment date

-- SELECT count, subject_name(area) FROM subjects GROUP BY subject_name; Show how many subjects are per area.

-- SELECT subject_id, count(student_id) FROM enrollments GROUP BY subject_id;  || Show how many students are enrolled per subject id.

-- SELECT student_id, count(subject_id) as "Subjects" FROM enrollments GROUP BY student_id; ||Show how many subjects each student is enrolled with alias subjects

--SELECT subject_id, count(student_id) as "Students Enrolled" FROM enrollments GROUP BY subject_id; Show how many students are enrolled in subject 3.

-- SELECT f_name, l_name FROM teachers WHERE teacher_id = (SELECT teacher_id FROM subjects WHERE subject_name = 'Programming' LIMIT 1); Show the full name of the teacher who is teaching the Programming subject (with subquery).

-- select S.subject_name FROM subjects S, enrollments E WHERE S.subject_id = E.subject_id AND E.student_id = 4; || Show the subject names where student 4 is enrolled.

-- SELECT S.f_name, S.l_name, S.email FROM students S, enrollments E WHERE S.student_id = E.student_id AND E.subject_id = 2; ||Show student's full name and email that are enrolled in subject 2.


-- SELECT ST.f_name, ST.l_name, E.enrollment_date, S.subject_name FROM STUDENTS ST, ENROLLMENTS E, SUBJECTS S WHERE ST.student_id = E.student_id AND E.subject_id = S.subject_id;|| Show a list with students full name, enrolment date and subject name.

-- SELECT ST.f_name, ST.l_name, E.enrollment_date, SU.subject_name, T.f_name, T.l_name FROM students ST, enrollments E, subjects SU, teachers T WHERE ST.student_id = E.student_id AND T.teacher_id = SU.teacher_id; || Show a list with students full name, enrolment date, subject name and the teacher's name teaching each subject.

-- SELECT CONCAT(ST.f_name, ST.l_name) as "Student Name", E.enrollment_date, SU.subject_name, CONCAT(T.f_name, T.l_name) as "Teacher'' Name" FROM students ST, enrollments E, subjects SU, teachers T WHERE ST.student_id = E.student_id AND T.teacher_id = SU.teacher_id; 
-- Bonus challenge: In the last query both students and teachers have the same column names. Use an alias to make clear who is who and print first name and last name in the same column
