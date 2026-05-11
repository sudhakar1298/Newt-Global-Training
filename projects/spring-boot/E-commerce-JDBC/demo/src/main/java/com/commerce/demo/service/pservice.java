package com.commerce.demo.service;

import com.commerce.demo.model.product;
import com.commerce.demo.repository.ProductRepository;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;

@Service
public class pservice {

    @Autowired
    private final ProductRepository repository;

    public pservice(ProductRepository repository) {
        this.repository = repository;
    }

    public List<product> getProducts() {
        return repository.getAllProducts();
    }

    public String createProduct(product p) {
        repository.addProduct(p);
        return "Product added successfully!";
    }
    public void saveProduct(product p) {
        repository.addProduct(p);
    }

    public void removeProduct(product p) {
        repository.rem(p);
    }

    public void increaseproquantity(product p) {
        repository.inc(p);
    }
}