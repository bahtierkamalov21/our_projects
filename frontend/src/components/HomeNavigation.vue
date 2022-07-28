<template>
  <v-app-bar
    class="nav"
    :class="{ 'nav-default': nav_default }"
    color="#171321"
    elevation="0"
    height="64"
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
      v-if="!mobile"
      @click="set_navigation_index(0)"
      class="nav__link text-capitalize font-weight-regular pa-2"
      :class="{ 'nav__link-active': swiper_index_home }"
      >Home</v-btn
    >
    <v-btn
      v-if="!mobile"
      @click="set_navigation_index(1)"
      class="nav__link text-capitalize font-weight-regular pa-2"
      :class="{ 'nav__link-active': swiper_index_projects }"
      >Projects</v-btn
    >
    <v-btn
      v-if="!mobile"
      @click="set_navigation_index(2)"
      class="nav__link text-capitalize font-weight-regular pa-2"
      :class="{ 'nav__link-active': swiper_index_contacts }"
      >Contacts</v-btn
    >
    <v-spacer></v-spacer>
    <v-btn
      min-width="32"
      width="32"
      min-height="32"
      height="32"
      color="white"
      class="nav__bars mr-2"
      v-if="!mobile"
    >
      <span :class="{ 'nav__bars-dark': this.$vuetify.theme.dark }">
        <font-awesome-icon icon="fa-brands fa-telegram" class="fa-2x" />
      </span>
    </v-btn>
    <v-btn
      min-width="32"
      width="32"
      min-height="32"
      height="32"
      color="white"
      class="nav__bars mr-2"
      v-if="!mobile"
    >
      <span :class="{ 'nav__bars-dark': this.$vuetify.theme.dark }">
        <font-awesome-icon icon="fa-brands fa-git-square" class="fa-2xl" />
      </span>
    </v-btn>
    <!-- theme change -->
    <v-btn
      min-width="32"
      width="32"
      min-height="32"
      height="32"
      color="white"
      class="nav__bars mr-2"
      @click="change_theme"
    >
      <span :class="{ 'nav__bars-dark': this.$vuetify.theme.dark }">
        <font-awesome-icon
          v-if="!$vuetify.theme.dark"
          icon="fa-solid fa-moon"
          class="fa-xl"
        />
        <font-awesome-icon v-else icon="fa-solid fa-sun" class="fa-xl" />
      </span>
    </v-btn>
    <v-btn
      min-width="32"
      width="32"
      min-height="32"
      height="32"
      color="white"
      class="nav__bars"
      @click="open_drawer"
    >
      <span :class="{ 'nav__bars-dark': this.$vuetify.theme.dark }">
        <font-awesome-icon icon="fa-solid fa-bars" class="fa-xl" />
      </span>
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
      mobile: false,
      swiper_index_home: true,
      swiper_index_projects: false,
      swiper_index_contacts: false,
    };
  },
  mounted() {
    setInterval(() => {
      this.nav_default = window.innerWidth <= 960;
      this.mobile = window.innerWidth <= 600;
      if (document.getElementById("swiper__index").innerHTML === "0") {
        this.swiper_index_home = true;
        this.swiper_index_projects = false;
        this.swiper_index_contacts = false;
      } else if (document.getElementById("swiper__index").innerHTML === "1") {
        this.swiper_index_home = false;
        this.swiper_index_projects = true;
        this.swiper_index_contacts = false;
      } else if (document.getElementById("swiper__index").innerHTML === "2") {
        this.swiper_index_home = false;
        this.swiper_index_projects = false;
        this.swiper_index_contacts = true;
      }
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
    change_theme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
  },
};
</script>

<style lang="scss" scoped>
.nav {
  &__link {
    text-decoration: none;
    color: #e0e0e0 !important;
    background-color: transparent !important;
    border-radius: 4px;
    transition: all 0.2s ease;
    &-active {
      background-color: rgba(255, 255, 255, 0.1) !important;
      transition: all 0.2s ease;
    }
  }
  &__bars {
    border-radius: 5px;
    background-color: #ffffff !important;
    &-dark {
      color: black;
    }
  }
}
</style>
