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

          <insight-list />
        </span>

        <span>
          <content-heading
            text="You liked"
            :link="'/search/insights/' + searchTerm"
          />

          <insight-list :number="false" :confidence_levels="false" />
        </span>
      </section>

      <section>
        <content-heading
          text="Insights"
          :link="'/search/insights/' + searchTerm"
        />

        <tall-card-list />
      </section>

      <section>
        <content-heading
          text="Dashboards"
          :link="'/search/insights/' + searchTerm"
        />

        <tall-card-list />
      </section>
    </div>
  </div>
</template>

<script>
import CompanyHeader from '~/components/company_header/CompanyHeader.vue'
import ContentHeading from '~/components/content_heading/ContentHeading.vue'
export default {
  components: { CompanyHeader, ContentHeading },
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
