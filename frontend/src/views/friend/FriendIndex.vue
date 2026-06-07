<script setup>
import {nextTick, onBeforeMount, onBeforeUnmount, onMounted, ref, useTemplateRef} from "vue";
import api from "@/js/http/api.js";
import Character from "@/components/character/Character.vue";

const friends=ref([])
const sentinelRef= useTemplateRef('sentinel-ref')
const isLoading = ref(false);
const hasFriend = ref(true);

function checkSentinelRef(){
  if(!sentinelRef.value) return false
  const rect = sentinelRef.value.getBoundingClientRect()
  return rect.top < window.innerHeight && rect.bottom >0
}

function removeFriend(friendId){
  friends.value = friends.value.filter(f =>f.id !== friendId)
}

async function loadMore() {
  if (isLoading.value || !hasFriend.value) return
  isLoading.value = true
  let newFriends = []
  try{

    const res = await api.get('/api/friend/get_list/',{
      params: {
        items_count:friends.value.length
      }
    })
    const data =res.data
    if(data.result ==='success'){
      newFriends = data.friends
    }
  }catch(err){

  }finally {
    isLoading.value = false
    if(newFriends.length === 0){
      hasFriend.value = false
    }else{
      friends.value.push(...newFriends)
      await nextTick()

      if(checkSentinelRef){
        await loadMore()
      }
    }
  }
}
let observer = null

onMounted(async() => {
  await loadMore()
  await nextTick()

  observer = new IntersectionObserver(
      entries =>{
        entries.forEach(entry =>{
          if(entry.isIntersecting){
            loadMore()
          }
        })
      },
      {root:null,rootMargin:'2px',threshold:0}
  )

  observer.observe(sentinelRef.value)

})

onBeforeUnmount(() => {
  observer?.disconnect()
})
</script>

<template>
  <div class="flex flex-col items-center mb-12">
    <div class="grid grid-cols-[repeat(auto-fill,minmax(240px,1fr))] gap-9 mt-12 justify-items-center w-full px-9">
      <Character
        v-for="friend in friends"
        :key="friend.id"
        :character="friend.character"
        :canRemoveFriend="true"
        :friendId="friend.id"
        @remove="removeFriend"
      />
    </div>
    <div ref="sentinel-ref" class=" h-2 mt-8"></div>
    <div v-if="isLoading" class="text-gray-500 mt-4">加载中...</div>
    <div v-if="!hasFriend" class="text-gray-500 mt-4">没有更多聊天了</div>
  </div>


</template>

<style scoped>

</style>