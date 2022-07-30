import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    api_url: "http://127.0.0.1:8000/api/v1/projects",
  },
  getters: {},
  mutations: {},
  actions: {},
  modules: {},
});
