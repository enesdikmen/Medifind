package com.medifind

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView
import org.json.JSONArray

class ErrorPage : AppCompatActivity() {
    private lateinit var textView: TextView
    private lateinit var errorText: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_error_page)

        val textView = findViewById<TextView>(R.id.errorText)

        errorText = intent.getStringExtra("error").toString()

        textView.text = errorText


    }

    fun goMain(view: View){
        val intent = Intent(this, MedicineSearch::class.java)
        startActivity(intent)
    }
}