<template>
  <div class="mobileHeader">
    <button class="showMenuButton" @click="toggleMobileMenu">
      <utils-svg-cmp
        v-if="!menuOpen"
        class="menuButtonIcon"
        name="icon_mobile_menu_open"
      />

      <utils-svg-cmp
        v-if="menuOpen"
        class="menuButtonIcon"
        name="icon_mobile_menu_close"
      />
    </button>

    <NuxtLink class="logoContainer" to="/">
      <utils-svg-cmp class="tikiLogo" name="tiki_logo" />
    </NuxtLink>
  </div>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  name: 'SidebarFull',
  data() {
    return {
      menuOpen: false,
    }
  },
  methods: {
    toggleMobileMenu() {
      this.$emit('clickedMenuButton')
      this.menuOpen = !this.menuOpen
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"
@import "assets/styles/mixins"

.mobileHeader
  width: 100vw
  height: 10vh

  background: $tiki-purple
  display: flex

  box-shadow: 0 4px 10px 0 rgba(0,0,0,0.32)

.showMenuButton
  background: none
  border: 0
  padding: 0

  margin-left: 24px

.menuButtonIcon
  height: 36px
  width: 36px

.logoContainer
  width: 33vw
  height: 10vh

  padding-right: 60px
  margin: auto auto

  position: relative
  display: flex
</style>
