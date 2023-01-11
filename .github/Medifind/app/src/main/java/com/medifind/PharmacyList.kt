package com.medifind

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.medifind.databinding.ItemListBinding
import org.json.JSONArray

class PharmacyList : AppCompatActivity() {
    private lateinit var jsonArray: JSONArray
    private lateinit var recyclerView: RecyclerView
    private lateinit var adapter: PharmacyListAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_pharmacy_list)
        recyclerView = findViewById(R.id.pharmacyList)
        recyclerView.layoutManager = LinearLayoutManager(this)

        jsonArray = intent.getStringExtra("medicines")?.let { JSONArray(it) } ?: JSONArray()


        adapter = PharmacyListAdapter(jsonArray, this)
        recyclerView.adapter = adapter
    }

    fun goMain(view: View){
        val intent = Intent(this, MedicineSearch::class.java)
        startActivity(intent)
    }

}

class PharmacyListAdapter(private val jsonArray: JSONArray, private val context: Context) : RecyclerView.Adapter<PharmacyListAdapter.ViewHolder>(), View.OnClickListener {

    class ViewHolder(val binding: ItemListBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemListBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.itemView.setOnClickListener(this)
        holder.itemView.tag = position
        val item = jsonArray.getJSONObject(position)
        holder.binding.listText.text = item.getString("pharmacy_name")
    }

    override fun getItemCount(): Int {
        return jsonArray.length()
    }

    override fun onClick(view: View) {
        val position = view.tag as Int
        val item = jsonArray.getJSONObject(position)

        val intent = Intent(context, MapPage::class.java)
        intent.putExtra("name", item.getString("pharmacy_name"))
        intent.putExtra("cord", item.getString("pharmacy_address"))
        context.startActivity(intent)

    }
}


