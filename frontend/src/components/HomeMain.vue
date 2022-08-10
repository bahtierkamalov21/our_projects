<template>
  <header class="header">
    <v-sheet color="background" class="header__background"></v-sheet>
    <v-container class="header__container">
      <v-col class="header__col pt-0 pb-0">
        <v-row class="header__content align-center">
          <div class="header__left">
            <v-chip class="header__chip ma-2 ml-0" color="primary">
              Python, Vue.js, JavaScript, Front-end, Back-end, Web developers
            </v-chip>
            <h1 class="header__h1">
              The Our <br />
              Projects <br />
              Platform
            </h1>
            <p class="header__subtitle mt-2">
              From planning to production, bring teams <br />
              together in one application. Ship secure code <br />
              faster, deploy to any cloud, and drive business <br />
              results.
            </p>
          </div>
          <div class="header__right">
            <div>
              <v-img src="@/assets/images/header-right-img.svg"></v-img>
            </div>
          </div>
        </v-row>
      </v-col>
    </v-container>
  </header>
</template>

<script>
export default {
  name: "HomeMain",
  mounted() {
    // before window resize
    this.element_substitution();
    window.addEventListener("resize", () => {
      this.element_substitution();
    });
  },
  methods: {
    // adaption of header__background
    element_substitution() {
      if (document.querySelector(".header__left").clientHeight <= 360) {
        document.querySelector(".header__background").style.height = "64.5vh";
      } else {
        document.querySelector(".header__background").style.height = "71.5vh";
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.header {
  height: 100%;
  position: relative;
  &__container {
    height: 100%;
  }
  &__background {
    width: 100%;
    height: 71.5vh;
    position: absolute;
    bottom: 0;
    background-color: white;
    box-shadow: 0 -4px 10px 0 rgba(23, 19, 33, 0.2) !important;
  }
  &__col {
    height: 100%;
  }
  &__content {
    height: 100%;
    position: relative;
    z-index: 1;
  }
  &__left {
    width: 50%;
  }
  &__h1 {
    font-size: calc(var(--index) * 4);
    line-height: 86px;
    font-weight: 600;
  }
  &__subtitle {
    font-size: calc(var(--index) * 1);
    line-height: 24px;
    color: #fff;
    padding: 12px;
    border-radius: 5px;
    background-color: #171321;
    display: inline-block;
  }
  &__right {
    width: 50%;
    display: flex;
    justify-content: center;
    & > div {
      width: 80%;
    }
  }
}
@media screen and (max-width: 960px) {
  .header {
    &__subtitle {
      line-height: 24px;
    }
    &__left {
      width: 50%;
    }
    &__h1 {
      line-height: 52px;
    }
    &__right {
      width: 48%;
      padding-right: 12px;
    }
  }
}
@media screen and (max-width: 600px) {
  .header {
    padding-top: 16px;
    &__subtitle {
      font-size: calc(var(--index) * 1.3);
      line-height: 18px;
    }
    &__background {
      height: 64.5vh;
    }
    &__left {
      width: 100%;
    }
    &__right {
      width: 100%;
      justify-content: inherit;
      display: inherit;
      & > div {
        width: 45%;
      }
    }
    &__h1 {
      line-height: 42px;
    }
    &__content {
      align-items: center !important;
      display: block;
    }
    &__chip {
      width: 80vw;
    }
  }
}
</style>
