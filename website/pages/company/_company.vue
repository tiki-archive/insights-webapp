<template>
  <div class="companyPageContainer">
    <company-header
      name="Dr Martens"
      :monthly_users="'103,301'"
      :following="this.following"
      @setFollowing="setFollowing"
    />

    <div class="themeStandardPageContainer companyPageContent">
      <section class="themeMultiContentSection">
        <span>
          <content-heading
            text="Popular"
            :link="'/search/insights/' + searchTerm"
          />

          <insight-list-cmp />
        </span>

        <span>
          <content-heading
            text="You liked"
            :link="'/search/insights/' + searchTerm"
          />

          <insight-list-cmp :number="false" :confidence_levels="false" />
        </span>
      </section>

      <section>
        <content-heading
          text="Insights"
          :link="'/search/insights/' + searchTerm"
        />

        <tall-card-list-cmp />
      </section>

      <section>
        <content-heading
          text="Dashboards"
          :link="'/search/insights/' + searchTerm"
        />

        <tall-card-list-cmp />
      </section>
    </div>
  </div>
</template>

<script>
import CompanyHeader from '~/components/company_header/CompanyHeaderCmp.vue'
import ContentHeading from '~/components/content_heading/ContentHeadingCmp.vue'
import InsightListCmp from '~/components/insight_list/InsightListCmp.vue'
import TallCardListCmp from '~/components/tall_card_list/TallCardListCmp.vue'
export default {
  components: {
    CompanyHeader,
    ContentHeading,
    InsightListCmp,
    TallCardListCmp,
  },
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

<style scoped lang="sass">
@import "assets/styles/theme/default"
.companyPageContainer
  margin: auto 0
.companyPageContent
  margin-top: $page-row-gap
</style>
