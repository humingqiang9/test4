package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class RandomController {
    
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello from Spring Boot!";
    }
    
    @GetMapping("/greeting")
    public String getGreeting() {
        return "Welcome to our Spring Boot application!";
    }
}