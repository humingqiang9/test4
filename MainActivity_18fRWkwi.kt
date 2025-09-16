package com.example.myapp

import android.app.Activity
import android.os.Bundle
import android.widget.Toast

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // Display a toast message
        Toast.makeText(this, "Hello from Kotlin Activity!", Toast.LENGTH_SHORT).show()
    }
}