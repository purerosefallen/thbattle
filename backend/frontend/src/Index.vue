<template>
  <div>
    <header-section></header-section>
    <router-view></router-view>
    <footer-section></footer-section>
  </div>
</template>

<style lang="sass">
@import "~bulma/bulma.sass";
@import "~@fortawesome/fontawesome-free/css/all.css";
</style>

<script>
import HeaderSection from './components/header/Header.vue'
import FooterSection from './components/footer/Footer.vue'

export default {
  name: 'Index',
  components: { HeaderSection, FooterSection },
}
</script>
