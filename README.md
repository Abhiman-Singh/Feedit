# FeedIt
Really Simple Syndication(RSS) Feed Reader App

## Link
- https://rssdatabase-e9c06.web.app/

## Overview

The RSS(Really Simple Syndication) Feed Reader is a cross-platform application built using Flutter, designed to fetch and categorize RSS feed data into text, audio, and video types. This app allows users to view headlines, images, and small descriptions for each feed, manage RSS links, and enjoy seamless functionality across Windows, Android, iOS, and web platforms.

## Features
- **RSS Feed Categorization:** Automatically classifies feeds into text, audio, and video types.
- **Custom RSS Links:** Users can add, name, and delete custom RSS links via a pop-up window.
- **Firebase Integration:** Login and Sign-up functionality using Firebase Authentication.User-specific data stored in Firestore, including sub-collections for added RSS links.
- **Interactive UI:** Tab-based navigation for filtering feeds and floating action buttons for link management.
- **Responsive Design:** Optimized for multiple platforms.
- **Dark and Light Mode:** Toggle between dark and light themes using a theme button.
- **Persistent Storage:** Backend data stored in Firebase for reliable access and synchronization.

## Screenshots
- Android and IOS
  
- Web
  

## Tech Stack
- **Flutter:** Cross-platform development framework.
- **Firebase:** Authentication and backend database.
- **Dart:** Programming language for Flutter.
- **HTTP:** Library for API calls and data fetching.


## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Abhiman-Singh/Feedit.git
2. Navigate to the project directory:
   ```bash
   cd rss-feed-reader
3. Install dependencies:
   ```bash
   flutter pub get
4. Configure Firebase:
   - Set up a Firebase project.
   - Add Firebase configuration files (google-services.json for Android and GoogleService-Info.plist for iOS).
   - Enable Firebase Authentication and Firestore.
5. Run the Application:
   ```bash
   flutter run

## Usage
- **Login/Sign-Up:** Use Firebase Authentication to log in or sign up.
- **Add RSS Links:** Click the floating action button to open the pop-up window.Enter a custom name and URL for the RSS feed.
- **View Feeds:** Feeds are categorized into text, audio, and video tabs.Browse feeds with headline, image, and description displayed on cards.
- **Manage Links:** Delete unwanted RSS links via the pop-up window.
- **Toggle Theme:** Use the theme button to switch between dark and light modes.

## Dependencies
- **Flutter SDK:** Cross-platform development.
- **Firebase Authentication:** User authentication.
- **Firebase Firestore:** Backend data storage.
- **HTTP:** Fetching RSS feed data.

