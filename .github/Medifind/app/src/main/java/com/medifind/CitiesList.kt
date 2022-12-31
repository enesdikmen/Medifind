package com.medifind

import android.content.Context
import android.content.Intent
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.core.content.ContextCompat.startActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.medifind.databinding.CityItemBinding
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONArray
import org.json.JSONObject

class CitiesList : AppCompatActivity() {
    private lateinit var jsonArray: JSONArray
    private lateinit var recyclerView: RecyclerView
    private lateinit var adapter: CityListAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_cities_list)
        recyclerView = findViewById(R.id.cityList)
        recyclerView.layoutManager = LinearLayoutManager(this)

        jsonArray = intent.getStringExtra("cities")?.let { JSONArray(it) } ?: JSONArray()

        var medicine_name = intent.getStringExtra("medicine_name").toString()


        Log.d(jsonArray.toString(), "hello")

        adapter = CityListAdapter(jsonArray, medicine_name, this)
        recyclerView.adapter = adapter
    }
}

class SearchTask(private val context: Context) : AsyncTask<JSONObject, Void, String>() {
    override fun doInBackground(vararg params: JSONObject): String {
        // Build the URL for the search request
        val json = params[0]
        val requestBody =
            json.toString().toRequestBody("application/json; charset=utf-8".toMediaTypeOrNull())
        val request =
            Request.Builder().url("https://medifindfunctions.azurewebsites.net/api/search_medicine")
                .post(requestBody).build()
        Log.d(json.toString(), "hi")

        val client = OkHttpClient()
        val response = client.newCall(request).execute()

        // Read the response from the server
        if (response.code == 200) {
            // The request was successful
            val responseBody = response.body?.string() ?: ""
            val jsonObject = JSONObject(responseBody)
            if (jsonObject.has("medicines")) {
                val data = jsonObject.getJSONArray("medicines").toString()
                val intent = Intent(context, PharmacyList::class.java)
                intent.putExtra("medicines", data)
                context.startActivity(intent)

            } else {
                // The request was unsuccessful
                return ""
            }
            return ""
        }

        fun onPostExecute(result: String) {

        }
        return ""
    }
}

class CityListAdapter(private val jsonArray: JSONArray, private val medicine_name: String, private val context: Context) : RecyclerView.Adapter<CityListAdapter.ViewHolder>(), View.OnClickListener {

    class ViewHolder(val binding: CityItemBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = CityItemBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.itemView.setOnClickListener(this)
        holder.itemView.tag = position
        val item = jsonArray.getString(position)
        Log.d(item.toString(), "hello2")
        holder.binding.cityItemName.text = item
    }


    override fun getItemCount(): Int {
        return jsonArray.length()
    }

    override fun onClick(view: View) {
        val position = view.tag as Int
        val item = jsonArray.getString(position)
        val jsonObject = JSONObject()

        jsonObject.put("medicine_name", medicine_name)
        jsonObject.put("city_name", item.toString())

        // Perform the search
        val task = SearchTask(context)
        task.execute(jsonObject)
    }

}