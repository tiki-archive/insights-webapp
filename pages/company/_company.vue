<template>
  <div class="pageContainer">
    <company-header
      name="Dr Martens"
      :monthly_users="'103,301'"
      :following="this.following"
      @setFollowing="setFollowing"
    />

    <div class="mainContentContainer">
      <div class="searchResultsContainer">
        <span class="topResult">
          <span class="heading">
            <h2>
              <NuxtLink
                class="headingLink"
                :to="'/search/insights/' + searchTerm"
              >
                Popular
              </NuxtLink>
            </h2>

            <NuxtLink class="seeAll" :to="'/search/insights/' + searchTerm">
              SEE ALL
            </NuxtLink>
          </span>

          <insight-list />
        </span>

        <span class="secondaryResult">
          <span class="heading">
            <h2>
              <NuxtLink
                class="headingLink"
                :to="'/search/insights/' + searchTerm"
              >
                You liked
              </NuxtLink>
            </h2>
          </span>

          <insight-list :number="false" :confidence_levels="false" />
        </span>

        <span class="gridRow">
          <span class="heading">
            <h2>
              <NuxtLink
                class="headingLink"
                :to="'/search/companies/' + searchTerm"
              >
                Companies
              </NuxtLink>
            </h2>

            <NuxtLink class="seeAll" :to="'/search/companies/' + searchTerm">
              SEE ALL
            </NuxtLink>
          </span>

          <tall-card-list />
        </span>

        <span class="gridRow">
          <span class="heading">
            <h2>
              <NuxtLink
                class="headingLink"
                :to="'/search/dashboard/' + searchTerm"
              >
                Dashboards
              </NuxtLink>
            </h2>

            <NuxtLink class="seeAll" :to="'/search/dashboard/' + searchTerm">
              SEE ALL
            </NuxtLink>
          </span>

          <tall-card-list />
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import CompanyHeader from '~/components/company_header/CompanyHeader.vue'
export default {
  components: { CompanyHeader },
  data() {
    return {
      slug: this.$route.params.company,
      following: false,
    }
  },
  methods: {
    setFollowing(following) {
      console.log('SET FOLLOWING ' + following)
      this.following = following
    },
  },
}
</script>

<style lang="sass">
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
