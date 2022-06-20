<template>
  <span>
    <button class="userButton" @click="toggleDropdown">
      <img class="userIcon" :src="icon" />
      <span class="userName">{{ name }}</span>
      <utils-svg-cmp class="downArrow" name="icon_down_arrow" />
    </button>

    <span v-if="dropdown" class="subMenu">
      <button class="subMenuButton">
        Account

        <utils-svg-cmp name="icon_external_link" />
      </button>
      <button class="subMenuButton">Profile</button>
      <button class="subMenuButton">Log out</button>
    </span>
  </span>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
export default {
  components: { UtilsSvgCmp },
  props: ['name', 'icon'],
  data() {
    return {
      dropdown: false,
    }
  },
  methods: {
    toggleDropdown() {
      this.dropdown = !this.dropdown
    },
    close(e) {
      if (!this.$el.contains(e.target)) {
        this.dropdown = false
      }
    },
  },
  mounted() {
    document.addEventListener('click', this.close)
  },
  beforeDestroy() {
    document.removeEventListener('click', this.close)
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

.subMenu
  position: absolute
  width: 168px
  padding: 4px
  background-color: $tiki-purple

  border-radius: 4px

  right: 32px
  transform: translate(0, 8px)

  display: flex
  flex-direction: column

.subMenuButton
  width: 100%
  border: 0
  outline: 0
  background: none
  padding: 12px
  height: 40px

  justify-content: center

  color: white
  font-size: .875rem
  font-family: $font-family-nunito-sans
  font-weight: 700

  cursor: pointer

  text-align: left

  &:hover
    background-color: rgba(255,255,255,.1)

  > svg
    fill: white
    float: right

.userButton
  display: flex
  align-items: center

  border: 0
  outline: 0
  border-radius: 23px
  background-color: $tiki-purple

  gap: 8px
  padding: 2px
  height: 32px

  &:hover
    background-color: lighten($tiki-purple, 3%)

.userIcon
  width: 28px
  height: 28px
  display: inline-block

  border-radius: 23px

.userName
  color: white
  font-family: $font-family-nunito-sans
  font-size: .875rem
  font-weight: 700

.downArrow
  margin-right: 8px
</style>
