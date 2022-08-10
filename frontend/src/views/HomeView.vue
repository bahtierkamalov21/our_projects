<template>
  <div class="home">
    <!-- Navigation -->
    <home-navigation
      @get_drawer="get_drawer"
      @get_navigation_index="get_navigation_index"
    />
    <!-- Swiper -->
    <div class="swiper">
      <!-- Drawer -->
      <home-drawer :drawer="drawer" :projects="projects" />
      <div class="swiper-wrapper">
        <div class="swiper-slide">
          <home-main />
        </div>
        <div class="swiper-slide">
          <home-projects :projects="projects" />
        </div>
        <div class="swiper-slide">
          <home-contacts />
        </div>
      </div>
      <!-- Add Pagination -->
      <div class="swiper-pagination"></div>
    </div>
  </div>
</template>

<script>
import HomeNavigation from "@/components/HomeNavigation";
import { Mousewheel, Pagination, Swiper } from "swiper";
import HomeMain from "@/components/HomeMain";
import HomeContacts from "@/components/HomeContacts";
import HomeProjects from "@/components/HomeProjects";
import HomeDrawer from "@/components/HomeDrawer";
import axios from "axios";
export default {
  name: "HomeView",
  components: {
    HomeDrawer,
    HomeProjects,
    HomeContacts,
    HomeMain,
    HomeNavigation,
  },
  data() {
    return {
      swiper: null,
      drawer: null,
      location_hash: location.hash,
      // backend
      projects: null,
    };
  },
  mounted() {
    // Init swiper.js
    this.swiper = new Swiper(".swiper", {
      direction: "vertical",
      autoHeight: true,
      mousewheel: true,
      speed: 1500,
      slidesPerView: 1,
      modules: [Mousewheel, Pagination],
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });
    // Swiper.js hook function
    this.swiper.on("activeIndexChange", function () {
      if (this.activeIndex === 0) {
        document.title = "Our Projects";
        document.getElementById("swiper__index").innerHTML = "0";
      } else if (this.activeIndex === 1) {
        document.title = "Our Projects | Projects";
        document.getElementById("swiper__index").innerHTML = "1";
      } else if (this.activeIndex === 2) {
        document.title = "Our Projects | Contacts";
        document.getElementById("swiper__index").innerHTML = "2";
      }
    });
    // Get projects from api
    axios
      .get(this.$store.state.api_url + "projects")
      .then((response) => {
        this.projects = response.data;
      })
      .catch((error) => console.log(error));
  },
  methods: {
    // Get emit drawer
    get_drawer(drawer) {
      this.drawer = drawer;
    },
    // Get emit navigation_index
    get_navigation_index(index) {
      if (index === 0) {
        this.swiper.slideTo(0);
      } else if (index === 1) {
        this.swiper.slideTo(1);
      } else if (index === 2) {
        this.swiper.slideTo(2);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.home {
  background-color: #f7f7f7;
}
.swiper {
  overflow: hidden;
  height: calc(100vh - 63.5px);
}
</style>
