package com.data.rest.job.data.rest.repo;


import com.data.rest.job.data.rest.model.JobPost;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;



@Repository
public interface JobRepo extends JpaRepository<JobPost, Integer> {

    //List<JobPost> findByPostProfileContainingOrPostDescContaining(String postProfile, String postDesc);


}