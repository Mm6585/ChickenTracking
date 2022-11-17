import { getDatabase, ref, child, get } from "firebase/database";
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {

};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


const dbRef = ref(getDatabase());

const getAOA = get(child(dbRef,'asdf/20221022/aoa')).then((snapshot) => {
    if (snapshot.exists()) {
        var data = snapshot.toJSON()        
        const aoa = JSON.stringify(data,null,3)
        console.log(aoa)
        const aoaString = aoa.toString()
        console.log(aoaString)
        return aoaString
    } else {
        console.log('if not exist')
    // if not exist snap shot
    }
    }).catch((error) => {
        console.log(error)
    //if not get 
});



export {
    getAOA
};



