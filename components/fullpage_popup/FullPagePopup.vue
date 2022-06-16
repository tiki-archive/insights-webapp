<template>
  <span class="popupContainer" @click="clickedPopup">
    <span class="popupOffset">
      <span class="popupWindow">
        <slot></slot>
      </span>
    </span>
  </span>
</template>

<script>
export default {
  props: ['text', 'link'],
  methods: {
    clickedPopup(e) {
      if (
        e.target.className === 'popupContainer' ||
        e.target.className === 'popupOffset'
      ) {
        this.$emit('clickedOut')
      }
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
.popupContainer
  position: fixed
  width: 100vw
  height: 100vh

  z-index: 100
  left: 0
  top: 0

  background: rgba(255, 255, 255, .31)

  display: flex
  justify-content: center
.popupOffset
  margin: auto auto
.popupWindow
  margin-left: 241px
  border-radius: 14px

  color: white
  display:  flex
  justify-content: center
  align-items: center

  background-color: $tiki-purple

  width: 52vw
  min-width: 300px
  max-width: 800px
  aspect-ratio: 8 / 3
</style>
