<template>
  <div class="themeStandardPageContainer">
    <section>
      <h1>Welcome back</h1>
      <wide-card-list title="Insights you might like" />
    </section>

    <section>
      <h2>Insights, but tall this time</h2>
      <tall-card-list />
    </section>

    <section>
      <title-description
        title="Description"
        description="The Top Subject Lines insight details the highest performing subject lines from the brand. The insight may be helpful in determining customer engagement, conversion rates, customer interests, and campaign optimization. "
      />
    </section>
  </div>
</template>

<script>
import WideCardList from '~/components/wide_card_list/WideCardListCmp.vue'
import TallCardList from '~/components/tall_card_list/TallCardListCmp.vue'
import TitleDescription from '~/components/title_description/TitleDescriptionCmp.vue'
export default {
  name: 'HomeFull',
  components: { WideCardList, TallCardList, TitleDescription },
  scrollToTop: true,
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"
</style>
