package com.medifind

import android.app.SearchManager
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.AsyncTask
import android.util.Log
import android.widget.*
import org.json.JSONObject
import androidx.appcompat.widget.SearchView
import com.medifind.databinding.ActivityMedicineSearchBinding
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody


class MedicineSearch : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_medicine_search)

        // Create the SearchView
        val medicineSearch = findViewById<SearchView>(R.id.medicine_name)
        val citySearch = findViewById<SearchView>(R.id.city_name)

        // Create the button
        val searchButton = findViewById<Button>(R.id.medicine_search_button)

        // Set the button click listener
        searchButton.setOnClickListener {
            // Get the search query from the SearchView
            val medicineName = medicineSearch.query.toString()
            val cityName = citySearch.query.toString()


            // Create the JSON object
            val jsonObject = JSONObject()

            // Add key-value pairs to the object
            jsonObject.put("medicine_name", medicineName)
            jsonObject.put("city_name", cityName)

            // Perform the search
            val task = SearchTask()
            task.execute(jsonObject)
        }
    }

    inner class SearchTask : AsyncTask<JSONObject, Void, String>() {
        override fun doInBackground(vararg params: JSONObject): String {
            // Build the URL for the search request
            val json = params[0]
            val requestBody = json.toString().toRequestBody("application/json; charset=utf-8".toMediaTypeOrNull())
            val request = Request.Builder().url("https://medifindfunctions.azurewebsites.net/api/search_medicine").post(requestBody).build()

            val client = OkHttpClient()
            val response = client.newCall(request).execute()

            // Read the response from the server
            if (response.code == 200) {
                // The request was successful
                val responseBody = response.body?.string() ?: ""
                val jsonObject = JSONObject(responseBody)
                if(jsonObject.has("medicines")) {
                    val data = jsonObject.getJSONArray("medicines").toString()
                    val intent = Intent(this@MedicineSearch, PharmacyList::class.java)
                    intent.putExtra("medicines", data)
                    startActivity(intent)
                }
                if(jsonObject.has("detail")){
                    val data = jsonObject.getJSONArray("cities").toString()
                    val intent = Intent(this@MedicineSearch, CitiesList::class.java)
                    intent.putExtra("cities", data)
                    intent.putExtra("medicine_name", json.getString("medicine_name"))
                    startActivity(intent)
                }

            } else {
                val responseBody = response.body?.string() ?: ""
                val jsonObject = JSONObject(responseBody)
                Log.d(jsonObject.toString(), "er")
                val data = jsonObject.get("error").toString()
                Log.d(data, "err")
                val intent = Intent(this@MedicineSearch, ErrorPage::class.java)
                intent.putExtra("error", data)
                startActivity(intent)
            }
            return ""
        }

        override fun onPostExecute(result: String) {

        }
    }
}