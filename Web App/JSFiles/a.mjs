import { initializeApp } from 'firebase/app';
import { getDatabase, ref, set } from 'firebase/database';
// Follow this pattern to import other Firebase services
// import { } from 'firebase/<service>';

// TODO: Replace the following with your app's Firebase project configuration
const firebaseConfig = {
    apiKey: "AIzaSyAz1R9Y4rgIUDR4TINqXvG2BbjZGzlWbXs",
    authDomain: "embedded-lab-2-part-2.firebaseapp.com",
    databaseURL: "https://embedded-lab-2-part-2.firebaseio.com",
    projectId: "embedded-lab-2-part-2",
    storageBucket: "embedded-lab-2-part-2.appspot.com",
    messagingSenderId: "164614426559",
    appId: "1:164614426559:web:cf7044cee5ca58327adb0a",
    measurementId: "G-FNKN7NGVYY"
};

const app = initializeApp(firebaseConfig);
const database = getDatabase();

function writeUserData(userId, name) {
  const db = getDatabase();
  set(ref(db, 'users/' + userId), {
    username: name,
  });
}
writeUserData(userID, ziyad);