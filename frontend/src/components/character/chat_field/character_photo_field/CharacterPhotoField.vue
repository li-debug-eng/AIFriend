<script setup>
defineProps(['character'])

</script>

<template>
  <div class="absolute top-6 h-10 left-2 right-22 bg-black/50 w-fit flex items-center justify-center gap-2 px-2 rounded-full">
    <div class="avatar">
      <div class=" w-8 rounded-full">
        <img :src="character.photo" alt="">
      </div>
    </div>
    <div class="text-white text-sm break-all line-clamp-1">
      {{ character.name }}
    </div>

  </div>
</template>

<style scoped>

</style>