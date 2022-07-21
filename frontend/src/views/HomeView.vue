<template>
  <div>
    <!-- Navigation -->
    <home-navigation
      @get_drawer="get_drawer"
      @get_navigation_index="get_navigation_index"
    />
    <!-- Swiper -->
    <div class="swiper">
      <!-- Drawer -->
      <home-drawer :drawer="drawer" />
      <div class="swiper-wrapper">
        <div class="swiper-slide">
          <home-main />
        </div>
        <div class="swiper-slide">
          <home-projects />
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
      info: null,
    };
  },
  mounted() {
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
    this.swiper.on("activeIndexChange", function () {
      if (this.activeIndex === 0) {
        document.title = "Our Projects";
      } else if (this.activeIndex === 1) {
        document.title = "Our Projects - Projects";
      } else if (this.activeIndex === 2) {
        document.title = "Our Projects - Contacts";
      }
    });
  },
  created() {
    // backend
    axios.get("http://127.0.0.1:8000/api/").then((response) => {
      this.info = response;
      console.log(this.info.json);
    });
  },
  methods: {
    get_drawer(drawer) {
      this.drawer = drawer;
    },
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
.swiper {
  overflow: hidden;
  min-height: 100vh;
}
.drawer {
  z-index: 100;
  backdrop-filter: blur(16px);
}
</style>
