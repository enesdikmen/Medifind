package com.medifind

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class PharmacyList : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_pharmacy_list)
    }

    val results = intent.getParcelableArrayListExtra<MyData>("results")

    // Set the adapter on the item list
    val listView = findViewById<ListView>(R.id.list_view)
    val adapter = MyAdapter(this, results)
    listView.adapter = adapter
}