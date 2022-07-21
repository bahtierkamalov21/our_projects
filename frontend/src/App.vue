<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({}),
};
</script>

<style lang="scss">
/*====== vars ======*/
:root {
  --index: calc(1vw + 1vh);
}

.v-application {
  font-family: "Inter", sans-serif !important;
}
.swiper-pagination-bullet-active {
  background: #171321;
}
</style>
