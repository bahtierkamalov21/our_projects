<template>
  <header class="header">
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
};
</script>

<style lang="scss" scoped>
.header {
  height: 100%;
  &__container {
    height: 100%;
  }
  &__col {
    height: 100%;
  }
  &__content {
    height: 100%;
    padding-top: 5vh;
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
    font-size: calc(var(--index) * 1.2);
    line-height: 32px;
    letter-spacing: -1px;
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
    &__left {
      width: 50%;
    }
    &__h1 {
      line-height: 52px;
    }
  }
}
@media screen and (max-width: 600px) {
  .header {
    &__left {
      width: 100%;
    }
    &__right {
      width: 100%;
      justify-content: inherit;
      display: inherit;
    }
    &__h1 {
      line-height: 42px;
    }
    &__subtitle {
      font-size: calc(var(--index) * 1.2);
      line-height: 16px;
      letter-spacing: -1px;
    }
    &__content {
      align-items: center !important;
      display: block;
      padding-top: 15vh;
    }
    &__chip {
      width: 80vw;
    }
  }
}
</style>
