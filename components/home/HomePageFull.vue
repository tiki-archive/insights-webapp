<template>
  <div class="homePage">
    <wide-card-list class="mostRelevant" title="Insights you might like" />

    <tall-card-list class="mostRelevant" title="Insights, but tall this time" />
  </div>
</template>

<script>
import TallCardList from '../general/TallCardList.vue'
import WideCardList from '../general/WideCardList.vue'
export default {
  components: { TallCardList, WideCardList },
  name: 'HomeFull',
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.homePage
  width: 96%
  margin: auto auto
  padding-top: 30px
  overflow: hidden

.mostRelevant
  width: 100%
  margin: 50px auto
  display: block
</style>
