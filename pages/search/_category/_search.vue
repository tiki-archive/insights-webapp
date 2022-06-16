<template>
  <div class="themeStandardPageContainer">
    <span>
      <h2>All {{ category }} for "{{ searchTerm }}"</h2>

      <tall-card-list :show_all="true" />
    </span>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    console.log(this.$route.params.search)
    return {
      searchTerm: this.$route.params.search,
      category: this.$route.params.category,
    }
  },
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
</style>
