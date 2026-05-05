package com.commerce.demo.controller;


import com.commerce.demo.model.product;
import com.commerce.demo.service.pservice;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/products")
public class pcontroller {

    private final pservice service;

    public pcontroller(pservice service) {
        this.service = service;
    }

    @GetMapping
    public List<product> getAllProducts() {
        return service.getProducts();
    }

    @PostMapping
    public String addProduct(@RequestBody product product) {
        return service.createProduct(product);
    }
}