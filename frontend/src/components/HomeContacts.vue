<template>
  <v-footer color="background" class="footer pa-0">
    <v-container class="footer__container"></v-container>
    <div class="footer__bottom"></div>
  </v-footer>
</template>

<script>
//import axios from "axios";
export default {
  name: "HomeContacts",
};
</script>

<style lang="scss" scoped>
.footer {
  height: 100%;
  &__container {
    height: 84%;
  }
  &__bottom {
    background-color: #171321;
    height: 64px;
    width: 100%;
  }
}
</style>
