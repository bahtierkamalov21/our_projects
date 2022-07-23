<template>
  <main class="projects">
    <v-container class="pt-10">
      <v-card
        height="70vh"
        class="projects__card"
        v-for="project in projects.slice(this.index_before, this.index_after)"
        :key="project.id"
      >
        <v-card-title>{{ project.title }}</v-card-title>
      </v-card>
      <v-pagination
        class="projects__pagination"
        :length="projects.length"
      ></v-pagination>
    </v-container>
  </main>
</template>

<script>
export default {
  name: "HomeProjects",
  props: ["projects"],
  data() {
    return {
      index_before: 0,
      index_after: 1,
    };
  },
};
</script>

<style lang="scss" scoped>
.projects {
  height: 100%;
  position: relative;
  &__card {
    border-radius: 10px !important;
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.2) !important;
  }
  &__pagination {
    position: absolute;
    bottom: 12px;
    left: 0;
    margin-left: 50%;
    transform: translate(-50%);
  }
}
@media screen and (max-width: 960px) {
  .projects__card {
    width: 95%;
  }
}
@media screen and (max-width: 600px) {
  .projects__card {
    width: 88%;
  }
}
</style>
