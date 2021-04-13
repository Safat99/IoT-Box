var firebaseConfig = {
  apiKey: "AIzaSyDK3f17CXWzJFlHiLS8kSbPMqS5m8g_qbM",
  authDomain: "iot-box-849d9.firebaseapp.com",
  databaseURL: "https://iot-box-849d9.firebaseio.com",
  projectId: "iot-box-849d9",
  storageBucket: "iot-box-849d9.appspot.com",
  messagingSenderId: "1021612354284",
  appId: "1:1021612354284:web:ff41c4c6c231731e6b93c9",
  measurementId: "G-T7SRFFCLN6",
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
let dbRef = firebase.database().ref("/IOT-BOX/");

const app = new Vue({
  el: "#app",

  data: {
    humidity: 0,
    led: 0,
    relay1: false,
    relay2: false,
    relay3: false,
    relay4: false,
    temperature: 0,
  },

  mounted() {
    console.log("mounting");

    dbRef.on("value", (snapshot) => {
      console.log("getting from firebase");
      const { humidity, relay1, relay2, relay3, relay4, temperature, led } =
        snapshot.val() || {};

      this.humidity = humidity;
      this.temperature = temperature;
      this.relay1 = this.toBool(relay1);
      this.relay2 = this.toBool(relay2);
      this.relay3 = this.toBool(relay3);
      this.relay4 = this.toBool(relay4);
      this.led = led;
    });
  },

  methods: {
    saveRelayData() {
      let payload = {
        temperature: this.temperature,
        relay1: this.toString(this.relay1),
        relay2: this.toString(this.relay2),
        relay3: this.toString(this.relay3),
        relay4: this.toString(this.relay4),
        humidity: this.humidity
      };

      let updates = {};
      updates["/IOT-BOX/"] = payload;
      return firebase.database().ref().update(updates, err => {
        if(err) alert("An error occured on updating the values");
        else alert("Saved");
      });
    },

    toBool(val) {
      switch (val.trim()) {
        case "0":
          return false;
        case "1":
          return true;
      }
    },

    toString(val) {
      switch (val) {
        case false:
          return "0";
        case true:
          return "1";
      }
    },
  },
});
