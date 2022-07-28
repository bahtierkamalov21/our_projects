<template>
  <section class="projects">
    <v-container class="projects__container">
      <v-card
        width="100%"
        height="80%"
        class="projects__cards mb-3"
        v-for="project in slice_projects"
        :key="project.id"
      >
        <v-card-title>{{ project.title }}</v-card-title>
        <ul>
          <li v-for="item in project.stack.split(',')" :key="item.id">
            {{ item }}
          </li>
        </ul>
      </v-card>
      <v-pagination
        class="projects__pagination"
        v-model="pages"
        :length="length"
      ></v-pagination>
    </v-container>
  </section>
</template>

<script>
export default {
  name: "HomeProjects",
  props: {
    projects: Array,
  },
  data() {
    return {
      get_projects: null,
      pages: 1,
      length: null,
      slice_projects: null,
      before: 0,
      after: 1,
    };
  },
  mounted() {
    // Инициализация данных из пропса требует времени...
    setTimeout(() => {
      this.get_projects = this.projects;
      this.length = this.get_projects.length;
      this.slice_projects = this.get_projects.slice(this.before, this.after);
    }, 1500);
  },
  watch: {
    pages() {
      this.before = this.pages - 1;
      this.after = this.pages;
      this.slice_projects = this.get_projects.slice(this.before, this.after);
    },
  },
};
</script>

<style lang="scss" scoped>
.projects {
  height: 100%;
  background-color: #f3f3f3;
  &__container {
    height: 100%;
    align-items: center;
    flex-direction: column;
    display: flex;
    justify-content: center;
  }
  &__cards {
    border-radius: 12px !important;
    box-shadow: 0 0 20px 0 rgba(34, 60, 80, 0.2) !important;
  }
}
</style>
