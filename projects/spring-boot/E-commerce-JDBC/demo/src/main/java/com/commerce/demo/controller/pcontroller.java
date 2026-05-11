package com.commerce.demo.controller;

import com.commerce.demo.model.product;
import com.commerce.demo.service.pservice;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/products")
public class pcontroller {

    private final pservice service;

    public pcontroller(pservice service) {

        this.service = service;
    }

    @GetMapping("/")
    public String home(Model model) {

        model.addAttribute("products", service.getProducts());

        return "index";
    }

    @PostMapping("/add")
    public String addProduct(@ModelAttribute product p) {

        service.saveProduct(p);

        return "redirect:/products/";
    }
    @PostMapping("/buy")
    public String removeProduct(@ModelAttribute product p)
    {
        service.removeProduct(p);
        return "redirect:/products/";
    }
    @PostMapping("/addp")
    public String iproduct(@ModelAttribute product p) {

        service.increaseproquantity(p);

        return "redirect:/products/";
    }


}