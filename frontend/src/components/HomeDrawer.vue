<template>
  <v-navigation-drawer
    absolute
    temporary
    width="50%"
    class="drawer"
    right
    color="rgba(255,255,255, 0.5)"
    v-model="get_drawer"
  >
    <v-container class="drawer__container">
      <v-col>
        <v-row class="justify-space-between"></v-row>
      </v-col>
      <v-btn
        block
        elevation="0"
        class="drawer__button text-capitalize font-weight-regular"
        ><p class="ma-0">
          Show <span class="text-lowercase">more</span>
        </p></v-btn
      >
    </v-container>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "HomeDrawer",
  props: {
    drawer: Boolean,
  },
  data() {
    return {
      get_drawer: this.drawer,
    };
  },
  watch: {
    drawer() {
      this.get_drawer = !this.get_drawer;
    },
  },
};
</script>

<style lang="scss" scoped>
.drawer {
  overflow: hidden;
  backdrop-filter: blur(16px);
  z-index: 40;
  &__container {
    height: 100%;
    position: relative;
  }
  &__button {
    position: absolute;
    bottom: 16px;
    min-width: 95% !important;
  }
}
@media screen and (max-width: 600px) {
  .drawer {
    width: 100% !important;
  }
}
</style>
