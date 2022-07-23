<template>
  <v-navigation-drawer
    absolute
    temporary
    width="50%"
    class="drawer"
    right
    color="rgba(255,255,255, 0.5)"
    v-model="drawer_menu"
  >
    <v-container class="drawer__container">
      <v-col>
        <v-row class="justify-space-between"></v-row>
      </v-col>
      <v-btn
        :disabled="button_show_more"
        @click="show_more"
        block
        elevation="0"
        class="drawer__button text-capitalize font-weight-regular"
        ><p class="ma-0">
          Показать <span class="text-lowercase">ещё</span>
        </p></v-btn
      >
    </v-container>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "HomeDrawer",
  props: ["drawer", "projects"],
  data() {
    return {
      drawer_menu: null,
      mobile: false,
      index_before: 0,
      index_after: 4,
      button_show_more: null,
    };
  },
  watch: {
    drawer() {
      this.drawer_menu = this.drawer;
      if (!this.drawer) {
        this.index_before = 0;
        this.index_after = 4;
      }
      if (!this.drawer && this.mobile) {
        this.index_before = 0;
        this.index_after = 2;
      }
    },
    mobile() {
      if (this.mobile) {
        this.index_after = 2;
      }
    },
  },
  mounted() {
    setInterval(() => {
      this.mobile = window.innerWidth <= 960;
      this.button_show_more = this.projects.length < this.index_after;
    });
  },
  methods: {
    show_more() {
      if (!this.mobile) {
        this.index_before += 4;
        this.index_after += 4;
      } else {
        this.index_before += 2;
        this.index_after += 2;
      }
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
