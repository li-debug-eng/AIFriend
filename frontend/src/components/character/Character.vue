<script setup>
import {ref} from "vue";
import {useUserStore} from "@/stores/user.js";
import UpdateCharacter from "@/views/create/character/UpdateCharacter.vue";
import UpdateIcon from "@/components/character/icon/UpdateIcon.vue";
import RemoveIcon from "@/components/character/icon/RemoveIcon.vue";
import api from "@/js/http/api.js";

const props = defineProps(['character','canEdit'])
const emit = defineEmits(['remove'])
const isHover = ref(false)
const user = useUserStore()

async function handleRemoveCharacter(){
  try{
    const res = await api.post('api/create/character/remove/',{
      character_id: props.character.id,
    })
    if (res.data.result === 'success'){
      emit('remove',props.character.id)
    }
  }catch(err){
    console.log(err)
  }
}

</script>

<template>
  <div>
    <div class="avatar cursor-pointer" @mouseover="isHover = true" @mouseout="isHover = false">
      <div class="w-60 h-100 rounded-2xl relative transition-transform duration-300" :class="{'scale-120' : isHover}">
        <img :src="character.background_image" alt="" />
        <div class="absolute left-0 top-50 w-60 h-50 bg-linear-to-t from-black/40 to-transparent"></div>
        <div v-if="canEdit&& character.author.user_id === user.id" class="absolute top-50 right-0">
          <RouterLink :to="{name:'update-character',params:{character_id:character.id}}" class="btn btn-circle btn-ghost bg-transparent">
            <UpdateIcon/>
          </RouterLink>
          <button @click="handleRemoveCharacter" class="btn btn-circle btn-ghost bg-transparent">
            <RemoveIcon/>
          </button>
        </div>
        <div class="absolute top-54 left-4 avatar">
          <div class="rounded-full w-16 ring-3 ring-white">
            <img :src="character.photo" alt="">
          </div>
        </div>
        <div class="absolute  top-56 left-24 text-3xl text-white font-bold line-clamp-1 break-all" >
          {{character.name}}
        </div>
        <div class="absolute top-75 left-5 right-5 text-white line-clamp-4 break-all">
          {{character.profile}}
        </div>
      </div>
    </div>
    <RouterLink :to="{name:'user-space-index',params :{user_id: character.author.user_id}}" class="flex items-center mt-4 gap-2 w-60">
      <div class="avatar">
        <div class="w-7 rounded-full">
          <img :src="character.author.photo" alt="">
        </div>
      </div>
      <div class="text-sm line-clamp-1 break-all">{{character.author.username}}</div>
    </RouterLink>
  </div>
</template>

<style scoped>

</style>