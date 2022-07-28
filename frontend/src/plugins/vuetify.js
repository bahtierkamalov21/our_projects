import Vue from "vue";
import Vuetify from "vuetify/lib";
import "vuetify/dist/vuetify.min.css";

Vue.use(Vuetify);

const opts = {
  theme: {
    dark: false,
    options: { customProperties: true },
    themes: {
      light: {
        primary: "#3f51b5",
        secondary: "#b0bec5",
        accent: "#8c9eff",
        error: "#b71c1c",
        background: "#ffffff",
        black: "#000000",
      },
      dark: {
        black: "#ffffff",
      },
    },
  },
};

export default new Vuetify(opts);
