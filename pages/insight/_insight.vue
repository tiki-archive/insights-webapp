<template>
  <div class="pageContainer">
    <insight-header
      name="Best Subject Lines"
      source="Dr Martens"
      icon="https://gyazo.com/16f7279929955b76d85115e146c08f68.png"
    />

    <div class="mainContentContainer">
      <div class="searchResultsContainer">
        <span class="topResult">
          <span class="heading">
            <h2>
              <TrackedNuxtLink
                class="headingLink"
                :to="'/search/insights/' + searchTerm"
              >
                Popular
              </TrackedNuxtLink>
            </h2>

            <TrackedNuxtLink
              class="seeAll"
              :to="'/search/insights/' + searchTerm"
            >
              SEE ALL
            </TrackedNuxtLink>
          </span>

          <insight-list />
        </span>

        <span class="secondaryResult">
          <span class="heading">
            <h2>
              <TrackedNuxtLink
                class="headingLink"
                :to="'/search/insights/' + searchTerm"
              >
                You liked
              </TrackedNuxtLink>
            </h2>
          </span>

          <insight-list :number="false" :confidence_levels="false" />
        </span>

        <span class="gridRow">
          <span class="heading">
            <h2>
              <TrackedNuxtLink
                class="headingLink"
                :to="'/search/companies/' + searchTerm"
              >
                Companies
              </TrackedNuxtLink>
            </h2>

            <TrackedNuxtLink
              class="seeAll"
              :to="'/search/companies/' + searchTerm"
            >
              SEE ALL
            </TrackedNuxtLink>
          </span>

          <tall-card-list />
        </span>

        <span class="gridRow">
          <span class="heading">
            <h2>
              <TrackedNuxtLink
                class="headingLink"
                :to="'/search/dashboard/' + searchTerm"
              >
                Dashboards
              </TrackedNuxtLink>
            </h2>

            <TrackedNuxtLink
              class="seeAll"
              :to="'/search/dashboard/' + searchTerm"
            >
              SEE ALL
            </TrackedNuxtLink>
          </span>

          <tall-card-list />
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import InsightHeader from '~/components/insight_header/InsightHeader.vue'
export default {
  components: { InsightHeader },
  data() {
    return {
      slug: this.$route.params.insight,
    }
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.mainContentContainer
  margin: auto 32px
  padding-top: 30px

.searchResultsContainer
  display: grid

  grid-template: 332px/repeat(auto-fill,minmax(max(180px,10%),1fr))
  grid-column-gap: 24px
  grid-row-gap: min(2.2vh, 22px)

  justify-content: space-between

.topResult
  grid-column: 1 / 4
  height: 260px

.secondaryResult
  grid-column: span 2 / -1

.gridRow
   grid-column: 1 / -1

.heading
  display: flex

h2
  margin: 16px 0

.seeAll
  color: $see-all-text
  font-weight: 800
  font-size: .875rem
  text-decoration: none

  margin: auto 0 auto auto

  &:hover
    text-decoration: underline

.headingLink
  text-decoration: none
  color: white

  &:hover
    text-decoration: underline
</style>
