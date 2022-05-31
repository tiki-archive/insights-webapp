<template>
  <div class="pageContainer">
    <h1 class="titleText">Search page {{ slug }}</h1>
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
