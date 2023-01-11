package com.medifind

import android.content.Intent
import android.location.Geocoder
import android.os.Bundle
import android.os.PersistableBundle
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.MapView
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import java.util.*

class MapPage : AppCompatActivity(), OnMapReadyCallback {
    private lateinit var map : MapView
    private lateinit var pharmacyName : TextView
    private lateinit var name : String
    private lateinit var cord : String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map_page)

        map = findViewById(R.id.map)
        pharmacyName = findViewById(R.id.pharmacyName)
        name = intent.getStringExtra("name").toString()

        pharmacyName.text = name

        cord = intent.getStringExtra("cord").toString()

        map.getMapAsync(this)
        map.onCreate(savedInstanceState)
    }

    fun goMain(view: View){
        val intent = Intent(this, MedicineSearch::class.java)
        startActivity(intent)
    }

    override fun onMapReady(map: GoogleMap) {
        map.uiSettings.isZoomControlsEnabled = true
        map.uiSettings.isScrollGesturesEnabled = true
        val geocoder = Geocoder(this, Locale.getDefault())
        val addresses = geocoder.getFromLocationName(cord, 1)

        val address = addresses!![0]
        val latLng = LatLng(address.latitude, address.longitude)
        map.addMarker(MarkerOptions().position(latLng).title(name))
        map.moveCamera(CameraUpdateFactory.newLatLngZoom(latLng, 9.0F))

    }

    override fun onStart() {
        super.onStart()
        map.onStart()
    }

    override fun onResume() {
        super.onResume()
        map.onResume()
    }

    override fun onPause() {
        super.onPause()
        map.onPause()
    }

    override fun onStop() {
        super.onStop()
        map.onStop()
    }

    override fun onDestroy() {
        super.onDestroy()
        map.onDestroy()
    }

    override fun onSaveInstanceState(outState: Bundle, outPersistentState: PersistableBundle) {
        super.onSaveInstanceState(outState, outPersistentState)
        map.onSaveInstanceState(outState)
    }

    override fun onLowMemory() {
        super.onLowMemory()
        map.onLowMemory()
    }
}