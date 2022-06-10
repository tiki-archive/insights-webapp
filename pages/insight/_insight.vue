<template>
  <div class="pageContainer">
    <insight-header
      name="Best Subject Lines"
      source="Dr Martens"
      icon="https://gyazo.com/16f7279929955b76d85115e146c08f68.png"
    />

    <div class="mainContentContainer">
      <insight-navbar />

      <span>
        <img src="https://gyazo.com/18cda419411923c058c8ddbf0a703f9b.png" />
      </span>

      <TitleDescription
        title="Description"
        description="The Customer Location insight details the number of customers purchasing items from the brand. The insight may be helpful in determining target markets, competitive opportunities, or optimizing marketing spend."
      />

      <span>
        <span class="heading">
          <h2>
            <NuxtLink
              class="headingLink"
              :to="'/search/dashboard/' + searchTerm"
            >
              Recommended Insights
            </NuxtLink>
          </h2>

          <NuxtLink class="seeAll" :to="'/search/dashboard/' + searchTerm">
            SEE ALL
          </NuxtLink>
        </span>

        <wide-card-list />
      </span>
    </div>
  </div>
</template>

<script>
import InsightHeader from '~/components/insight_header/InsightHeader.vue'
import TitleDescription from '~/components/title_description/TitleDescription.vue'
export default {
  components: { InsightHeader, TitleDescription },
  data() {
    return {
      slug: this.$route.params.insight,
      filters: this.$route.query.location,
    }
  },
  methods: {
    filterProduct() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, {
          location: 'USA',
          time: '1week',
        }),
      })
    },
  },
  created() {
    console.log(this.$route.query)
  },
}
</script>

<style scoped lang="sass">
@import "assets/styles/theme"

.mainContentContainer
  margin: 0 32px

  display: flex
  flex-wrap: wrap
  flex-direction: column

  gap: 32px

.heading
  display: flex

h2
  margin: 16px 0

img
  margin: auto
  display: flex
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
