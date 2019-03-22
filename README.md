# StoneHack2019
Repository for the Stonehill Hackathon 2019 (Srivatsava Missula, Varun Giridhar, Dhruv Venkataraman)

__Themes:__ Healthcare

__Project description:__ OCR driven application for identifying medications and storing prescriptions

## Problem statement
We face the common problem that incorrect or poorly informed administration of medication often leads to health complications.

## Implementation
Our project uses an __iOS application__ (coded in Swift) to take user input in the form of images: either prescriptions or medications themselves.

Both of these are put through __OCR__ (Optical Character Recognition). Medications are compared with an internal database to return values regarding dosage, and ailments that it treats.
Prescriptions are converted by OCR and sent to a __Firebase__ database. A python server retrieves this data, and uses it to map the medications to timestamps.

This data is sent back to the app, and is also linked to Google Assistant, so you can get alarms, notifications, and reminders.

## Components
