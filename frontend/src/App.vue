<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script>
export default {
  name: "App",

  data() {
    return {};
  },
};
</script>

<style lang="scss">
/*====== vars ======*/
:root {
  --index: calc(1vw + 1vh);
}

html {
  overflow: hidden !important;
}

.v-application {
  font-family: "Inter", sans-serif !important;
}
.swiper-pagination-bullet {
  background: var(--v-black-base);
}
.swiper-pagination-bullet-active {
  background: var(--v-black-base);
}

/* Change theme */
.theme--light {
  transition: all 0.4s ease !important;
}
.theme--dark {
  transition: all 0.4s ease !important;
}
</style>
