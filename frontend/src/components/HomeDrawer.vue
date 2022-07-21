<template>
  <v-navigation-drawer
    absolute
    temporary
    width="50%"
    class="drawer"
    right
    color="rgba(255,255,255, 0.5)"
    v-model="drawer_menu"
  ></v-navigation-drawer>
</template>

<script>
export default {
  name: "HomeDrawer",
  props: ["drawer"],
  data() {
    return {
      drawer_menu: null,
    };
  },
  watch: {
    drawer() {
      this.drawer_menu = this.drawer;
    },
  },
};
</script>

<style lang="scss" scoped>
@media screen and (max-width: 600px) {
  .drawer {
    width: 100% !important;
  }
}
</style>
