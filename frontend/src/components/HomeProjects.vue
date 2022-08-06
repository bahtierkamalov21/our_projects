<template>
  <section class="projects">
    <div class="projects__background">
      <h2>Our completed projects</h2>
    </div>
    <v-container class="projects__container">
      <v-card
        width="100%"
        height="50%"
        class="projects__none mb-6"
        v-if="!length"
      >
        <div class="projects__none__title">
          <v-card-title class="pa-8 ma-0">Projects coming soon...</v-card-title>
        </div>
        <span>
          <font-awesome-icon icon="fa-solid fa-code" class="fa-3x" />
        </span>
      </v-card>
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
        v-if="length"
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
  position: relative;
  &__background {
    position: absolute;
    top: 0;
    width: 100%;
    height: 35%;
    background-color: black;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: calc(var(--index) * 2);
  }
  &__container {
    height: 100%;
    align-items: center;
    flex-direction: column;
    display: flex;
    justify-content: center;
    & > span {
      color: var(--v-black-base);
    }
  }
  &__none {
    position: relative;
    top: 20px;
    border-radius: 4px !important;
    box-shadow: 0 1.6px 3.6px 0 rgb(0 0 0 / 13%),
      0 0.3px 0.9px 0 rgb(0 0 0 / 11%) !important;
    display: flex;
    flex-direction: column;
    align-items: center;
    &__title {
      width: 100%;
      & > * {
        text-transform: uppercase;
        font-size: 22px;
        font-weight: 600;
      }
    }
    & > *:last-child {
      margin-top: 4%;
    }
  }
  &__cards {
    border-radius: 12px !important;
    box-shadow: 0 0 20px 0 rgba(34, 60, 80, 0.2) !important;
  }
}
@media screen and (max-width: 600px) {
  .projects {
    &__container {
      align-items: inherit;
    }
    &__none {
      width: 90% !important;
      &__title {
        & > * {
          font-size: 18px !important;
          padding: 22px !important;
        }
      }
      & > *:last-child {
        margin-top: 10% !important;
      }
    }
  }
}
</style>
