<template>
  <div class="pageContainer">
    <!-- <search-bar /> -->
    <span class="gridRow">
      <h2>All {{ category }} for "{{ searchTerm }}"</h2>
      <tall-card-list class="mostRelevant" :show_all="true" />
    </span>
  </div>
</template>

<script>
export default {
  name: 'HomeFull',
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
@import "assets/styles/theme"

.pageContainer
  margin: calc(4vh + 24px) 32px 0
  overflow: hidden
  position: relative

  display: block
</style>
