# StoneHack2019
*Repository for the Stonehill Hackathon 2019 (Srivatsava Missula, Varun Giridhar, Dhruv Venkataraman)*

__Themes:__ Healthcare

__Project description:__ OCR driven application for identifying medications and prompting prescriptions

## Thesis
Over 20,000 people die every year due to medical errors. We approach this problem with three statements:
1. People unable to identify existing medicine at home
2. Consuming the wrong medicines, and experience side effects
3. Patients forgetting their medication schedules

Our solution is an app of two key features: identifying medications and enforcing prescriptions. 

## Implementation
Our project uses an __iOS application__ (coded in Swift) to take user input in the form of images: either prescriptions or medications themselves.

The image is put through __OCR__ (Optical Character Recognition). Medications are compared with an internal database (of stockpiled medicine) to return descriptions, expiration dates, recommended dosages, and where to find it.

Prescriptions are converted by OCR and sent to a __Firebase__ database. A python server retrieves this data, and uses it to map the medications to timestamps.
This data is sent back to the app, and linked to a user's Google Calendar, SMS Messenger and even Google Home, creating an active schedule to ensure appropriate medication.

## Components
The project chiefly functions at three levels: the Swift application, the Firebase database, and the Python server.

### Swift application
The iOS application is coded in Swift, and takes pictures to be processed by OCR.
