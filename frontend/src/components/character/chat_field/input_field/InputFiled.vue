<script setup>

import SendIcon from "@/components/character/chat_field/input_field/icon/SendIcon.vue";
import MicIcon from "@/components/character/chat_field/input_field/icon/MicIcon.vue";
</script>

<template>
  <div class="absolute bottom-4 left-4 h-12 w-86 flex items-center">
    <input
        class="input bg-black/30 backdrop-blur-sm w-full h-full text-white text-base rounded-2xl pr-20"
        type="text"
        placeholder="文本输入"
    >
    <div class="absolute right-2 w-8 h-8 flex justify-center items-center cursor-pointer">
      <SendIcon />
    </div>
    <div class="absolute right-10 w-8 h-8 flex justify-center items-center cursor-pointer">
      <MicIcon />
    </div>
  </div>
</template>

<style scoped>

</style>