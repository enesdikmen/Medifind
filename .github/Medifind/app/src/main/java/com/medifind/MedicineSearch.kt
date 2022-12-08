package com.medifind

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MedicineSearch : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_medicine_search)
    }

    // Create the SearchView
    val searchView = findViewById<SearchView>(R.id.search_view)

// Set the listener on the SearchView
    searchView.setOnQueryTextListener(
    object : SearchView.OnQueryTextListener {
        override fun onQueryTextSubmit(query: String): Boolean {
            // This method is called when the user submits their search query

            // Perform the search here
            searchRemoteDatabase(query)

            return true
        }

        override fun onQueryTextChange(newText: String): Boolean {
            // This method is called when the user changes their search query
            return false
        }
    })

    // Create the button
    val searchButton = findViewById<Button>(R.id.search_button)

// Set the button click listener
    searchButton.setOnClickListener
    {
        // Get the search query from the SearchView
        val query = searchView.query.toString()

        // Perform the search
        searchRemoteDatabase(query)
    }

    // Define the function that searches the remote database
    fun searchRemoteDatabase(query: String) {
        // Build the URL for the search request
        val url = URL("https://my-server.com/search?q=" + URLEncoder.encode(query, "UTF-8"))

        // Open the connection and set the request method
        val connection = url.openConnection() as HttpUrlConnection
        connection.requestMethod = "GET"

        // Read the response from the server
        val responseCode = connection.responseCode
        if (responseCode == 200) {
            val inputStream = connection.inputStream
            val response = inputStream.bufferedReader().use { it.readText() }

            // Process the search results
            // (This will depend on the format of the response and how you want to parse it)
            val results = mutableListOf<MyData>()
            // ...

            // Close the input stream and connection
            inputStream.close()

            // Create an Intent to start the new activity
            val intent = Intent(this, ResultsActivity::class.java)

            // Put the search results as an Extra in the Intent
            intent.putExtra("results", results)

            // Start the new activity
            startActivity(intent)

            // Display the search results
            // (This will depend on your specific UI and how you want to show the results)
        }

        // Close the connection
        connection.disconnect()
    }


}

