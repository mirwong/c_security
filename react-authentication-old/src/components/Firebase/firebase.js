/* jshint esversion: 6 */
import firebase from 'firebase/app';
import 'firebase/auth';

// const config = {
//   apiKey: "AIzaSyCRRbqqR9I8Y-KeiZuf6e884FUTFY5mOp8",
//   authDomain: "auth-app-practice.firebaseapp.com",
//   databaseURL: "https://auth-app-practice.firebaseio.com",
//   projectId: "auth-app-practice",
//   storageBucket: "auth-app-practice.appspot.com",
//   messagingSenderId: "477050079827",
//   appId: "1:477050079827:web:a5092abe9d7e97728414a6",
//   measurementId: "G-GH24W92VLR"
// };

const config = {
  apiKey: process.env.REACT_APP_API_KEY,
  authDomain: process.env.REACT_APP_AUTH_DOMAIN,
  databaseURL: process.env.REACT_APP_DATABASE_URL,
  projectId: process.env.REACT_APP_PROJECT_ID,
  storageBucket: process.env.REACT_APP_STORAGE_BUCKET,
  messagingSenderId: process.env.REACT_APP_MESSAGING_SENDER_ID,
};


// var app = firebase.app();

class Firebase {
    constructor() {
        // if (!firebase.apps.length) {}
        firebase.initializeApp(config);
        this.authObj = firebase.auth();
    }
    // Auth API

    doCreateUserWithEmailAndPassword(email, password) {
        return this.authObj.createUserWithEmailAndPassword(email, password);
    }

    doSignInWithEmailAndPassword(email, password) {
        return this.authObj.signInWithEmailAndPassword(email, password);
    }

    doSignOut(obj) {
        return obj.authObj.signOut();
    }

    doPasswordReset(email) {
        return this.authObj.sendPasswordResetEmail(email);
    }

    doPasswordUpdate(password) {
        return this.authObj.currentUser.updatePassword(password);
    }
}

export default Firebase;
