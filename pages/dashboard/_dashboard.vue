<template>
  <div class="pageContainer">
    <h1 class="titleText">I am a dashboard page for {{ slug }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      slug: this.$route.params.dashboard,
    }
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.pageContainer
  margin: auto 32px
  padding-top: 1.75vh
  overflow: hidden
  position: relative

.titleText
  margin: 70px 0 16px
</style>
