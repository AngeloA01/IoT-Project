import { initializeApp } from "firebase/app";
import { getDatabase, ref, set } from "firebase/database";

var firebaseConfig = {
  apiKey: "AIzaSyAz1R9Y4rgIUDR4TINqXvG2BbjZGzlWbXs",
  authDomain: "embedded-lab-2-part-2.firebaseapp.com",
  databaseURL: "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "embedded-lab-2-part-2",
  storageBucket: "embedded-lab-2-part-2.appspot.com",
  messagingSenderId: "164614426559",
  appId: "1:164614426559:web:cf7044cee5ca58327adb0a",
  measurementId: "G-FNKN7NGVYY"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);

function writeUserData(userId, name) {
  const db = getDatabase();
  set(ref(db, 'users/'), {
    username: name,
  });
}

writeUserData(ziyad)
