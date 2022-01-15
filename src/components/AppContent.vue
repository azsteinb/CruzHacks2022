<template>
  <div id="content" class="mt-4 mb-4">
    <input type='file' class="button is-primary is-large mt-4">Upload Shit
    <button class="button is-primary is-large mt-4" v-on:click="upload_file()">Upload Shit</button>
  </div>
</template>

<script>
  export default {
    methods: {
      select_file () {
        console.log('selecting file')
      },
      on_file_select () {
          console.log('file has been selected')
      }


    }
  }
</script>