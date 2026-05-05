package com.commerce.demo.service;

import com.commerce.demo.model.product;
import com.commerce.demo.repository.ProductRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class pservice {

    private final ProductRepository repository;

    public pservice(ProductRepository repository) {
        this.repository = repository;
    }

    public List<product> getProducts() {
        return repository.getAllProducts();
    }

    public String createProduct(product product) {
        repository.addProduct(product);
        return "Product added successfully!";
    }
}