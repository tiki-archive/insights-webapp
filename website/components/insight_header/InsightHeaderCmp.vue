<template>
  <span class="insightHeader">
    <span class="headerImageContainer">
      <img class="headerImage" v-if="validURL(this.icon)" :src="this.icon" />
      <utils-svg-cmp class="headerImage" v-else :name="this.icon" />
    </span>
    <span class="headerInfo">
      <span class="themeHeaderLabel">Insight</span>
      <span class="themeBigHeaderText">{{ name }}</span>
      <span class="themeHeaderSource">{{ source }}</span>
    </span>
  </span>
</template>

<script>
import UtilsSvgCmp from '../utils/UtilsSvgCmp.vue'
/**
 * Insights have name, icon/image, and source (something like company/industry/etc)
 */
export default {
  components: { UtilsSvgCmp },
  props: ['name', 'icon', 'source'],
  methods: {
    validURL(str) {
      const pattern = new RegExp(
        '^(https?:\\/\\/)?' + // protocol
          '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
          '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
          '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
          '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
          '(\\#[-a-z\\d_]*)?$',
        'i'
      ) // fragment locator
      return !!pattern.test(str)
    },
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme/default"

.insightHeader
  width: 100%

  display: flex
  justify-content: flex-end

  gap: 24px

  align-items: flex-end

.headerImageContainer
  width: 200px !important
  height: 200px

  > img, > svg
    border-radius: 15px
    box-shadow: 0 4px 60px rgb(0 0 0 / 50%)
    width: 200px
    height: 200px

.headerInfo
  display: flex
  flex-direction: column

  width: 100%

  overflow: hidden
</style>
