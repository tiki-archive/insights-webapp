<template>
  <error
    :error="{
      statusCode: 115,
      message: 'Your screen is too small.',
      details:
        'You must use a device with a bigger screen like a tablet, laptop, or desktop. Support for smaller screens will be added at a later date.',
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
