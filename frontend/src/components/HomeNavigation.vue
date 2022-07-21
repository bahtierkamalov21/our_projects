<template>
  <v-app-bar
    class="nav"
    :class="{ 'nav-default': nav_default }"
    color="#171321"
    elevation="0"
    app
  >
    <router-link to="/" class="text-decoration-none mr-2">
      <v-img
        width="32"
        height="32"
        class="mr-2"
        src="@/assets/images/logo.svg"
      ></v-img>
    </router-link>
    <router-link to="#" class="nav__link mr-4">Why Our Projects?</router-link>
    <v-btn
      v-if="!display_mobile"
      @click="set_navigation_index(0)"
      color="transparent"
      class="nav__link text-capitalize font-weight-regular pa-2"
      >Home</v-btn
    >
    <v-btn
      v-if="!display_mobile"
      @click="set_navigation_index(1)"
      color="transparent"
      class="nav__link text-capitalize font-weight-regular pa-2"
      >Projects</v-btn
    >
    <v-btn
      v-if="!display_mobile"
      @click="set_navigation_index(2)"
      color="transparent"
      class="nav__link text-capitalize font-weight-regular pa-2"
      >Contacts</v-btn
    >
    <v-spacer></v-spacer>
    <v-btn
      min-width="32"
      width="32"
      min-height="32"
      height="32"
      color="white"
      class="nav__bars"
      @click="open_drawer"
    >
      <font-awesome-icon icon="fa-solid fa-bars" class="fa-xl" />
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: "HomeNavigation",
  data() {
    return {
      nav_default: false,
      drawer: false,
      navigation_index: null,
      display_mobile: false,
    };
  },
  mounted() {
    setInterval(() => {
      this.nav_default = window.innerWidth <= 960;
      this.display_mobile = window.innerWidth <= 600;
    });
  },
  methods: {
    open_drawer() {
      this.drawer = !this.drawer;
      this.$emit("get_drawer", this.drawer);
    },
    set_navigation_index(index) {
      this.navigation_index = index;
      this.$emit("get_navigation_index", this.navigation_index);
    },
  },
};
</script>

<style lang="scss" scoped>
.nav-default {
  padding-top: 4px;
  min-height: 64px;
}
.nav__bars {
  border-radius: 4px;
}
.nav__link {
  text-decoration: none;
  color: #e0e0e0 !important;
  border-radius: 4px;
}
</style>
