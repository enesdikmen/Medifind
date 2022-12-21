package com.medifind

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.content.Intent
import android.animation.Animator
import android.animation.Animator.AnimatorListener
import android.view.ViewPropertyAnimator
import android.view.animation.LinearInterpolator
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Find the TextView in your layout
        val textView: TextView = findViewById(R.id.mainAppName)

        // Animate the TextView using the ViewPropertyAnimator
        val animator: ViewPropertyAnimator = textView.animate()
            .translationY(-675f)
            .setDuration(2000)
            .setInterpolator(LinearInterpolator())
        animator.start()
        // Set an animation listener to start the next activity when the animation is finished
        animator.setListener(object: AnimatorListener {
            override fun onAnimationStart(animation: Animator) {
            }

            override fun onAnimationEnd(animation: Animator) {
                // Start the next activity when the animation is finished
                startActivity(Intent(this@MainActivity, MedicineSearch::class.java))
            }

            override fun onAnimationCancel(animation: Animator) {
            }

            override fun onAnimationRepeat(animation: Animator) {
            }
        })
    }
}