<template>
  <div class="pageContainer">
    <!-- <search-bar /> -->

    <h1 class="titleText">Search page {{ slug }}</h1>

    <wide-card-list class="mostRelevant" title="Insights you might like" />

    <wide-card-list class="mostRelevant" title="Insights you might like" />

    <wide-card-list class="mostRelevant" title="Insights you might like" />

    <wide-card-list class="mostRelevant" title="Insights you might like" />

    <wide-card-list class="mostRelevant" title="Insights you might like" />

    <wide-card-list class="mostRelevant" title="Insights you might like" />
  </div>
</template>

<script>
import WideCardList from '~/components/wide_card_list/WideCardList.vue'

export default {
  name: 'HomeFull',
  components: { WideCardList },
  data() {
    return {
      slug: this.$route.params.search,
    }
  },
  created() {
    this.$root.$emit('enableSearch')
  },
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.pageContainer
  margin: 24px 32px 0
  overflow: hidden
  position: relative

.titleText, .mostRelevant
  margin: 70px 0 16px
</style>
