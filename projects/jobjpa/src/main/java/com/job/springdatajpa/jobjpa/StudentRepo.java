package com.job.springdatajpa.jobjpa;


import com.job.springdatajpa.jobjpa.model.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;



@Repository
public interface StudentRepo extends JpaRepository<Student, Integer> {

}