<template>
  <div class="pageContainer">
    <h1 class="titleText">Welcome back</h1>
    <wide-card-list class="mostRelevant" title="Insights you might like" />

    <h2 class="titleText">Insights, but tall this time</h2>
    <tall-card-list class="mostRelevant" />

    <title-description
      class="titleText"
      title="Description"
      description="The Best Subject Lines insight details the highest performing subject lines from the brand. The insight may be helpful in determining customer engagement, conversion rates, customer interests, and campaign optimization. "
    />
  </div>
</template>

<script>
import WideCardList from '~/components/wide_card_list/WideCardList.vue'
import TallCardList from '~/components/tall_card_list/TallCardList.vue'
import TitleDescription from '~/components/title_description/TitleDescription.vue'
export default {
  name: 'HomeFull',
  components: { WideCardList, TallCardList, TitleDescription },
  scrollToTop: true,
}
</script>

<style lang="sass">
@import "assets/styles/theme"

.pageContainer
  margin: 24px 32px
  overflow: hidden
  position: relative

.titleText
  margin: 70px 0 16px

.mostRelevant
  width: 100%
  margin: 0 auto
  display: block
</style>
