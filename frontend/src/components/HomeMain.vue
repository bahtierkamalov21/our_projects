<template>
  <header class="header">
    <img
      class="header__background-blocks"
      src="@/assets/images/background_blocks.svg"
      alt="header-background-blocks"
    />
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
  position: relative;
  &__background-blocks {
    position: absolute;
    width: 40vw;
    bottom: -15vh;
    right: 2%;
  }
  &__container {
    height: 100%;
  }
  &__col {
    height: 100%;
  }
  &__content {
    height: 100%;
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
    &__background-blocks {
      width: 70vw;
    }
    &__subtitle {
      font-size: calc(var(--index) * 1.3);
      line-height: 18px;
    }
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
