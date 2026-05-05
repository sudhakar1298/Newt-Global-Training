package com.commerce.demo.repository;

import com.commerce.demo.model.product;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class ProductRepository {

    private final JdbcTemplate jdbcTemplate;

    public ProductRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public List<product> getAllProducts() {
        String sql = "SELECT * FROM products";

        return jdbcTemplate.query(sql, (rs, rowNum) -> {
            product p = new product();
            p.setId(rs.getInt("id"));
            p.setName(rs.getString("name"));
            p.setPrice(rs.getDouble("price"));
            p.setQuantity(rs.getInt("quantity"));
            return p;
        });
    }

    public void addProduct(product p) {
        String sql = "INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)";
        jdbcTemplate.update(sql,
                p.getName(),
                p.getPrice(),
                p.getQuantity());
    }
}