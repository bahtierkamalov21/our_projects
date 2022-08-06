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
    <v-container class="drawer__container pa-4">
      <div v-if="projects_length === null" class="projects__none">
        <v-card-title class="pa-0">Projects coming soon...</v-card-title>
        <span style="color: #ffffff">
          <font-awesome-icon icon="fa-solid fa-code" class="fa-3x" />
        </span>
      </div>
      <v-col>
        <v-row class="justify-space-between"></v-row>
      </v-col>
      <v-btn
        block
        elevation="0"
        :disabled="disabled_button"
        class="drawer__button text-capitalize font-weight-regular"
      >
        <p class="ma-0">Show <span class="text-lowercase">more</span></p>
      </v-btn>
    </v-container>
  </v-navigation-drawer>
</template>

<script>
import axios from "axios";
export default {
  name: "HomeDrawer",
  props: {
    drawer: Boolean,
  },
  data() {
    return {
      get_drawer: this.drawer,
      projects: null,
      projects_length: null,
    };
  },
  watch: {
    drawer() {
      this.get_drawer = !this.get_drawer;
    },
  },
  computed: {
    disabled_button: function () {
      return this.projects_length > 6;
    },
  },
  mounted() {
    // Get projects from api
    axios
      .get(this.$store.state.api_url + "projects")
      .then((response) => {
        this.projects = response.data;
        this.projects_length = this.projects.length;
      })
      .catch((error) => console.log(error));
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

.projects__none {
  height: 92%;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #000000;

  & > *:first-child {
    text-transform: uppercase;
    font-weight: 600;
    position: absolute;
    top: 0;
    left: 0;
  }
}

@media screen and (max-width: 600px) {
  .drawer {
    width: 100% !important;
  }
}
</style>
