package com.medifind


import android.view.View
import android.view.ViewGroup
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.*
import androidx.test.espresso.assertion.ViewAssertions.*
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.filters.LargeTest
import org.hamcrest.Description
import org.hamcrest.Matcher
import org.hamcrest.Matchers.allOf
import org.hamcrest.TypeSafeMatcher
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@LargeTest
@RunWith(AndroidJUnit4::class)
class MedicineFoundTest {

    @Rule
    @JvmField
    var mActivityScenarioRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun medicineFoundTest() {
        val searchAutoComplete = onView(
            allOf(
                withId(androidx.preference.R.id.search_src_text),
                childAtPosition(
                    allOf(
                        withId(androidx.preference.R.id.search_plate),
                        childAtPosition(
                            withId(androidx.preference.R.id.search_edit_frame),
                            1
                        )
                    ),
                    0
                ),
                isDisplayed(),
                withContentDescription("MedicineSearch")
            )
        )
        searchAutoComplete.perform(replaceText("Parol"), closeSoftKeyboard())

        val searchAutoComplete2 = onView(
            allOf(
                withId(androidx.preference.R.id.search_src_text),
                childAtPosition(
                    allOf(
                        withId(androidx.preference.R.id.search_plate),
                        childAtPosition(
                            withId(androidx.preference.R.id.search_edit_frame),
                            1
                        )
                    ),
                    0
                ),
                isDisplayed(),
                withContentDescription("CitySearch")
            )
        )
        searchAutoComplete2.perform(replaceText("istanbul"), closeSoftKeyboard())

        val materialButton = onView(
            allOf(
                withId(R.id.medicine_search_button), withText("Search"),
                childAtPosition(
                    childAtPosition(
                        withId(android.R.id.content),
                        0
                    ),
                    5
                ),
                isDisplayed()
            )
        )
        materialButton.perform(click())

        val textView = onView(
            allOf(
                withId(R.id.textView3), withText("Pharmacies"),
                withParent(withParent(withId(android.R.id.content))),
                isDisplayed()
            )
        )
        textView.check(matches(withText("Pharmacies")))
    }

    private fun childAtPosition(
        parentMatcher: Matcher<View>, position: Int
    ): Matcher<View> {

        return object : TypeSafeMatcher<View>() {
            override fun describeTo(description: Description) {
                description.appendText("Child at position $position in parent ")
                parentMatcher.describeTo(description)
            }

            public override fun matchesSafely(view: View): Boolean {
                val parent = view.parent
                return parent is ViewGroup && parentMatcher.matches(parent)
                        && view == parent.getChildAt(position)
            }
        }
    }
}
