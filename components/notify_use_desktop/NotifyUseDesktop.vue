<template>
  <error
    :error="{
      statusCode: -1,
      message: 'This site is only available on desktop.',
      details: 'Mobile support will be added at a later date.',
    }"
  />
</template>

<script>
import error from '~/layouts/error.vue'
export default {
  components: { error },
  name: 'NotifyUseDesktop',
}
</script>
