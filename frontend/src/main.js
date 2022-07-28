import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";
// import fonts api
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faBars,
  faSun,
  faMoon,
  faCode,
} from "@fortawesome/free-solid-svg-icons";
import {
  faGitSquare,
  faTelegram,
  faGitlab,
} from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

Vue.prototype.$http = axios;

Vue.config.productionTip = false;

library.add(faBars, faGitSquare, faTelegram, faGitlab, faSun, faMoon, faCode);

Vue.component("font-awesome-icon", FontAwesomeIcon);

new Vue({
  router,
  store,
  vuetify,
  FontAwesomeIcon,
  render: (h) => h(App),
}).$mount("#app");
