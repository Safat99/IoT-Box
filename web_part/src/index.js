const app = new Vue({
  el: "#app",

  data: {
    humidity: 0,
    led: 0,
    relay1: false,
    relay2: true,
    relay3: false,
    relay4: false,
    temperature: 0,
  },

  mounted: function () {
    console.log("mounting")
    this.temperature = 35;
    this.humidity = 7;
  },

  methods: {
    saveRelayData() {
      console.log(this.relay1);
      console.log(this.relay2);
      console.log(this.relay3);
      console.log(this.relay4);
    }
  },
});
