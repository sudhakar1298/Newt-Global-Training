package com.JobApp.controller;

import com.JobApp.model.JobPost;
import com.JobApp.service.JobService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class JobController {
    @Autowired
    private JobService service;

    @GetMapping({"/", "home"})
    public String home() {
        return "home";
    }

    @GetMapping("addjob")
    public String addJob() {
        return "addjob";
    }

    @PostMapping("handleForm")
    public String handleForm(JobPost jobPost,Model model) {
        service.addJob(jobPost);
        model.addAttribute("jobPost", jobPost);
        return "success";
    }
    @GetMapping("jobPosts/keyword/{keyword}")
    public List<JobPost> searchByKeyword(@PathVariable("keyword") String keyword) {
        return service.serach(keyword);
    }
    @GetMapping("viewalljobs")
    public String viewJobs(Model m) {
        List<JobPost> jobs = service.getAllJobs();
        m.addAttribute("jobPosts", jobs);
        return "viewalljobs";
    }
    @DeleteMapping("jobPost/{postId}")
    public String deleteJob(@PathVariable int postId)
    {
        service.deleteJob(postId);
        return "Deleted";
    }


        @GetMapping("load")
    public String loadData() {
        service.load();
        return "viewalljobs;";
    }
}
