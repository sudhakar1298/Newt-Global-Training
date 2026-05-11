package com.job.springdatajpa.jobjpa;

import com.job.springdatajpa.jobjpa.model.Student;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class JobjpaApplication {

	public static void main(String[] args) {

		ApplicationContext context=SpringApplication.run(JobjpaApplication.class, args);
		StudentRepo repo=context.getBean(StudentRepo.class);
		Student s1= context.getBean(Student.class);
		s1.setRollNo(101);
		s1.setName("Navin");
		s1.setMarks(75);

		repo.save((s1));
	}

}
