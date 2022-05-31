<template>
  <div class="pageContainer">
    <h1 class="titleText">I am a company page for {{ slug }}</h1>
  </div>
</template>

<script>
export default {
  validate({ params }) {
    return /^\d+$/.test(params.company)
  },
  data() {
    return {
      slug: this.$route.params.company,
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
