<template>
  <div class="insightHeader">
    <span class="insightHeaderInfo">
      <span class="headerImageContainer">
        <img class="headerImage" v-if="validURL(this.icon)" :src="this.icon" />
        <utils-svg-cmp class="headerImage" v-else :name="this.icon" />
      </span>
      <span class="headerInfo">
        <span class="insightLabel">Insight</span>
        <span class="insightName">{{ name }}</span>
        <span class="insightSource">{{ source }}</span>
      </span>
    </span>
  </div>
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
@import "assets/styles/theme"

.insightHeaderInfo
  display: flex
  align-items: flex-end

  gap: 24px

.insightHeader
  padding: 0 32px 32px

  width: 100%
  height: 320px

  box-sizing: border-box !important

  flex-direction: column

  display: flex
  justify-content: flex-end


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

  color: white
  font-size: 1rem

  box-sizing: border-box

  width: 100%

  overflow: hidden

.insightName
  color: white
  font-size: min(6rem, calc(6vw))
  line-height: 6rem
  padding: 8px 0

  letter-spacing: -0.04em

  font-weight: 800

  overflow: hidden
  white-space: nowrap
  text-overflow: ellipsis

.insightSource
  font-size: 1.375rem
  font-weight: 600
</style>
