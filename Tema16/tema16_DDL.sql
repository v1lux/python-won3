create table class (
	id serial primary key,
	class_nr smallint not null,
	class_letter varchar(1) not null
);

create table student (
	id serial primary key,
	name varchar(30),
	class_id smallint not null,
	foreign key (class_id) references class(id)
);

create table grades (
	id serial primary key,
	student_id int not null,
	grades smallint,
	foreign key (student_id) references student(id)
);
